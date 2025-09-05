# worsheet 1

#question 1
# print("""Twinkle, twinkle, little star,
#     How I wonder what you are!
#         Up above the world so high,
#         Like a diamond in the sky.
# Twinkle, twinkle, little star,
#     How I wonder what you are""")

    
#question 2
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print(last_name,first_name)


# question 3
# import math
# radius = float(input("Enter the radius of the circle: "))
# area = math.pi * radius * radius
# print("Area of the circle is:", area)


# question 4
# color_list = ["Red", "Green", "White", "Black"]
# print("First color:", color_list[0])
# print("Last color:", color_list[-1])


# question 5
# n=int(input("enter a number:"))
# result=n+(n*n)+(n*n*n)
# print("value is",result)


# question 6
# values = input("Enter numbers separated by commas: ")
# print("List:", values.split(","))
# print("Tuple:", tuple(values.split(",")))



# question 7
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print("Temperature in Fahrenheit:", fahrenheit)



# question 8
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c=a
# a=b
# b=c
# print("value swapped of a and b:",a,b)



# question 9 
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(num, "is Even")
# else:
#     print(num, "is Odd")



# question 10
# year = int(input("Enter a year: "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(year, "is a Leap Year")
# else:
#     print(year, "is Not a Leap Year")



# question 11
# import math
# x1 = float(input("Enter x1: "))
# y1 = float(input("Enter y1: "))
# x2 = float(input("Enter x2: "))
# y2 = float(input("Enter y2: "))
# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# print("Euclidean distance:", distance)




# question 12
# a = int(input("Enter first angle: "))
# b = int(input("Enter second angle: "))
# c = int(input("Enter third angle: "))
# if a + b + c == 180 and a > 0 and b > 0 and c > 0:
#     print("Yes, it forms a triangle")
# else:
#     print("No, it cannot form a triangle")



# question 13
# P = float(input("Enter principal amount: "))
# r = float(input("Enter annual interest rate (in %): ")) / 100
# t = float(input("Enter time in years: "))
# n = int(input("Enter number of times interest is compounded per year: "))
# A = P * (1 + r/n)**(n*t)
# CI = A - P
# print("Compound Interest:", CI)




# question 14
# num = int(input("Enter a number: "))

# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(num, "is Not Prime")
#             break
#     else:
#         print(num, "is Prime")
# else:
#     print(num, "is Not Prime")




# question 15
# N = int(input("Enter a positive integer: "))
# sum_ofsquares = (N * (N + 1) * (2 * N + 1)) // 6
# print("Sum of squares up to", N, "is:", sum_ofsquares)





