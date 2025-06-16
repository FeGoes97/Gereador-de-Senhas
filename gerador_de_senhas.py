import random
import string

# Função para gerar senha
def gerar_senha(tamanho=12):
    # Definindo os caracteres possíveis
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gerando a senha aleatória
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    
    return senha

# Exemplo de uso
tamanho = int(input("Digite o tamanho da senha: "))
senha_gerada = gerar_senha(tamanho)
print("Senha gerada:", senha_gerada)
