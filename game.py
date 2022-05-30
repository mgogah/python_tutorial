secret_answer = "aden"
answer = ""
count = 0
limit = 3
lose = False
while secret_answer != answer and not lose:
    if count < limit:
       print("You have: " +str(limit - count) + " / " + str(limit))
       answer = input("Write Capital of YEMEN: ")
       count +=1
    else:
        lose = True

if lose:
    print("You lose :( ")
else:
    print("You WIN :)")

