# Guessing game program behavior

1. You give a welcome for the user first, something like ...

```txt
Welcome to the Number Guessing Game!  
I'm thinking of a number between 1 and 100
```

2. Then you have to give a difficulty option for the user. He has to select between
easy or hard. In base to this option. You will give a number of attempts. 10 in
easy mode and 5 for the hard one.
The legend has to say...

```txt
Choose a difficulty. Type 'easy' or 'hard':
```

And wait for the prompt. Remember you have to ask again if any of two words doesn't match.

3. Show the number of attempts remaining

```txt
You have `attempts remaining` remaining to guess the number.
```

This value is updated after each guess.

4. Ask for the guessed number

```txt
Make a guess:
```

5. **Show if the number is to high or to low**

- If the number guessed rebase the secret number you show `To high`.
- If the number guessed is below of the secret number you say `Too low`.

Remember also any time the number is not the secret number you show the number of attempts remaining, and the label to make a guess again.

```txt
# Example 1
Make a guess: 3
Too low.
Guess again.

# Example 2
Make a guess: 100
Too high
Guess again
```

7. If the guess corresponds to the secret number you Win. So you have to show ...
```
You got it! The answer was 14.
```
And the game just ends.