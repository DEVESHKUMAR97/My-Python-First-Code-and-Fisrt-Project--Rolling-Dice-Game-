import random
import os

count1 = 0
count2 = 0
count3 = 0
game = 1
while True:
 value1 = random.randint(1,6)
 value2 = random.randint(1,6)

 list = [value1,value2]
 flag = 1

 print("          Dice Rolling Game !      Game Number  : " + str(game))
 print()

 for i in list:
    if flag == 1:
        print("   Your Dice :")
    else:
        print("   Computer Dice :")
    if i == 1:
        print("""
                 -----------------
                 |               |
                 |               |
                 |       *       |
                 |               |
                 |               |
                 -----------------""")
    elif i == 2:
        print("""
                 -----------------
                 |               |
                 |               |
                 |  *        *   |
                 |               |
                 |               |
                 -----------------""")
    elif i == 3:
        print("""
                 -----------------
                 |               |
                 |               |
                 |   *   *   *   |
                 |               |
                 |               |
                 -----------------""")
    elif i == 4:
        print("""
                 -----------------
                 |               |
                 |   *       *   |
                 |               |
                 |   *       *   |
                 |               |
                 -----------------""")
    elif i == 5:
        print("""
                 -----------------
                 |               |
                 |   *       *   |
                 |       *       |
                 |   *       *   |
                 |               |
                 -----------------""")
    elif i == 6:
        print("""
                 -----------------
                 |               |
                 |   *   *   *   |
                 |               |
                 |   *   *   *   |
                 |               |
                 -----------------""")
    if flag == 1:
        print("""
             *************************
             *************************\n""")
        flag =2

 print("\n\n   You got " + str(value1) + " and Computer got " + str(value2) + ".")
 if value1 > value2:
    count1+=1
    print("   So, You Won !")
 elif value1 < value2:
    count2+=1
    print("   So, You Loss !")
 else:
    count3+=1
    print("   So, It is Draw !")

 print("\n\n   You have won " + str(count1) + " games.")
 print("   Computer have won " + str(count2) + " games.")
 print("   " + str(count3) + " games remains drawn.")


 while True:
   var = input("\n\n   Do You want to play one more game. <y/n>:")
   if var != 'y' and var != 'Y' and var != 'n' and var != 'N':
    print("Invalid choice! choose again.")
   else:
       break
 if var == 'n' or var == 'N':
     break
 else:
     game+=1
     os.system('cls')


print("\n\n   Okh Bye Bye! See you again.")

# Created By : Devesh Kumar
# If you like give it a thumbs up.
