import boto3
import sys
import json
import csv
import ec2_service
from boto3.session import Session

def main():
    sys.stdout = open ('ec2_class.txt','w')
    ec2 = boto3.client('ec2')
    ec2_class = ec2_service.instance.import_ec2_service(ec2)
    # running = ec2_class.import_ec2_service()
    # for i in range(len(running['Reservations'])):
    #     instancename = running['Reservations'][i]['Instances'][0]['Tags'][0]['Value']
    #     instanceid = running['Reservations'][i]['Instances'][0]['InstanceId']
    #     instancetype = running['Reservations'][i]['Instances'][0]['InstanceType']
    #     publicipaddr = running['Reservations'][i]['Instances'][0]['PublicIpAddress']
    #     privateipaddr = running['Reservations'][i]['Instances'][0]['PrivateIpAddress']
    #     availablezone = running['Reservations'][i]['Instances'][0]['Placement']['AvailabilityZone']
    #     print(instancename, instanceid, instancetype, availablezone, privateipaddr, publicipaddr)
    print(ec2_class['Reservations'])

    # for reservation in ec2_class['Reservations'] :
    #     print(len(reservation['Instances']))

    return ec2_class

def conversion():


main()


