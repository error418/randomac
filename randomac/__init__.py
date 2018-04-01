from random import randint

def main():
    mac = []
    for i in range(0,5):
        mac.append(hex(randint(0, 255))[2:])
    
    print ':'.join(mac)

main()