import boto3


# Create an S3 client
bohoo = boto3.client('s3')

# List all S3 buckets
response = bohoo.list_buckets()

print("S3 Buckets:")
for cat in response['Buckets']:
    print(f"- {cat['Name']}")

Bucket_name='cool1337'
response = bohoo.get_bucket_location(Bucket=Bucket_name)
print(Bucket_name)
print(f"Region: {response['LocationConstraint']}")

# creating a bucket
print("we are creating buckets")
for i in range(0,3):
    buckets=str(input("Enter the bucket name"))
    creating_bucket=buckets.replace(" ","")
    response = bohoo.create_bucket(
    Bucket=creating_bucket,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1', 
    },
)

print(" creating bucket: ")

 