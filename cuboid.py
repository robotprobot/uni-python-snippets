width = int(input("Please enter width: "))
length = int(input("Please enter length: "))
height = int(input("Please enter height: "))

print("Width is: " + str(width))
print("Length is: " + str(length))
print("Height is: " + str(height))

sideone = width * height
sidetwo = width * length
sidethree = length * height

surfacearea = sideone + sidetwo + sidethree
surfaceareadoubled = surfacearea * 2

print("Surface area is: " + str(surfaceareadoubled))

volume = length * width * height

print("Volume is: " + str(volume))
