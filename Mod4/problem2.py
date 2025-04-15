'''
#2. The headlights of a car should only automatically turn
on when the daylight outside is below a certain threshold. 
If a sensor threshold is below the number 8, print 
"Headlights On"; otherwise, print "Headlights Off".
'''
daylight_value = int(input("Could you give me a number between 1 and 16 to represent the amount of daylight? "))
sensor_threshold = 8
if (daylight_value < sensor_threshold):
  print("Headlights On")
else:
  print("Headlights Off")
