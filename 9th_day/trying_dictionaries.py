programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over",
    "Loop": "The action of doing something over and over again",
    # Some other keys
    123: "Some other definition"
}

print(programming_dictionary["Function"])
print(programming_dictionary[123])

# Resign one of the values
programming_dictionary[123] = "One hundred and twenty three"
print(programming_dictionary)

# An empty dictionary (no values)
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Adding new values
programming_dictionary["definition"] = "Just a description of something"
print(programming_dictionary["definition"])

# Loop through dictionaries
for something in programming_dictionary:
    print(something)


for key in programming_dictionary:
    print(f"{key}: {programming_dictionary[key]}")


# Nested List in Dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Stuttgart", "Leipzig", "Dortmund"],
        "total_visits": 5
    }
}

# Print Lille

france = travel_log["France"]
print(france["cities_visited"])
print(travel_log["France"]["cities_visited"][2])

# quiz test
starting_dictionary = {
    "a": 9,
    "b": 8,
}

final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

final_dictionary = starting_dictionary["c"] = 7


print(final_dictionary)

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# dict[1] = 4
print(dict[1])
