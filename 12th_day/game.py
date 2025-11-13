# This code is just a demo of the course

enemies = 1


def increase_enemies():
    enemies = 2
    # This is a local scope inside the function
    print(f"enemies inside function: {enemies}")


increase_enemies()  # output 2
# And this below is a global scope
print(f"enemies outside function: {enemies}")  # output 1


# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)


# drink_potion()
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

print(new_enemy)
