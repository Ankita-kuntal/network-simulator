class Bridge:
    def __init__(self, name):
        self.name = name
        self.devices = []

    def connect(self, device):
        self.devices.append(device)

    def forward(self, packet):
        print(f"{self.name} forwarding {packet}")
        for d in self.devices:
            d.receive(packet)