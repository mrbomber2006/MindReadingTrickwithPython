from colorama import Fore
from time import *


print(Fore.LIGHTWHITE_EX +
      "I can read your mind!\nany number you choose is going to be 8\nlets start!")
print(Fore.BLUE + "*" * 12)
old_number = int(input(Fore.LIGHTYELLOW_EX +
                 "choose any number you think about: "))

# answer = old_number
answer = old_number * 2
sleep(2)
print(Fore.LIGHTWHITE_EX + f"The" + Fore.CYAN + " number " + Fore.LIGHTWHITE_EX + "is multiplied by two Your" +
      Fore.CYAN + " answer " + Fore.LIGHTWHITE_EX + "is : " + Fore.LIGHTRED_EX + f"{answer} ")
print(Fore.BLUE + "*" * 12)
answer += 8
sleep(3)
print(Fore.LIGHTWHITE_EX + f"Your" + Fore.CYAN + " answer " + Fore.LIGHTWHITE_EX +
      " is multiplied by eight :" + Fore.LIGHTRED_EX + f"{answer} ")
answer += old_number
sleep(3)
print(Fore.BLUE + "*" * 12)
print(Fore.LIGHTWHITE_EX +
      f"Add your" + Fore.CYAN + " answer " + Fore.LIGHTWHITE_EX + " with the first number you entered: " + Fore.LIGHTRED_EX + f"{answer} ")
answer -= 2
sleep(3)
print(Fore.BLUE + "*" * 12)
print(Fore.LIGHTWHITE_EX + f"Subtract the" + Fore.CYAN + " answer " +
      Fore.LIGHTWHITE_EX + " by two: " + Fore.LIGHTRED_EX + f"{answer} ")
answer //= 3
sleep(3)
print(Fore.BLUE + "*" * 12)
print(Fore.LIGHTWHITE_EX + f"Divide the" + Fore.CYAN + " answer " +
      Fore.LIGHTWHITE_EX + " by three: " + Fore.LIGHTRED_EX + f"{answer} ")
answer -= old_number
sleep(3)
print(Fore.BLUE + "*" * 12)
print(Fore.LIGHTWHITE_EX +
      f"Subtract the first" + Fore.CYAN + " number " + Fore.LIGHTWHITE_EX + " you choose from the" + Fore.CYAN + " answer " + Fore.LIGHTWHITE_EX + ": " + Fore.LIGHTRED_EX + f"{answer} ")
answer *= 4
sleep(3)
print(Fore.BLUE + "*" * 12)
print(Fore.LIGHTWHITE_EX + f"Multiply the" + Fore.CYAN + " answer " +
      Fore.LIGHTWHITE_EX + " by 4: " + Fore.LIGHTRED_EX + f"{answer} ")
print(Fore.BLUE + "*" * 12)
sleep(2)
print(Fore.LIGHTWHITE_EX + f"see? The" + Fore.CYAN + " answer " +
      Fore.LIGHTWHITE_EX + " is " + Fore.LIGHTRED_EX + f"{answer} ")
