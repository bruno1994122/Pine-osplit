from colorama import Style,Fore
import os


print(Fore.BLUE + "bem-vindos!")
here = os.getcwd()
print(Fore.GREEN + here + Fore.MAGENTA + "$" + Fore.RESET)
coman = input()