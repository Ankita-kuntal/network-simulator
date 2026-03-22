class EndDevice:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.hub = None
        self.switch = None

    def connect(self, connection):
        self.connection = connection
        connection.connect(self)

    def send(self, packet):
        print(f"{self.name} sending {packet}")

        if self.hub:
            self.hub.receive(packet, self)

        elif self.switch:
            self.switch.receive(packet, self)

        elif self.connection:
            self.connection.transmit(self, packet)

    def receive(self, packet):
        if packet.dest == self.name:
            print(f"{self.name} received: {packet.data}")