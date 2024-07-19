from dotenv import load_dotenv
import os
import boto3

load_dotenv()

R2_ACCESS_KEY = os.getenv("R2_ACCESS_KEY")
R2_SECRET_KEY = os.getenv("R2_SECRET_KEY")
R2_BUCKET_NAME = os.getenv("R2_BUCKET_NAME")
R2_CONNECTION_URL = os.getenv("R2_CONNECTION_URL")
R2_ACCOUNT_ID = os.getenv("R2_ACCOUNT_ID")
R2_TOKEN = os.getenv("R2_TOKEN")

class R2Uploader:
  def __init__(self):
    self.access_key = R2_ACCESS_KEY
    self.secret_key = R2_SECRET_KEY
    self.bucket_name = R2_BUCKET_NAME
    self.connection_url = R2_CONNECTION_URL
    self.account_id = R2_ACCOUNT_ID
    self.token = R2_TOKEN
    
    self.client = self.create_client()
    
  def create_client(self):
    client = boto3.client(
      's3',
      aws_access_key_id=self.access_key,
      aws_secret_access_key=self.secret_key,
      endpoint_url=self.connection_url,
      config=boto3.session.Config(signature_version='s3v4')
    )
    return client
    
  def upload_file(self, file_name, object_name=None):
    if object_name is None:
      object_name = os.path.basename(file_name)
      
    self.client.upload_file(file_name, self.bucket_name, object_name)
    
  def check_if_file_exists(self, object_name):
    try:
      self.client.head_object(Bucket=self.bucket_name, Key=object_name)
      return True
    except:
      return False
    
  def delete_file(self, object_name):
    self.client.delete_object(Bucket=self.bucket_name, Key=object_name)