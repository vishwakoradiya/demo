# p1 = 'hello'
# for i in p1:
#     print(i)

# p1 = ['dev','raj']
# for i in p1:
#     print(i)

# for i in range(101):
#     print(i)

# for i in range(5,11):
#     print(i)

# for i in range(5,11):
#     if i == 6:
#         break
#     print(i)

# for i in range(10):
#     if i == 6:
#         continue
#     print(i)

# i = 0
# while i in range(20):
#     print(i)
#     i += 1


# i = 0
# while i in range(20):
#     if i == 3:
#         break
#     print(i)
#     i += 1

#i = 0
#while i in range(20):
#    i += 1
#    if i == 3:
#        continue
#    print(i)

    #ex 1
#for i in range(1, 51):
#    print(i)

    #ex 2
#for i in range(2, 101, 2):
#    print(i)
    
    #ex 3
#for i in range(1, 11):
#    print(f"7 x {i} = {7*i}")

    #ex 4
#total = 0
#for i in range(1, 101):
#    total += i
#print(total)

    #ex 5
#p1 = 'hello'
#for i in p1:
#    print(i)

    #ex 6
#for i in range(1, 16):
#    print(i, "cube =", i**3)

    #ex 7
#for i in range(31, 101, 2):
#    print(i)

    #ex 8
#n = 5
#fact = 1
#for i in range(1, n + 1):
#    fact *= i
#print(fact)

    #ex 9
#num = 12345
#count = 0
#temp = num
#while temp > 0:
#    count += 1
#    temp //= 10
#print(count)

    #ex 11
#s = "education"
#vowels = "aeiouAEIOU"
#count = 0
#for ch in s:
#    if ch in vowels:
#        count += 1
#print(count)

    #ex 12

    #ex 13
#for i in range(1, 201):
#    if i % 3 == 0 and i % 5 == 0:
#        print(i)

    #ex 15
#for num in range(2, 201):
#    prime = True
#    for i in range(2, int(num**0.5) + 1):
#        if num % i == 0:
#            prime = False
#            break
#    if prime:
#       print(num)

    #ex 16
#num = 121
#temp = num
#rev = 0
#while temp > 0:
#    rev = rev * 10 + temp % 10
#    temp //= 10
#print("Palindrome" if num == rev else "Not Palindrome")

    #ex 17
#for i in range(1, 11):
#    for j in range(1, 11):
#        print(i*j, end="\t")

    #ex 19
#for i in range(1, 6):
#   print("*" * i)

    #ex 20
#for i in range(5, 0, -1):
#    for j in range(1, i + 1):
#        print(j)