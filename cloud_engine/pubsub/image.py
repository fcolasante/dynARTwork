# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# [START run_imageproc_handler_setup]
import os
import tempfile
import json
from google.cloud import storage, vision
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

import numpy as np; np.random.seed(0)
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


storage_client = storage.Client()
vision_client = vision.ImageAnnotatorClient()
# [END run_imageproc_handler_setup]


# [START run_imageproc_handler_analyze]
# Blurs uploaded images that are flagged as Adult or Violence.
def blur_offensive_images(data):
    file_data = data

    file_name = file_data['name']
    bucket_name = "dynartwork-277815.appspot.com"

    blob = storage_client.bucket(bucket_name).get_blob(file_name)
    blob_uri = f'gs://{bucket_name}/{file_name}'
    blob_source = {'source': {'image_uri': blob_uri}}

    # Ignore already-blurred files
    if file_name.startswith('blurred-'):
        print(f'The image {file_name} is already blurred.')
        return

    print(f'Analyzing {file_name}.')

    result = vision_client.safe_search_detection(blob_source)
    detected = result.safe_search_annotation

    # Process image
    if detected.adult == 5 or detected.violence == 5:
        print(f'The image {file_name} was detected as inappropriate.')
        return __blur_image(blob, json.dumps(data))
    else:
        print(f'The image {file_name} was detected as OK.')
# [END run_imageproc_handler_analyze]


# [START run_imageproc_handler_blur]
# Blurs the given file using ImageMagick.
def __blur_image(current_blob, data):
    file_name = current_blob.name
    _, temp_local_filename = tempfile.mkstemp()

    # Download file from bucket.
    current_blob.download_to_filename(temp_local_filename)
    print(f'Image {file_name} was downloaded to {temp_local_filename}.')

    # Blur the image using ImageMagick.
    with Image(filename=temp_local_filename) as image:
        with Drawing() as draw:
            draw.stroke_color = Color('black')
            draw.stroke_width = 2
            draw.fill_color = Color('white')
            draw.arc(( 25, 25),  # Stating point
                    ( 75, 75),  # Ending point
                    (135,-45))  # From bottom left around to top right
            image.resize(*image.size, blur=16, filter='hamming')
            draw(image)
            image.save(filename=temp_local_filename)

    print(f'Image {file_name} was blurred.')

    # Upload result to a second bucket, to avoid re-triggering the function.
    # You could instead re-upload it to the same bucket + tell your function
    # to ignore files marked as blurred (e.g. those with a "blurred" prefix)
    blur_bucket_name = "processed_artworks"
    blur_bucket = storage_client.bucket(blur_bucket_name)
    new_blob = blur_bucket.blob(file_name)
    new_blob.upload_from_filename(temp_local_filename)
    print(f'Blurred image uploaded to: gs://{blur_bucket_name}/{file_name}')

    # Delete the temporary file.
    os.remove(temp_local_filename)
# [END run_imageproc_handler_blur]
def build_image(data):
    import urllib
    import io, base64
    _, temp_local_filename = tempfile.mkstemp()
    print(os.stat(temp_local_filename))
    fig, ax = plt.subplots()
    im = ax.imshow(data['data'])
    fig.tight_layout()
    #ax.get_figure().savefig(temp_local_filename)
    buf = io.BytesIO()
    plt.axis('off')
    fig.savefig(buf, format='png')
    buf.seek(0)
    image_as_a_string = buf.read()

    file_name = f"data_{data['name']}.png"
    blur_bucket_name = "processed_artworks"
    blur_bucket = storage_client.bucket(blur_bucket_name)
    new_blob = blur_bucket.blob(file_name)
    new_blob.upload_from_string(image_as_a_string, content_type='image/png' )
    
    print(f'Data image uploaded to: gs://{blur_bucket_name}/{file_name}')

    # Delete the temporary file.
    os.remove(temp_local_filename)
