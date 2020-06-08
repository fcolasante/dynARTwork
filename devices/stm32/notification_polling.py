#!/usr/bin/env python

# Copyright 2017 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This application demonstrates how to poll for GCS notifications from a
Cloud Pub/Sub subscription, parse the incoming message, and acknowledge the
successful processing of the message.

This application will work with any subscription configured for pull rather
than push notifications. If you do not already have notifications configured,
you may consult the docs at
https://cloud.google.com/storage/docs/reporting-changes or follow the steps
below:

1. First, follow the common setup steps for these snippets, specically
   configuring auth and installing dependencies. See the README's "Setup"
   section.

2. Activate the Google Cloud Pub/Sub API, if you have not already done so.
   https://console.cloud.google.com/flows/enableapi?apiid=pubsub

3. Create a Google Cloud Storage bucket:
   $ gsutil mb gs://testbucket

4. Create a Cloud Pub/Sub topic and publish bucket notifications there:
   $ gsutil notification create -f json -t testtopic gs://testbucket

5. Create a subscription for your new topic:
   $ gcloud beta pubsub subscriptions create testsubscription --topic=testtopic

6. Run this program:
   $ python notification_polling.py my-project-id testsubscription

7. While the program is running, upload and delete some files in the testbucket
   bucket (you could use the console or gsutil) and watch as changes scroll by
   in the app.
"""
import os
import argparse
import json
import time
import cv2
from google.cloud import storage
from google.cloud import pubsub_v1

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
        #generation = attributes["objectGeneration"]
        var = "Message not important"
        if "data" in object_id:
            message.ack()
        else:
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
            # display the image
            print("Showing image:{}".format(object_id))
            img2 = cv2.imread('./{}'.format(object_id))
            message.ack()
            cv2.imshow("image", img2)
            var = "Image correctly showed"
        print("Result of callback:{}".format(var))
        

    #subscriber.subscribe(subscription_path, callback=callback)
    subscriber.subscribe(subscription_path, callback=callback)
    # The subscriber is non-blocking, so we must keep the main thread from
    # exiting to allow it to process messages in the background.
    print("Listening for messages on {}".format(subscription_path))
    img = cv2.imread('./{}'.format("cristo.jpg"))
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    # for the full screen mode
    #cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    while True:
        cv2.waitKey(0) 
        #time.sleep(60)


    # [END poll_notifications]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "project", help="The ID of the project that owns the subscription"
    )
    parser.add_argument(
        "subscription", help="The ID of the Pub/Sub subscription"
    )
    args = parser.parse_args()
    poll_notifications(args.project, args.subscription)
