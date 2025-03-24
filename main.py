# TELA DE LOGIN
acesso = False
tentativas = 0

while acesso == False:

    usuario = input("Usuário: ")
    senha = int(input("Senha: "))

    if usuario != "admin" and senha != 123:

        tentativas += 1
        resto = 3 - tentativas
        print("Usuário ou senha incorretos.")

        if tentativas > 2:
            print("Você excedeu o número de tentatívas. Por favor, tente mais tarde")
            break

        print(f"Restam {resto} tentatívas")

    else:
        print("Acesso liberado.")
        acesso = True

print("Seja bem-vindo!")