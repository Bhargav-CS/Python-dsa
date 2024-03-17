# 3. Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

max_num = int(input("Enter a number: "))
odd_numbers = [x for x in range(1, max_num) if x % 2 != 0]
print(odd_numbers)