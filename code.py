import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize the S3 client
s3 = boto3.client(
    's3', 
    region_name='us-east-1',  # Replace with your AWS region
    aws_access_key_id='YOUR_ACCESS_KEY_ID',  # Replace with your AWS Access Key ID
    aws_secret_access_key='YOUR_SECRET_ACCESS_KEY'  # Replace with your AWS Secret Access Key
)

# Function to list S3 bucket content
def list_bucket_content(bucket_name, path=''):
    try:
        # List objects in the bucket with an optional prefix (path)
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=path)

        if 'Contents' in response:
            # If content exists, extract the keys (file/directory names)
            content = [item['Key'] for item in response['Contents']]
            print("Bucket Content:", content)
        else:
            print(f"No content found in the specified path '{path}'.")

    except NoCredentialsError:
        print("Error: AWS credentials are not available.")
    except PartialCredentialsError:
        print("Error: AWS credentials are incomplete.")
    except Exception as e:
        print(f"Error: {e}")

# Example Usage:
# List the top-level content of the bucket (no path specified)
list_bucket_content('your-bucket-name')  # Replace with your bucket name

# List content in a specific directory/path inside the bucket
list_bucket_content('your-bucket-name', 'dir1/')  # Replace with your bucket name and path
