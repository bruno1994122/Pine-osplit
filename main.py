from colorama import Style,Fore
import os
from pog import runp, setup





def start():
  here = os.getcwd()
  coman = input(Fore.GREEN + here + Fore.MAGENTA + "$" + Fore.RESET)
  cod = coman.split()
  if coman == "help":
    print(Fore.YELLOW + "Comandos:\n" + Fore.RESET + "help - mostra os comandos\n" + Fore.GREEN + "clear - limpa a tela\n" + "ls - mostra os arquivos\n" + "cd - muda de diretorio \n dica: você pode usar cd ... para voltar um diretorio")
    start()
  elif coman == "clear":
    os.system("clear")
    start()
  elif coman == "ls":
    neo = os.listdir()
    for item in neo:
      print(Fore.GREEN + item)
      start()
  elif cod[0] == "cd" and len(cod) > 1:
    try:
      os.chdir(cod[1])
      start()
    except FileNotFoundError:
      print(Fore.RED + "Diretorio não encontrado.")
      start()
    except NotADirectoryError:
      print(Fore.RED + "Não é um diretório")
      start()
  elif cod[0] == "cd" and len(cod) > 1:
    os.chdir("..")
  elif len(cod) == 3 and cod[0] == "pog":
    if cod[1] == "install":
      try:
        arquivo = cod[2]
        runp(arquivo)
      except FileNotFoundError:
        print(Fore.RED + "Arquivo não encontrado.")
        start()
      except Exception as e:
        print("o sistema não conseguiu executar um script")
        start()
      pass
  else:
    print(Fore.RED + "Comando Invalido")
    start()
  
print(Fore.BLUE + "bem-vindos!")
start()
  
  
  