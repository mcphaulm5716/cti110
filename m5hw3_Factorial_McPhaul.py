#M5HW3: Factorial
#CTI-110
#Maaka McPhaul
#10/13/17

number = int (input("Enter a nonnegative integer? "))

product = 1
for i in range(number):
    product = product * (i+1)

    
print(product)
