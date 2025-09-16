import os # Biblioteca importada para limpar o terminal

plantio_berinjela = [] # Formato: Retângulo [comprimento, largura, area_total]
plantio_cana = [] # Formato: Triangulo [base, altura, area_total

# Aqui usamos limpar terminal para melhor visualização do que está acontecendo
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

