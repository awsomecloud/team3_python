class quota:
    def __init__(self,quota):
        self.ec2 = quota

    def import_service_quota(self):
        response = self.quota.get_service_quota(
            ServiceCode = 'ec2',
            QuotaCode = 'L-1216C47A'
        )

        return response