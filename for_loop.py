# For loop demo

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)

# Highest score
# -------------

student_scores = [124, 165, 173, 280, 189, 169,
                  346, 520, 280, 146]  # The highest is 520

# This is the built in function sum()
total_score = sum(student_scores)
print(total_score)

highest = 0
for score in student_scores:
    if score > highest:
        highest = score

print(highest)

# Gauss problem demo
# ---------------------

total_sum = 0
# Remember in a range the second argument is not inclusive so you have to
# add 1
for number in range(1, 100 + 1):
    total_sum += number

print(total_sum)

# FizzBuzz challenge
# ------------------

for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
