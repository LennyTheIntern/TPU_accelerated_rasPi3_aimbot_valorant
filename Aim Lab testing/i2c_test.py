from smbus import SMBus

addr = 0x8
bus = SMBus(1)

numb = 11234

print("Enter 1")
while(True):
    numb = input("enter Number:")
    bus.write_byte(addr,numb >> 0)
    bus.write_byte(addr,numb >> 8)

