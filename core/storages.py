import boto3, uuid

from my_settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET_NAME

class MyS3Client:
    def __init__(self, access_key, secret_key, bucket_name):
        boto3_s3 = boto3.client(
            's3',
            aws_access_key_id     = access_key,
            aws_secret_access_key = secret_key
        )
        self.s3_client   = boto3_s3
        self.bucket_name = bucket_name
        
    def upload(self, file):
        try:
            file_name  = str(uuid.uuid4())
            extra_args = { 'ContentType' : file.content_type }
            
            self.s3_client.upload_fileobj(
                file,
                self.bucket_name,
                file_name,
                ExtraArgs = extra_args
            )
            return file_name
        
        except:
            None
        
    def delete(self, file_name):
        self.s3_client.delete_object(Bucket=self.bucket_name, Key=file_name)

s3_client = MyS3Client(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET_NAME)

class FileHandler:
    def __init__(self, client):
        self.client = client
    
    def upload(self, file):
        return self.client.upload(file)
    
    def delete(self, file_name):
        return self.client.delete(file_name)  