#CTI-110
#M3HW2 Software Sales
#Maaka McPhaul
#9/19/17


    
userNumberOfPackages = int( input('Please enter the number of packages purchased: ' ))
packagePrice = 99

if userNumberOfPackages < 10: discount = 0;
elif userNumberOfPackages < 20: discount = 0.10
elif userNumberOfPackages < 50: discount = 0.20
elif userNumberOfPackages < 100: discount = 0.30
else: discount = 0.40

subTotal = userNumberOfPackages * packagePrice
discountAmount = discount * subTotal
total = subTotal - discountAmount

print("\nAmount of discount: $" + format( discountAmount, ',.2f' ) + \
      "\nTotal amount: $" + format( total, ",.2f" ))
                            
