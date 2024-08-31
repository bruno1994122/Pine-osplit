import os
from colorama import Fore

def main():
  here = os.getcwd()
  comam = input(Fore.GREEN + f"{here}" + Fore.MAGENTA + "$" + Fore.RESET)
  pass