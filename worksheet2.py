# worksheet 2

# question 2
# L = [11, 12, 13, 14]

#(i) 
# L.append(50)
# L.append(60)
# print(" adding 50, 60:", L)

#(ii)
# L.remove(11)
# L.remove(13)
# print("removing 11, 13:", L)

# (iii) 
# L.sort()
# print("Ascending:", L)

# (iv) 
# L.sort(reverse=True)
# print("Descending:", L)

# (v) 
# print("finding 13 in L", 13 in L)

# (vi) 
# print("Length of L:", len(L))

# (vii) 
# print("Sum of L:", sum(L))

# (viii) 
# odd_sum = sum([x for x in L if x % 2 != 0])
# print("Sum of odd numbers:", odd_sum)

# (ix) 
# even_sum = sum([x for x in L if x % 2 == 0])
# print("Sum of even numbers:", even_sum)

# (x) 
# def is_prime(n):
#     if n < 2: return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0: return False
#     return True

# prime_sum = sum([x for x in L if is_prime(x)])
# print("Sum of prime numbers:", prime_sum)

# (xi) 
# L.clear()
# print(" clearing:", L)

# (x)
# del L




# question 2
# nums = [1, 2, 3, 4, 5]
# total = 0
# for n in nums:
#     total += n
# print("Sum:", total)




# question 3
# nums = [1, 2, 3, 4, 5]
# product = 1
# for n in nums:
#     product *= n
# print("Product:", product)



# question 4
# array = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
# print(array)




# question 5
# D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}

# (i) 
# D[8] = 8.8
# print("After adding (8:8.8):", D)

# (ii) 
# D.pop(2, None)
# print("After removing key 2:", D)

# (iii) 
# print("Is key 6 present", 6 in D)

# (iv) 
# print("Number of elements:", len(D))

# (v) 
# print("Sum of values:", sum(D.values()))

# (vi) U
# D[3] = 7.1
# print("updating key 3:", D)

# (vii)
# D.clear()
# print("After clearing:", D)




# question 6
# S1 = {10, 20, 30, 40, 50, 60}
# S2 = {40, 50, 60, 70, 80, 90}

# (i)
# S1.update([55, 66])
# print("After adding 55, 66:", S1)

# (ii) 
# S1.discard(10)
# S1.discard(30)
# print("After removing 10, 30:", S1)

# (iii)
# print("Is 40 in S1", 40 in S1)

# (iv) 
# print("Union:", S1 | S2)

# (v) 
# print("Intersection:", S1 & S2)

# (vi) 
# print("Difference (S1 - S2):", S1 - S2)



# question 7
# (i)
# import random
# import string
# for _ in range(100):
#     length = random.randint(6, 8)  # random length between 6 and 8
#     rand_str = ''.join(random.choice(string.ascii_letters) for _ in range(length))
#     print(rand_str)


# (ii)
# def is_prime(n):
#     if n < 2: return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0: return False
#     return True
# primes = [n for n in range(600, 801) if is_prime(n)]
# print("Primes between 600 and 800:", primes)


# (iii)
# nums = [n for n in range(100, 1001) if n % 7 == 0 and n % 9 == 0]
# print("Divisible by 7 and 9:", nums)




# question 8
# exam_st_date = (11, 12, 2025)
# print("The examination will start from: %i / %i / %i" % exam_st_date)



# question 9
# numbers = [10, 23, 45, 66, 75, 90, 101]
# for n in numbers:
#     if n % 5 == 0:
#         print(n)



# question 10
# num = 37
# is_even = (num % 2 == 0)
# if is_even:
#     print(num, "is Even")
# else:
#     print(num, "is Odd")




# question 11
# text = "Emma is a good girl. Emma likes Python. Emma is learning AI."
# count = text.count("Emma")
# print("Number of times 'Emma' appears:", count)



# question 12
# list1 = [10, 21, 32, 43, 54, 65]
# list2 = [11, 22, 33, 44, 55, 66]
# new_list = [x for x in list1 if x % 2 != 0] + [y for y in list2 if y % 2 == 0]
# print("New list:", new_list)




# question 13
# positions = [(2, 3), (4, 5), (6, 7), (7, 8)]
# even_positions = [pos for pos in positions if pos[0] % 2 == 0]
# print("Positions with even x:", even_positions)



# question 14
# sensor_data = {1: 2.3, 2: 4.5, 3: 1.8, 4: 3.6}
# high_sensors = [sid for sid, val in sensor_data.items() if val > 3.0]
# print("Sensor IDs with readings > 3.0:", high_sensors)




# question 15
# commands_received = {"MOVE", "TURN_LEFT", "TURN_RIGHT", "STOP"}
# commands_executed = {"MOVE", "TURN_LEFT", "STOP"}
# not_executed = commands_received - commands_executed
# print("Commands not executed:", not_executed)

