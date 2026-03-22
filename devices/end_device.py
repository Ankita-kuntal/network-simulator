class EndDevice:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.hub = None
        self.switch = None

    def connect(self, connection):
        self.connection = connection     #Connect device to wire
        connection.connect(self)

    def send(self, packet):
        print(f"{self.name} sending {packet}")      #Device starts transmission

        if self.hub:
            self.hub.receive(packet, self)

        elif self.switch:
            self.switch.receive(packet, self)

        elif self.connection:
            self.connection.transmit(self, packet)

    def receive(self, packet):
        if packet.dest == self.name:
            print(f"{self.name} received: {packet.data}")   #Device accepts only its own data