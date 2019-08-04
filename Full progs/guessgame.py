secret_word = "Giraffe"
guess = ""
count = 1

while guess != secret_word and count <= 3:
    guess = input("Enter the Guess")
    count+=1

if count <= 3:
    print("You Win as count is " + str(count))
else:
    print("You Lose")

