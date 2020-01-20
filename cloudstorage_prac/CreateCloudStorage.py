from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    bucket_name = "teststorechakra"
    source_file_name = "/Users/demo/Documents/learn/gcp/Setting_gcp_datalabs.sh"
    destination_blob_name = "testcloud sdk"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

upload_blob("teststorechakra","/Users/demo/Documents/learn/gcp/Setting_gcp_datalabs.sh","testcloud sdk")