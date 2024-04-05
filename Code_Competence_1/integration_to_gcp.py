import json
import google.cloud.storage
from datetime import datetime

with open("canvas-joy-418901-707fd80a567d.json") as f:
    service_account_info = json.load(f)

credentials_info = google.oauth2.service_account.Credentials.from_service_account_info(
    service_account_info
)

storage_client = google.cloud.storage.Client(credentials=credentials_info)

bucket = storage_client.get_bucket("sentiment_chatgpt_storage_cc1")

datetime_now = datetime.now().strftime("%d%m%Y-%H-%M-%S")

blob = bucket.blob(f"data-{datetime_now}/sentiment_good.csv")
blob.upload_from_filename("sentiment_good.csv")

blob = bucket.blob(f"data-{datetime_now}/sentiment_bad.csv")
blob.upload_from_filename("sentiment_bad.csv")

blob = bucket.blob(f"data-{datetime_now}/sentiment_neutral.csv")
blob.upload_from_filename("sentiment_neutral.csv")

blob = bucket.blob(f"data-{datetime_now}/sentiment_counts.csv")
blob.upload_from_filename("sentiment_counts.csv")

blob = bucket.blob(f"data-{datetime_now}/sentiment_chatgpt.sql")
blob.upload_from_filename("sentiment_chatgpt.sql")

print("File Uploaded to Bucket")