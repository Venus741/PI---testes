from main import tentar_login

def test_login_correto():
    tentativas = [0]
    resposta = tentar_login(tentativas, "admin", 123)
    assert resposta == "Acesso liberado"

def test_login_errado_1_tentativa():
    tentativas = [0]
    resposta = tentar_login(tentativas, "user", 123)
    assert resposta == "Usuário ou senha incorretos. Restam 2 tentativas"

def test_login_errado_3_tentativas():
    tentativas = [3]
    resposta = tentar_login(tentativas, "admin", 000)
    assert resposta == "Você excedeu o número de tentativas"