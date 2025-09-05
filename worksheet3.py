# workshhet 3


# question 1
# def difference_17(n):
#     if n > 17:
#         return 2 * abs(n - 17)
#     else:
#         return 17 - n

# print(difference_17(20))  
# print(difference_17(10))  


# question 2
# def test_range(n):
#     return (100 <= n <= 1000) or (n == 2000)

# print(test_range(150))   
# print(test_range(2000))  
# print(test_range(50))    



# question 3
# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("robot"))  




# question 4
# def count_case(s):
#     counts = {"UPPER": 0, "LOWER": 0}
#     for ch in s:
#         if ch.isupper():
#             counts["UPPER"] += 1
#         elif ch.islower():
#             counts["LOWER"] += 1
#     return counts

# print(count_case("Hello Robot"))




# question 5
# def unique_list(lst):
#     return list(set(lst))

# print(unique_list([1, 2, 2, 3, 4, 4, 5]))




# question 6
# def even_numbers(lst):
#     return [x for x in lst if x % 2 == 0]

# print(even_numbers([1,2,3,4,5,6,7,8,9]))




# question 7
# def robot():
#     def move():
#         return "Robot is moving"
#     return move()

# print(robot())




# question 8
# def student(name, age, course):
#     pass
# print("Function arguments:", student.__code__.co_varnames[:student.__code__.co_argcount])




# question 9
# def move_robot(x, y, direction):
#     if direction == "up":
#         y += 1
#     elif direction == "down":
#         y -= 1
#     elif direction == "left":
#         x -= 1
#     elif direction == "right":
#         x += 1
#     return (x, y)

# print(move_robot(0, 0, "up"))      
# print(move_robot(2, 3, "left"))  




# question 10
# def classify_temperature(temp):
#     if temp < 15:
#         return "Cold"
#     elif 15 <= temp <= 30:
#         return "Moderate"
#     else:
#         return "Hot"

# print(classify_temperature(10)) 
# print(classify_temperature(20))  
# print(classify_temperature(35)) 



# question 11
# def is_goal_reached(path):
#     x, y = 0, 0
#     for move in path:
#         if move == "up":
#             y += 1
#         elif move == "down":
#             y -= 1
#         elif move == "left":
#             x -= 1
#         elif move == "right":
#             x += 1
#     return (x, y) == (2, 0)

# print(is_goal_reached(["up", "right", "right", "down"]))  
# print(is_goal_reached(["up", "right"]))                  




# question 12
# class Student:
#     def __init__(self, student_id, student_name, student_class):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.student_class = student_class

#     def display(self):
#         print("ID:", self.student_id)
#         print("Name:", self.student_name)
#         print("Class:", self.student_class)


# s1 = Student(105, "sagar", "URA302")
# s1.display()





# question 13
# class Student:
#     def __init__(self, student_id, student_name, student_class):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.student_class = student_class

#     def display(self):
#         print(f"ID: {self.student_id}, Name: {self.student_name}, Class: {self.student_class}")


# student1 = Student(105, "sagar", "URA302")
# student2 = Student(108, "udhav", "URA302")

# student1.display()
# student2.display()




# question 14
# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius * self.radius

#     def perimeter(self):
#         return 2 * math.pi * self.radius


# c = Circle(5)
# print("Area:", c.area())
# print("Perimeter:", c.perimeter())




# question 15
# class MyString:
#     def __init__(self):
#         self.text = ""

#     def get_String(self):
#         self.text = input("Enter a string: ")

#     def print_String(self):
#         print(self.text.upper())

# s = MyString()
# s.get_String()
# s.print_String()




# question 16
# class Robot:
#     def __init__(self, name, task):
#         self.name = name
#         self.task = task
#         self.battery_level = 100

#     def perform_task(self):
#         if self.battery_level >= 10:
#             print(self.name, "is performing:", self.task)
#             self.battery_level -= 10
#         else:
#             print(self.name, "has low battery! Please recharge.")

#     def recharge(self):
#         self.battery_level = 100
#         print(self.name, "is recharged to 100%")

#     def status(self):
#         print("Name:", self.name)
#         print("Task:", self.task)
#         print("Battery Level:", self.battery_level, "%")

# r1 = Robot("Robo1", "Sweeping")
# r1.perform_task()
# r1.status()
# r1.recharge()
# r1.status()












