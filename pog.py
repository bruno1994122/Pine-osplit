import os

# Caminho do script Python a ser executado
def runp(filep):
    os.system(f"python {filep}")
class setup:
    def setupog():
        if not os.path.exists("pogins"):
            os.makedirs("pogins")
    pass