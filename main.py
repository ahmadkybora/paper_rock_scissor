import random

options = ["s", "k", "q"]
user_choice = input("lotfan az bein mavared zir yeki ra entekhab konid")
user_score = 0
pc_score = 0
run = True

while run:
    pc_choice = random.choice(options)
    print(f"pc choice: {pc_choice}")

    if user_choice == pc_choice:
        print("ye bar dige")
    elif user_choice == "s":
        if pc_choice == "k":
            pc_score += 1
            print("pc win")
        else:
            user_score += 1
            print("user win")
    elif user_choice == "k":
        if pc_choice == "q":
            pc_score += 1
            print("pc win")
        else:
            user_score += 1
            print("user win")
    elif user_choice == "q":
        if pc_choice == "s":
            pc_score += 1
            print("pc win")
        else:
            user_score += 1
            print("user win")

    print(f"user: {user_score} -pc: {pc_score} - berim daste badi")
    if user_score == 3 or pc_score == 3:
        if user_score == 3:
            print("user win")
        else:
            print("user win")

        break