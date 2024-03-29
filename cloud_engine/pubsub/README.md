# Cloud Run Pub/Sub Tutorial Sample

This sample shows how to create a service that processes Pub/Sub messages.

Use it with the [Cloud Pub/Sub with Cloud Run tutorial](http://cloud.google.com/run/docs/tutorials/pubsub).

[![Run in Google Cloud][run_img]][run_link]

[run_img]: https://deploy.cloud.run/button.svg
[run_link]: https://deploy.cloud.run/?git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&dir=run/pubsub

## Build

```
docker build --tag pubsub-tutorial:python .
```

## Run Locally

```
docker run --rm -p 9090:8080 -e PORT=8080 pubsub-tutorial:python
```

## Test

```
pytest
```

_Note: you may need to install `pytest` using `pip install pytest`._

## Deploy

```
export GOOGLE_APPLICATION_CREDENTIALS="/home/frank/university/dynARTwork/devices/credential/DynArtWork-5537e0885c4e.json"
export GOOGLE_CLOUD_PROJECT=dynartwork-277815
```

# Submit a build using Google Cloud Build
```
gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/pubsub-tutorial

# Deploy to Cloud Run
gcloud beta run deploy sensors-service --image gcr.io/${GOOGLE_CLOUD_PROJECT}/pubsub-tutorial
```
