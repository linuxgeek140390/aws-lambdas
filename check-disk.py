import boto3
import botocore
import time
#ssm_client = boto3.client('ssm',region_name='us-east-1')
cmd = 'disk_usage=`df -h / | awk \'{print $5}\' | tail -1 | sed \'s/.$//\'` ; if [ $disk_usage -gt 20 ]; then echo "file system utilization is high"; sleep 2 ; echo "system will be rebooted"; fi'

def handler(event=None, context=None):
    client = boto3.client('ssm', region_name='us-east-1')

    instance_id = instance_id = event['Trigger']['Dimensions'][0]['value'] # hard-code for example
    response = client.send_command(
        InstanceIds=[instance_id],
        DocumentName='AWS-RunShellScript',
        Parameters={
            'commands': [
                # Simple test if a file exists
                cmd
            ]
        }
    )
    command_id = response['Command']['CommandId']
    tries = 0
    output = 'False'
    while tries < 10:
        tries = tries + 1
        try:
            time.sleep(0.5)  # some delay always required...
            result = client.get_command_invocation(
                CommandId=command_id,
                InstanceId=instance_id,
            )
            if result['Status'] == 'InProgress':
                continue
            output = result['StandardOutputContent']
            break
        except client.exceptions.InvocationDoesNotExist:
            continue
    return output == 'True'
