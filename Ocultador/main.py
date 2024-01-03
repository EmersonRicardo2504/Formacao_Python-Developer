import ctypes

pasta = input("Digite o caminho da pasta a ser ocultada ex (C:/Area_de_trabalho/teste): ")

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

if retorno:
    print("Arquivo ocultado.")

else:
    print("Arquivo não ocultado.")
