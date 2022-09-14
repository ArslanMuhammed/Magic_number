import random

min_number   = 1
max_number   = 10
magic_number = random.randint(min_number, max_number)
life         = 4
score        = life 

def search_magical_number(min, max):

#   ----- The question -----       
    answer_int = 0
    while answer_int == 0:
        answer_str = input("What is the magic number between " + str(min) + " and " + str(max) + " ? ")

#   ----- The cases of errors -----         
        try:
            answer_int = int(answer_str)
        except:
            print("You must put an int and not str. Try again")
        else:
            if answer_int < min or answer_int > max:
                print("The answer must be between", min, "and", str(max) + ". Try again.")

    return answer_int



for i in range(life):
    print()
    print(f"You are {score}/{life} lifes:")
    answer = search_magical_number(min_number, max_number)
    if answer == magic_number:
        print("True answer!")
        break
    elif answer > magic_number:
        print("The answer is smaller!")
        score -= 1
    else:
        print("The magical number is bigger!")
        score -= 1

print()

if   score == 4:
    print("Cheer. The score is perfect")
elif score >= 2:
    print("The score is correct!")
else:
    print("The score is bad")
