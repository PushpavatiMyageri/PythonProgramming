#5. python program for compound interest
p = float(input("enter the principle value : "))
t = float(input("enter the term  : "))
r = float(input("enter the rate of interest : "))
compound_interest = p*(pow((1+r/100),t))
print(compound_interest)
