p= float(input("Enter the Principal Amount: "))
r= float(input("Enter the Interest Rate :"))
t= int(input("Enter the no. of years :"))
#Convert rate from percent to decimal
r = r / 100
# Formula of Compound Interest 
A = p * (1 + r) ** t
# Formula to Calulate Interest
interest= A-p
print("Final amount after", t, "years is:", A)
print("Interest earned:", interest)
