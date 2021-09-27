import boto3
region= "ap-southeast-1"
client = boto3.client('docdb',region_name=region)
#custom_filter = [{    'Name':'tag:Scheduling',    'Values': ['enabled']}]
response = client.describe_db_clusters()
#print(response)
for i in response['DBClusters']:
    db_instance_name = i['DBClusterIdentifier']
    db_instance_arn = i['DBClusterArn']
    #print(db_instance_name)
    #print(db_instance_arn)
    tagCheckPass = 'false'
    ClusterTags = client.list_tags_for_resource(ResourceName=db_instance_arn)
    #print(ClusterTags)
    for ClusterTag in ClusterTags["TagList"]:
        if 'env' in ClusterTag["Key"]:
            if 'prod' in ClusterTag["Value"]:
                tagCheckPass = 'true'
                print(tagCheckPass)
                stop_res = client.stop_db_cluster(DBClusterIdentifier='string')

~
