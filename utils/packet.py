class Packet:
    def __init__(self, src, dest, data):
        self.src = src
        self.dest = dest
        self.data = data

    def __str__(self):
        return f"{self.src} -> {self.dest} : {self.data}"  #Used for printing

    # Convert to binary
    def to_binary(self):
        return ' '.join(format(ord(c), '08b') for c in self.data)