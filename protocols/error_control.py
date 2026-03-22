def add_parity(data):
    parity = sum(ord(c) for c in data) % 2
    return data + str(parity)

def check_parity(data):
    content = data[:-1]
    parity = int(data[-1])
    return (sum(ord(c) for c in content) % 2) == parity