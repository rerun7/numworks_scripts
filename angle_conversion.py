import math

# All Functions
def dmsToDegrees(hours, minutes, seconds):
    deg = hours + float(minutes)/60 + float(seconds)/3600
    return deg

def dmsToRadians(hours, minutes, seconds):
    deg = hours + float(minutes)/60 + float(seconds)/3600
    return math.radians(deg)

def radiansToDms(rad):
    seconds = rad % 60
    minutes = (rad / 60) % 60
    degrees = rad / (60 * 60)
    return seconds, minutes, degrees

def radiansToDegrees(rad):
    return math.degrees(rad)

def degreesToDms(deg):
    start = abs(float(deg))
    hours = int(start)
    left = start - hours
    minutes = int(left * 60)
    seconds = (left % 60) / float(3600)   

    if deg < 0: 
        degrees = degrees * -1

    return degrees, minutes, seconds 


def degreesToRadians(deg):
    return math.radians(deg)
    print()

# Excecuting Program
print("------ Mode ------")
mode = int(input("1: Dms to Deg\n2: Dms to Rad\n3: Rad to Dms\n4: Rad to Deg\n5: Deg to Dms\n6: Deg to Rad\n\nMode: "))
print()

if (mode == 1):
    hours = float(input("Hours: "))
    minutes = float(input("Minutes: "))
    seconds = float(input("Seconds: "))
    print()
    print(dmsToDegrees(hours, minutes, seconds))

elif (mode == 2):
    hours = float(input("Hours: "))
    minutes = float(input("Minutes: "))
    seconds = float(input("Seconds: "))
    print()
    print(dmsToRadians(hours, minutes, seconds))

elif (mode == 3):
    radians = float(input("Radians: "))
    print()
    print(radiansToDms(radians))

elif (mode == 4):
    radians = float(input("Radians: "))
    print()
    print(radiansToDegrees(radians))

elif (mode == 5):
    degrees = float(input("Degrees: "))
    print()
    print(degreesToDms(degrees))

elif (mode == 6):
    degrees = float(input("Degrees: "))
    print()
    print(degreesToRadians(degrees))

else:
    print("Not in range.")