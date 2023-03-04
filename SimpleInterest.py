# taking input values from user
principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time in years: "))
rate = float(input("Enter the rate of interest: "))

# calculating the simple interest
simple_interest = (principal * time * rate) / 100

# displaying the calculated simple interest
print("Simple interest = ", simple_interest)
