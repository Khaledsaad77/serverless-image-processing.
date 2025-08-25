import boto3
import urllib.parse

s3 = boto3.client('s3')
DEST_BUCKET = "img-ingest-output"

def lambda_handler(event, context):
    try:
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
        print(f"📥 Incoming key: {key} from {source_bucket}")

        if source_bucket == DEST_BUCKET or key.startswith("img-ingest-output/"):
            print(f"⏭️ Skipping {key} (already in output bucket)")
            return {"status": "skipped"}

        filename = key.split("/")[-1]
        # تغيير الامتداد فقط
        if filename.endswith(".png"):
            filename = filename.replace(".png", ".jpg")

        dest_key = filename

        # نسخ الملف كما هو بدون تعديل فعلي
        s3.copy_object(
            Bucket=DEST_BUCKET,
            CopySource={'Bucket': source_bucket, 'Key': key},
            Key=dest_key
        )

        print(f"✅ Renamed and copied {key} → {DEST_BUCKET}/{dest_key}")
        return {"status": "success", "dest_key": dest_key}

    except Exception as e:
        print(f"❌ Error during copy: {str(e)}")
        raise
