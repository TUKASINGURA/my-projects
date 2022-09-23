secret_word = "Richard"
guess = ""
start = 0
guess_count = 3
while guess !=secret_word:
    if start < guess_count:
     guess = input("Enter the secret_word:   ")
     start +=1
    else:
     print(f"The secret word was {secret_word}, THANK YOU")
     break
if guess==secret_word:
    print("YOU WON THE GAME")
else:
    print("out of GUESSES, you lost the game")