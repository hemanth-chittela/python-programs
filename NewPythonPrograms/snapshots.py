import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_snapshots(OwnerIds=['self'])
print(response)
#print(response['Snapshots'][0]['SnapshotId'])
response1 = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
active_instanceIds=set()
#print("instance id",response1['Reservations'][0]['Instances'][0]['InstanceId'])
print("-------------------------------------------------------")
for i in response1['Reservations']:
    for j in i['Instances']:
        active_instanceIds.add(j['InstanceId'])

for king in response['Snapshots']:
    snapshot_id = king['SnapshotId']
    volume_id = king.get('VolumeId')

    if not volume_id:
            # Delete the snapshot if it's not attached to any volume
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")
    else:
            print("cannot be deleted as the snapshots",snapshot_id,"are connnected to the volumes",volume_id,)
            # Check if the volume still exists
            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['Volumes'][0]['Attachments']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # The volume associated with the snapshot is not found (it might have been deleted)
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")