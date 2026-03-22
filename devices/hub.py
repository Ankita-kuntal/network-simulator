class Hub:
    def __init__(self, name):
        self.name = name
        self.devices = []
                                               #Connect device to hub
    def connect(self, device):
        self.devices.append(device)
        device.hub = self

    def receive(self, packet, sender):
        print(f"{self.name} broadcasting {packet}")
        for device in self.devices:
            if device != sender:             #Hub sends data to ALL devices(broadcasting)
                device.receive(packet)                    