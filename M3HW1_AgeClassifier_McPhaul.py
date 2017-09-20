#CTI-110
#M3HW1 Age Classifier
#Maaka McPhaul
#9/18/2017

def main():

    userAge = int( input( "Please enter your age: " ))

    if userAge <= 1:
        print( "\nYou are an infant" )
    elif userAge < 13:
        print( "\nYour are an child" )
    elif userAge < 20:
        print("\nYou are an teenager"  )
    elif userAge >= 20:
        print( "\nYou are an adult" )


main()
