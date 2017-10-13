#M5HW1 Distant Traveled
#CTI-110
#Maaka McPhaul
#10/13/17

vehiclespeed = float(input("What is the speed of the vehicles in mph: " ) )
timetraveled = int(input("How many hours has it traveled?: " ) )


print( "Hour","\tDistance Traveled" )
for currenthour in range(1, timetraveled + 1):
    distancetraveled = vehiclespeed * currenthour
    print( currenthour,"\t",distancetraveled)
