#reteaching myself the syntax of python

print("Welcome to my quiz!")

playing = input("Do you want to play? ")
print(playing)

answersCorrect = 0
answersFalse = 0

if(playing!="yes"):
    quit();
else:
    print("Ok let's play nerd")

    #q1
    answer = input("what does CPU stand for? ")
    if answer != "central processing unit":
        answersFalse+=1
    else:
        answersCorrect+=1
    
    #q2
    answer2 = input("who never dies? ")
    if answer2 == "technoblade":
        answersCorrect+=1
    else:
        answersFalse+=1

    #finish testing
    print("\n\nThe quiz is over! Here are your scores: ")
    score = answersCorrect/(answersCorrect + answersFalse)*100
    print("Missed questions: ", answersFalse)
    print("Percentage Score: ", score,"/100")
    print("\nThanks for playing!")



