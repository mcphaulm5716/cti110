#M6T1 Kilometer Converter
#CTI 110
#Maaka McPhaul
#10/26/17

def main ():
    km_in=float(input("Enter kilometers: "))
    show_miles(km_in)

def show_miles(km):
    miles = km * 0.6214
    print(km, 'kilometers is equal to', miles, "miles")


main()
