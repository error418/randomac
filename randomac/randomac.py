from random import randint

blockFormat = "{0:0{1}x}"

def generate(separator = ':'):
    mac = []
    for i in range(0,5):
        mac.append(blockFormat.format(randint(0, 255), 2))
    
    return separator.join(mac)