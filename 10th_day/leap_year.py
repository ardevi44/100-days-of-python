# How to know if a certain number year is a leap year or not?

# Solution

def is_a_leap_year(year):
    message_true = f"Yeah, {year} is a leap year."
    message_false = f"No, {year} is not a leap year."
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(message_true)
            else:
                print(message_false)
        else:
            print(message_true)
    else:
        print(message_false)


def is_a_leap_year_2(year):
    condition_1 = (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0)
    condition_2 = (year % 4 == 0) and not (year % 100 == 0)

    if condition_1 or condition_2:
        return True
    else:
        return False


year_number = 2024

if (is_a_leap_year_2(year_number)):
    print(f"Yeah, {year_number} is a leap year.")
else:
    print(f"No, {year_number} is not a leap year.")
