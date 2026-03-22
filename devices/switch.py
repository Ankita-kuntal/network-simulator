class Switch:
    def __init__(self, name):
        self.name = name
        self.mac_table = {}
        self.devices = []

    def connect(self, device):
        self.devices.append(device)
        device.switch = self

    def receive(self, packet, sender):
        print(f"\n{self.name} received {packet}")

        # MAC Learning
        self.mac_table[packet.src] = sender
        print(f"Learning: {packet.src} -> {sender.name}")

        # Show MAC Table
        print("MAC Table:", {k: v.name for k, v in self.mac_table.items()})

        # Forwarding
        if packet.dest in self.mac_table:
            print("Forwarding to specific device")
            target = self.mac_table[packet.dest]
            target.receive(packet)
        else:
            print("Broadcasting (unknown MAC)")
            for d in self.devices:
                if d != sender:
                    d.receive(packet)