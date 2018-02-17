import fmc_rest_client.core.base_resources

class DeviceRecord(fmc_rest_client.core.base_resources.DeviceResource):
    
    def __init__(self, name=None, default_action='TRUST', desc=None):
        super().__init__(name)
        self.name = name
        self.description = desc

