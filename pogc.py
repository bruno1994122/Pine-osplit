import os
from colorama import Fore,Style

def menu():
  here = os.getcwd()
  codf = input(Style.BRIGHT + "Menu do pogc!\ndigite help para ajuda\n" + Style.RESET_ALL + Fore.GREEN + here + Fore.MAGENTA + "$ " + Fore.RESET)
  comap = codf.split()
  if codf == "exitpog":
    os.system("python main.py")
    pass
  elif codf == "help":
    print("exitpog para voltar ao menu\nexecute {arquivo} para executar um arquivo python")
    menu()
  elif comap[0] == "execute" and len(comap) > 1: 
    print("executando...")
    os.system(f"python {comap[1]}")
    pass
  else:
    print("error at command line ???\n invalid command")

menu()