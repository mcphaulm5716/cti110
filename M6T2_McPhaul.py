#M6T2 Feet to Inches Converter
#CTI 110
#Maaka McPhaul
#10/26/17

#constant for the number of inches per foot
INCHES_PER_FOOT = 12

def main():
    # get a number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    # convert that to inches
    print(feet, 'equals', feet_to_inches(feet), 'inches.')
    
# the feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()
