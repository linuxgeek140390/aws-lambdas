import boto3
region= "ap-southeast-2"
client = boto3.client('ec2',region_name=region)
custom_filter = [{    'Name':'tag:Scheduling',    'Values': ['enabled']}]
response = client.describe_instances(Filters=custom_filter)
#print(response)
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        if instance['State']['Name'] == 'running':
            res=(instance["InstanceId"])
            #print(type(res))
            print(res)
            client.stop_instances(InstanceIds=[res])
