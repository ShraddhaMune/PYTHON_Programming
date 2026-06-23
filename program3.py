#to swap two numbers entered by user

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("Before swapping : ")
print("a = ",a)
print("b = ",b)

temp = a
a = b
b = temp

print("Ater swapping : ")
print("a = ",a)
print("b = ",b)