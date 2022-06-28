import random
print("Winning Rules for the rock paper scissors are as follows: \n"
      + "rock vs paper->paper wins\n"
      + "rock vs scissors->rock wins\n"
      + "paper vs scissors->scissors wins\n")


class Draw:
    pass


while True:
    print("Enter choice \n 1 for rock,\n 2 for paper,\n 3 for scissors.\n")
#     take input from the user
    choice =int(input("User turn: "))
    while choice >3 or choice < 1:
        choice=int(input("Enter valid input: "))
    if choice==1:
        choice_name='rock'
    elif choice==2:
        choice_name='paper'
    else:
        choice_name='scissors'
    print('user choice: '+choice_name)
    print("\n it is now computer's turn......")

#     OR is the short-circuit operator
#      if any of the condition is true then it returns true value
#      looping until the user enters invalid input
#     initialize choice variable corresponding to the choice value
#     print user choice
    comp_choice = random.randint(1 , 3)
    while comp_choice == choice:
        comp_choice=random.randint(1 , 3)
    if comp_choice == 1:
        comp_choice_name ='rock'
    elif comp_choice == 2:
        comp_choice_name ='paper'
    else:
        comp_choice_name ='scissors'
    print("Computer choice is: "+comp_choice_name)
    print(choice_name + "Vs" + comp_choice_name)
#     we need to check for a draw
    if choice == comp_choice:
        print("Draw=>", end="")
        result = Draw
#   condition for winning
    if ((choice==1 and comp_choice==2)or
        (choice==2 and comp_choice==1)):
        print('paper wins=>',end='')
        result = 'paper'

    elif((choice==3 and comp_choice==1)or
        (choice == 1 and comp_choice == 3)):
        print('rock wins=>',end='')
        result = 'rock'

    else:
        print('scissors wins =>',end='')
        result ='scissors'

    if result == Draw:
        print("<== it's a tie ==>")
    if result== choice_name:
        print("<== user wins==>")
    else:
        print("<== computer wins==>")
    print("Do you want to play again? (Y/N)")
    ans=input().lower
#     whether it's n or N then it's the same
    if ans == 'n':
        break

#
#    After we come out of the while loop
#    we print thanks for playing
print("\n Thanks for playing")



