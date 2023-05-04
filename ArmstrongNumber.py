n = int(input())
# Hint:
# We can use list comprehension and map function to solve this problem
# Step 1: Think of a way to extract the individual digits from a number.
revString = str(n)[::-1]
lst1 = [int(x) ** 3 for x in revString]
lstSum = sum(lst1)
if lstSum == n:
    print("True")
else:
    print("False")
# The str(n) function converts the number(n) to string. The string is an iterable object, a loop can be used to extract individual digits.

# Step 2: Calculate the sum of powers of individual digits of the number.
# Then convert the individual digits back to integers. Then you can use the map() to find the sum of powers of all digits stored in int

# Step 3: Compare the sum of cubes to the original number itself. If the number is the same as the sum of powers, then the number n is an Armstrong number else it is not.
