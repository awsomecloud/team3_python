import boto3
import ec2_service
import service_quota
import re

def vcpuusage():
    ec2 = boto3.client('ec2')
    ec2_class = ec2_service.instance.import_ec2_service(ec2)
    total = 0

# instance describe
    for i in range(len(ec2_class['Reservations'])):
        instancetype = ec2_class['Reservations'][i]['Instances'][0]['InstanceType']
        vcpu = ec2_class['Reservations'][i]['Instances'][0]['CpuOptions']
        core = ec2_class['Reservations'][i]['Instances'][0]['CpuOptions']['CoreCount']
        threads = ec2_class['Reservations'][i]['Instances'][0]['CpuOptions']['ThreadsPerCore']
        print (instancetype)

        #  All Standard (A, C, D, H, I, M, R, T, Z) instances
        if instancetype[:1] in ["a","c","d","h","i","m","r","t","z"] :
            total += (core*threads)

    print (total)
    return total

def vcpuquota():
    quota = boto3.client('service-quotas')
    quota_class = service_quota.quota.import_service_quota(quota)
    vcpu_quota = quota_class['Quota']['Value']
    print (vcpu_quota)
    return quota_class


vcpuusage()
vcpuquota()