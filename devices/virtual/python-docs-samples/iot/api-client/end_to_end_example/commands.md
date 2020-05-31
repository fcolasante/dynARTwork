python cloudiot_pubsub_example_mqtt_device.py \
  --registry_id iot-devices \
  --device_id test-dev \
  --project_id "${DEVSHELL_PROJECT_ID:-Cloud Shell}" \
  --private_key_file rsa_private.pem \
  --algorithm RS256 \
  --ca_certs roots.pem \
  --cloud_region us-central1