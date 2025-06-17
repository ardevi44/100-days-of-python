print("""\
             ░░░░░░░
        ░░░░░░░░░░░░░░░░░
      │░░░░░░░░░░░░░░░░░░░│
      │░░░░░░░░░░░░░░░░░░░│
     ░└┐░░░░░░░░░░░░░░░░░┌┘░
     ░░└┐░░░░░░░░░░░░░░░┌┘░░
     ░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░
      ░│██████▌░░░▐██████│░
      ░│▐███▀▀░░▄░░▀▀███▌│░  
      ─┘░░░░░░░▐█▌░░░░░░░└─
      ░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░ 
        ─┘██▌░░░░░░░▐██└─
        ░░▐█─┬┬┬┬┬┬┬─█▌░░
        ░░░▀┬┼┼┼┼┼┼┼┬▀░░░
         ░░░└┴┴┴┴┴┴┴┘░░░
           ░░░░░░░░░░░
""")

choice1 = input("""
Welcome to treasure island.
Your mission is to find the treasure.

You're at a cross road. Where do you want to go?
          Type [L] for "left" or [R] "right"
          -> """).lower()
# Remember to evaluate first the case in we win.
# Is the option that the program needs to do something after.
if choice1 == "l":
    choice2 = input('''
You've come to a lake. There is an island in the middle of the lake.
          Type [W] to wait for a boat. Type [S] to swim across.
          -> ''').lower()
    if choice2 == "w":
        door = input('''
You've arrived at the island unharmed. There is a house with 3 doors.
          One red [R], one Yellow [Y] and one Blue [B]. Which color do you choose?
          -> ''').lower()
        if door == "y":
            print("""
                             _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           '.  ||:::::.-!()oo @!()@.-'_.||
           '.'-;|:.-'.&$@.& ()$%-'o.'_|U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-|U|.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_|.-'
""")
            print("Congratulations! You've Won!")
        elif door == "r":
            print("You will burn in hell. Game over")
        elif door == "b":
            print("You've been eaten by beasts. Game over")
        else:
            print("Game over")
    else:
        print("You've been attacked by a trout. Game over")

else:
    print("You've been fallen into a hole. Game Over")
