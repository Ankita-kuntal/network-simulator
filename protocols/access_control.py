import random

def csma_cd():
    print("\n[Access Control: CSMA/CD]")
    success = random.choice([True, False])

    if success:
        print("Channel free")
        return True
    else:
        print("Collision detected! Retry...")
        return False