initialvelocity = int(input("What is the initial velocity in meters per second (m/s)? "))
timetaken = int(input("What is the time taken in seconds? "))
acceleration = int(input("What is the acceleration in meters per second per second (m/s2)? "))

##distance = ((timetaken * initialvelocity) + (acceleration * timetaken / 2))

distance = (initialvelocity * timetaken) + (acceleration / 2) * (timetaken * timetaken)

print("Distance is: " + str(distance) + "m")
