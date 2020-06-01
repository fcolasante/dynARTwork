# Copyright 2019 Google, LLC.
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

# [START run_pubsub_server_setup]
import base64
import os
import sys
import tempfile
import json
from google.cloud import storage, vision
from wand.image import Image
storage_client = storage.Client()
from flask import Flask, request

import image

app = Flask(__name__)
# [END run_pubsub_server_setup]


# [START run_pubsub_handler]
@app.route('/', methods=['POST'])
def index():
    envelope = request.get_json()
    if not envelope:
        msg = 'no Pub/Sub message received'
        print(f'error: {msg}')
        return f'Bad Request: {msg}', 410

    if not isinstance(envelope, dict) or 'message' not in envelope:
        msg = 'invalid Pub/Sub message format'
        print(f'error: {msg}')
        return f'Bad Request: {msg}', 411

    pubsub_message = envelope['message']

    name = 'World'
    if isinstance(pubsub_message, dict) and 'data' in pubsub_message:
        print(base64.b64decode(pubsub_message['data']).decode('utf-8'))
        try:
            data = json.loads(
                base64.b64decode(pubsub_message['data']).decode('utf-8'))
        except Exception as e:
            msg = ('Invalid Pub/Sub message: '
                   'data property is not valid base64 encoded JSON')
            print(f'error: {e}')
            return f'Bad Request: {msg}', 412
    
        # Validate the message is a Cloud Storage event.
        if not data["name"] or not data["data"]:
            msg = (data)
            print(f'error: {msg}')
            return f'Bad Request: {msg}', 413

        file_name="test.jpg"
        bucket_name = "dynartwork-277815.appspot.com"

        blob = storage_client.bucket(bucket_name).get_blob(file_name)
        print(f'Hello {name}!')

        try:
            image.blur_offensive_images(data)
            # Flush the stdout to avoid log buffering.
            sys.stdout.flush()
            return ('', 204)

        except Exception as e:
            print(f'error: {e}')
            return ('', 500)

        # Flush the stdout to avoid log buffering.
        sys.stdout.flush()

    return ('', 204)
# [END run_pubsub_handler]


if __name__ == '__main__':
    PORT = int(os.getenv('PORT')) if os.getenv('PORT') else 8080

    # This is used when running locally. Gunicorn is used to run the
    # application on Cloud Run. See entrypoint in Dockerfile.
    app.run(host='127.0.0.1', port=PORT, debug=True)
