import boto3
client = boto3.client('rds')
response = client.describe_db_instances()
for i in response['DBInstances']:
    db_instance_name = i['DBInstanceIdentifier']
    db_instance_arn = i['DBInstanceArn']
    print(db_instance_name)
    print(db_instance_arn)
    tagCheckPass = 'false'
    rdsInstanceTags = client.list_tags_for_resource(ResourceName=db_instance_arn)
    for rdsInstanceTag in rdsInstanceTags["TagList"]:
        if 'env' in rdsInstanceTag["Key"]:
            if 'prod' in rdsInstanceTag["Value"]:
                tagCheckPass = 'true'
                print(tagCheckPass)
