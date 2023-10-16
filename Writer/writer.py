from firebase_admin import storage


def upload_to_firebase(fileName):

    # Get a reference to the storage bucket
    bucket = storage.bucket()

    # Upload the file
    blob = bucket.blob('folder85/' + fileName)
    blob.upload_from_filename(fileName)

    # Make the uploaded file public (optional)
    #blob.make_public()

    # Print the public URL of the uploaded file
    print("Your file URL:", blob.public_url)

