    #ex 1
# def sum_tuple(numbers: tuple[int, ...]):
#     return sum(numbers)
# t = (1, 2, 3, 4)
# print(sum_tuple(t))  

    #ex 2
# data = {
#     'a' : [10,20,30],
#     'b' : [40,50]
# }

# total = sum(sum(values) for values in data.values() )
# print(total)

    #ex 3


    #ex 4
# def separate_even_odd(numbers):
#     evens = []
#     odds = []
#     for num in numbers:
#         if num % 2 == 0:
#             evens.append(num)
#         else:
#             odds.append(num)
#     return evens, odds

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# even_list, odd_list = separate_even_odd(nums)
# print("Even:", even_list)
# print("Odd:", odd_list)

    #ex 5
# def reverse_list(lst):
#     reversed_list = []
#     for i in range(len(lst) - 1, -1, -1):
#         reversed_list.append(lst[i])
#     return reversed_list

# numbers = [1, 2, 3, 4, 5]
# print(reverse_list(numbers))

    #ex 6
# keys = ['apple', 'banana', 'cherry']
# values = [1, 2, 3]
# my_dict = dict(zip(keys, values))
# print(my_dict)

    #ex 7
# numbers = [12, 35, 1, 10, 34, 1]

# def second_largest(lst):
#     unique_values = list(set(lst))  
#     if len(unique_values) < 2:
#         return None  
#     unique_values.sort()
#     return unique_values[-2]

# result = second_largest(numbers)
# print(result)

    #ex 8
# numbers = {3, 7, 10, 15, 2, 20, 8}
# numbers = {n for n in numbers if n >= 10}
# print(numbers)

    #ex 9
# def all_unique(lst):
#     return len(lst) == len(set(lst))
# numbers = [1, 2, 3, 4, 5]
# print(all_unique(numbers))  

    #ex 10
# employees = {
#     "bhumi": 50000,
#     "rina": 75000,
#     "jay": 68000
# }

# highest_paid = max(employees, key=employees.get)

# print(highest_paid, employees[highest_paid])


    #ex 11
# def get_primes(numbers):
#     primes = []
#     for num in numbers:
#         if num < 2:
#             continue     
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#     return primes

# nums = [1, 2, 3, 4, 5, 10, 11, 13, 15]
# print(get_primes(nums))

    #ex 12
# numbers = (1, 2, 3, 4, 5, 6, 7, 8)
# even_count = 0
# odd_count = 0

# for n in numbers:
#     if n % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Even:", even_count)
# print("Odd:", odd_count)


        #ex 13
# def common_elements(set1, set2):
#     return set1 & set2
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(common_elements(a, b))

    #ex 14
# students = {
#     "Aena": 85,
#     "jay": 67,
#     "Charmi": 72,
#     "Dev": 60
# }
# for student, marks in students.items():
#     if marks > 70:
#         print(student, ":", marks)

        #ex 15
# def long_strings(strings):
#     result = []
#     for s in strings:
#         if len(s) > 5:
#             result.append(s)
#     return result
# words = ["apple", "banana", "kiwi", "strawberry", "pear"]
# print(long_strings(words))

    #ex 16
# people = [("vishwa", 20), ("ujjwal", 17), ("meet", 25), ("man", 15)]

# names_above_18 = []

# for name, age in people:
#     if age > 18:
#         names_above_18.append(name)

# print(names_above_18)

    #ex 17
# def max_min(s):
#     return max(s), min(s)
# numbers = {10, 25, 5, 30, 15}
# maximum, minimum = max_min(numbers)

# print("Maximum:", maximum)
# print("Minimum:", minimum)

    #ex 18
# products = {
#     "apple": 100,
#     "banana": 50,
#     "orange": 80
# }

# for product in products:
#     products[product] = products[product] * 1.10  
# print(products)

    #ex 19
# def palindrome(number):
#     num_str = str(number)
#     return num_str == num_str[::-1]
# print(palindrome(121))   
# print(palindrome(123))   
# print(palindrome(1221))  

    #ex 20
# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique_numbers = list(set(numbers))
# print(unique_numbers)
