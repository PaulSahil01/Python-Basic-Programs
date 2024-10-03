# Author of the code: SAHIL PAUL 
# Course : Introduction to Programming
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.


# Get lower and upper limits from the user
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
# Function to check if a number is prime
def prime(num):
    if num < 2:  # Numbers less than 2 are not prime
        print(f"{num} is not prime")  # Optional: print for clarity
    else:
        is_prime_flag = True  # Assume the number is prime
        for i in range(2, int(num**0.5) + 1):  # Check for factors from 2 to the square root of num
            if num % i == 0:  # If num is divisible by i, it's not prime
                is_prime_flag = False  # Set flag to False if not prime
                break  # No need to check further
        if is_prime_flag:
            print(num)  # Print the prime number if it is prime

print(f"Prime numbers between {lower} and {upper} are:")
# Iterate through the range and check for prime numbers
for number in range(lower, upper + 1):
    prime(number)  # Check if the current number is prime
