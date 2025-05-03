# inspiration code for Python Unit Testing Project

import math

def surfaceArea(radius):
    return 4 * math.pi * radius**2

def volume(radius):
    return (4/3) * math.pi * radius**3

def prompt():
    print()
    print("---------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("---------------------------------------------------")
    radius = float(input("Please Enter the radius: "))
    result = volume(radius)
    print(f"The Volume is: {result}")
    return result

if __name__ == '__main__':
    prompt()

