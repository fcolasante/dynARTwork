from google.cloud import storage
# create storage client
storage_client = storage.Client.from_service_account_json('dynartwork-277815-firebase-adminsdk-jsi7c-6e0190638b.json')
# get bucket with name
bucket = storage_client.get_bucket('processed_artworks')
# get bucket data as blob

blob = bucket.get_blob('test.jpg')
# convert to stringfil
json_data = blob.download_as_string()

text_file = open("sample.jpg", "wb")
n = text_file.write(json_data)
text_file.close()
import subprocess

#Display the image
image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-q", "-B", "black", "-g", "1280x800", "/home/pi/Documents/sample.jpg"])

# Do other stuff here...

# You can now close the image by doing
#image.kill()