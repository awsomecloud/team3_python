class ec2:

    def __init__(self, ec2_client):
        self.ec2 = ec2_client

    def import_ec2_service(self):
        response = self.ec2.describe_instances(
            Filters=[
                {
                    'Name': 'instance-state-name',
                    'Values': ['stopped']
                }
            ]
        )
        return response
