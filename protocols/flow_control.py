def stop_and_wait(sender, packet):
    print("\n[Flow Control: Stop & Wait]")

    sender.send(packet)

    ack = True  # simulate ACK

    if ack:
        print("ACK received")
    else:
        print("Resending packet")
        sender.send(packet)