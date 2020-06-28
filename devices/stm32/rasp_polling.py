import os
import argparse
import json
import time
#import cv2
from wand.image import Image
from google.cloud import storage
from google.cloud import pubsub_v1
import subprocess

def poll_notifications(project, subscription_name):
    """Polls a Cloud Pub/Sub subscription for new GCS events for display."""
    # [BEGIN poll_notifications]
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(
        project, subscription_name
    )

    def callback(message):
        #show_image(message.attributes['objectId'])
        #print("Received message:\n{}".format(summarize(message)))
        data = message.data.decode("utf-8")
        attributes = message.attributes

        event_type = attributes["eventType"]
        bucket_id = attributes["bucketId"]
        object_id = attributes["objectId"]
        print(object_id)
        message.ack()
        var = "Message not important"
        if "data" in object_id:
            storage_client = storage.Client.from_service_account_json('service_account.json')
            # get bucket with name
            bucket = storage_client.get_bucket('processed_artworks')
            # get bucket data as blob
            blob = bucket.get_blob(object_id)
            # convert to stringfil
            json_data = blob.download_as_string()
            # open file in writing
            text_file = open(object_id, "wb")
            # write on file and close
            n = text_file.write(json_data)
            text_file.close()
            # image to process
            image_to_get = object_id[:-4].split("_")[-1]
            print(image_to_get)
            with Image(filename=image_to_get) as left:
                print('width_1 =', left.width)
                print('height_1 =', left.height)
                # data image
                with Image(filename=object_id) as img2:
                    print('width_2 =', img2.width)
                    print('height_2 =', img2.height)
                    if left.width != img2.width or left.height != img2.height:
                        img2.resize(left.width, left.height)
                        img2.save(filename="resized.png") 
                        with Image(filename="resized.png") as affinity:
                            left.remap(affinity)
                    else:
                        left.remap(img2)
                    left.save(filename="image_displayed.jpg")
            # display the image
            print("Showing image:{}".format(image_to_get))
            #img2 = cv2.imread('./image_displayed.jpg')
            #cv2.imshow("image", img2)
            var = "Image correctly showed"
        print("Result of callback:{}".format(var))
        

    subscriber.subscribe(subscription_path, callback=callback)
    # The subscriber is non-blocking, so we must keep the main thread from
    # exiting to allow it to process messages in the background.
    print("Listening for messages on {}".format(subscription_path))
    #img = cv2.imread('./{}'.format("cristo.jpg"))
    #cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    # for the full screen mode
    #cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    while True:
        #cv2.waitKey(0)
        time.sleep(60)
    # [END poll_notifications]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "project", help="The ID of the project that owns the subscription",
        default="dynartwork-277815"
    )
    parser.add_argument(
        "subscription", help="The ID of the Pub/Sub subscription",
        default="processed-sub"
    )
    args = parser.parse_args()
    poll_notifications(args.project, args.subscription)
