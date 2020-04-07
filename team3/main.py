import boto3
import ec2_service

def main():
    ec2_client = boto3.client('ec2')

    ec2 = ec2_service.ec2(ec2_client)
    ec2_response = ec2.import_ec2_service()
    print(ec2_response['Reservations'])
    return ec2_response

main()