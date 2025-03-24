# TELA DE LOGIN
acesso = False

while acesso == False:

    tentativas = 0
    usuario = input("Usuário: ")
    senha = int(input("Senha: "))

    if usuario != "admin" and senha != 123:
        
        tentativas += 1
        tentativas_restantes = 3 - tentativas

        print(f"Usuário ou senha incorretos. Restam {tentativas_restantes} tentativas")

        if tentativas > 3:
            print("Você excedeu o número de tentatívas. Por favor, tente mais tarde")
            break

    else:
        print("Acesso liberado.")
        acesso = True

print("Seja bem-vindo!")