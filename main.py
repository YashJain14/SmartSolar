from sense_hat import SenseHat
from time import sleep
from random import uniform

sense = SenseHat()
userchoice = 0
userinput = 0.0
sourceintensity = 0.0
modulator = 0.0
roomintensity = 0.0
artificialintensity = 0.0
print("1: Change room light intensity\n2: Display current light data")

while True:
    sourceintensity = uniform(0.0,1000.0)
    try:
      userchoice = int(input("Enter your choice: "))
    except:
      print("Invalid input, enter 1 or 2 only")
      continue
    if ((userchoice != 1) and (userchoice != 2)):
      print("Invalid input, enter 1 or 2 only")
      continue
    
    if (userchoice == 1):
      userinput = float(input("Set room light intensity: "))
      
    if (userinput <= sourceintensity):
      artificialintensity = 0.0
      modulator = sourceintensity - userinput
      roomintensity = sourceintensity - modulator
    else:
      modulator = 0.0
      artificialintensity = userinput - sourceintensity
      roomintensity = sourceintensity + artificialintensity
    
    if (userchoice == 2):
      print("Room light intensity: {a}\nArtificial light intensity: {b}\nExternal light intensity: {c}\nModulator: {d}".format(a = roomintensity, b = artificialintensity, c = sourceintensity, d = modulator))
