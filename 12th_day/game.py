# This code is just a demo of the course

enemies = 1


def increase_enemies():
    enemies = 2
    # This is a local scope inside the function
    print(f"enemies inside function: {enemies}")


increase_enemies()  # output 2
print(f"enemies outside function: {enemies}")  # output 1 because global scope


def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# print(potion_strength) Not defined in this scope

# Global scope
player_health = 10


def drink_potion():
    # This is the way to modify a global variable inside a local scope
    global player_health
    potion_strength = 2
    print(f"Health before: {player_health}")
    # pLayer_health is available here cause is in the global scope
    player_health += potion_strength
    print(f"The potion has {potion_strength} points of strength!")
    print(f"Health after: {player_health}")


drink_potion()

# There is no such a thing like block scope in python
game_level = 3
enemies = ["Skeleton", "zombies", "Alien"]

# This won't create a block scope for the new_enemy variable, so it's accessible
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)  # 'Skeleton' because there is no block scope

# Another great idea in order to modify a global variable is to create a function that do this
my_global_number = 56


def increase_by_2(my_number):
    my_number += 2
    return my_number


print(my_global_number)
my_global_number = increase_by_2(my_global_number)
print(my_global_number)
