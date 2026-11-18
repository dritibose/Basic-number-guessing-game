import time as t
print("NUMBER GUESSING GAME\n")
print("***"*20,"\n\n")

print("A random number will be decided by me\n You have to guess it correctly.")
import random
secret=random.randint(1,20)

print("Are you ready?\n")
t.sleep(2)
res=input("yes/no?= ")
if res=="no":
  print("that is what makes it fun..continuing anyways..\n")
t.sleep(2)
print("The random Number is decided.\n")
t.sleep(2)
print("would you like to choose your number of attempts? reply in yes/ no. ")
response =input()


if response == "yes":
   tries= int(input("Enter the number of tries= "))
elif response=="no":
  print("Your reply didn't match the desired result,\n As default you have 3 tries, try to make best out of it!")

else:
   print("\n As default you have 3 tries, try to make best out of it!")
   tries=3

attempt=tries

while attempt >0:
 if attempt== tries:
  print(" \n The game begins now...\n")
  t.sleep(2)
  print("The number range is 1-20, would you like to change it? reply yes/no.")
  res=input()
  if res=="yes":
   t.sleep(2)
   up=int(input("Starting from 0, what would you like to have as a upper limit? "))
   secret=random.randint(0,up)
   print(f"\nThe begins with a new limit from 0 to {up}. Give your best!")
  elif res=="no":
    print("Continuing with range 1-20\n")
  else:
    print("Your reply didn't match the desired format. Continuing with range 1-20\n")

 print("___"*20)
 guessed=int(input("Enter number = \n"))

 if guessed == secret:
  if attempt==tries:
   print("You guess it on the first try!! Remarkable. You WIN.")
   t.sleep(3)
   print("Thankyou for playing!")
   break
  else:
    o="last"
    print(f"you guessed it on the {tries-attempt if attempt-tries!=-1 else o }th try, YOU WIN ")
    t.sleep(2)
    print("Thankyou for playing!")
    break

 else:
    attempt-=1
    print("the number is wrong! Try AGAIN.\n")
    print(f"you have {attempt} attempts left, give your best guess.\n\n")

else:
 print("---"*20)
 t.sleep(2)
 print("the game has ended.")
 t.sleep(2)
 print(f"you had {tries} tries, yet you failed to guess it.\n")
 t.sleep(2)
#
 print(f'the number was {secret}, Thankyou for playing.')