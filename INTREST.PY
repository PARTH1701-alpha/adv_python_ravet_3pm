# This is an program to calculate simple inrest


def simple_intrest(p, n, r):
    """This function calulates  simple interest and amount"""
    i = (p * n * r) / 100
    a = p + i
    return i, a


# Take p, n, r as input from user
p = float(input("Please enter Principal in INR : "))
n = float(input("Please enter number of years :"))
r = float(input("Please enter rate of intrest in %p.a. :"))

# Call simple intrest function
i, a = simple_intrest(p, n, r)

# Show  the function result
print(f"Simple Intrest :{i:.2f} INR")
print(f"Amount : {a:.2f}INR")
