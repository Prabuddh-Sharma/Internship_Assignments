
#Assignment 3.1

def cal():
    
    print("Basic Math Operations ->")

    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))

    print(f"\nAddition: {n1} + {n2} = {n1 + n2}")
    print(f"Subtraction: {n1} - {n2} = {n1 - n2}")
    print(f"Multiplication: {n1} * {n2} = {n1 * n2}")

    if n2 == 0:
        print(f"Division: {n1} / {n2} Error")
    else:
        print(f"Division: {n1} / {n2} = {n1 / n2}")

# TO EXECUTE ->
#cal()

#Assignment 3.2

def Palindrome(x):
    
    if x < 0:
        return False

    s = str(x)

    r_str = ""
    for char in s:
        r_str = char + r_str

    return s == r_str

print(f"FOR 121  {Palindrome(121)}")
print(f"FOR -121 {Palindrome(-121)}")
print(f"FOR 10 {Palindrome(10)}")
print(f"FOR 12321 {Palindrome(12321)}")
print(f"FOR 0 {Palindrome(0)}")