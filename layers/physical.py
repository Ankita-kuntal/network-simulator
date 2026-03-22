class Connection:
    def __init__(self):
        self.devices = []

    def connect(self, device):
        self.devices.append(device)

    def transmit(self, sender, packet):
        for device in self.devices:
            if device != sender:
                device.receive(packet)