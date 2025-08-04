import boto3
import os

def upload_file(local_path, bucket, s3_path):
    s3 = boto3.client('s3')
    s3.upload_file(local_path, bucket, s3_path)
    print(f'Uploaded {local_path} to s3://{bucket}/{s3_path}')

if __name__ == '__main__':
    upload_file('../data/sample_api_output.csv', 'your-bucket-name', 'outputs/sample_api_output.csv')
