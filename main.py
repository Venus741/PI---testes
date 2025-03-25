# ADAPTAÇÃO PARA TESTE

def verificar_login(usuario: str, senha: int) -> bool:
    return usuario == "admin" and senha == 123

def tentar_login(tentativas: list, usuario: str, senha: int) -> str:
    if verificar_login(usuario, senha):
        return "Acesso liberado"
    
    else:
        tentativas[0] += 1
        if tentativas[0] > 2:
            return "Você excedeu o número de tentativas"
        
        else:
            resto = 3 - tentativas[0]
            return f"Usuário ou senha incorretos. Restam {resto} tentativas"