import boto3
def cartoon():
    client = boto3.client('s3')
    Bucket=input("Enter the bucket name: ")
    try:
        response = client.create_bucket(
        Bucket=Bucket,
        CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
        
    }
    )
        print("s3 bucket",Bucket,"is created")
    except:
        print("s3 bucket exists")
    finally:
        response = client.get_bucket_acl(
        Bucket='pokemon1337',
    )
    print(response['ResponseMetadata']['HostId'])
    print(response['ResponseMetadata']['HTTPStatusCode'])
cartoon()
