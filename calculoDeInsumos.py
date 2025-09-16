import os
import csv

# Vetores principais para dados de plantio (armazenam os últimos dados inseridos)
plantio_berinjela = [] # Formato: Retângulo [comprimento, largura, area_total]
plantio_cana = [] # Formato: Triangulo [base, altura, area_total]

# Listas apenas para armazenar todas as áreas para análise estatística
areas_da_berinjela = []
areas_da_cana = []

# Aqui usamos limpar terminal para melhor visualização do que está acontecendo
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Nesta etapa calculamos a area da berinjela levanto em conta que é um Retângulo:
def calcular_area_berinjela():
    while True:
        try:
            comprimento = float(input("Insira em metros o comprimento da area que você pretende calcular da berinjela:"))
            largura = float(input("Insira em metros a largura da area que você pretende calcular da berinjela:"))
            area = comprimento * largura
            print(f"Área calculada: {area:.2f} m²")
            return [comprimento, largura, area]
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# Nesta etapa calculamos a area da cana levanto em conta que é um triangulo:
def calcular_area_cana():
    while True:
        try:
            base = float(input("Insira em metros a base da area que você pretende calcular da cana: "))
            altura = float(input("Insira em metros a altura da area que você pretende calcular da cana:"))
            area = (base * altura) / 2
            print(f"Área calculada: {area:.2f} m²")
            return [base, altura, area]
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def calcular_manejo_insumos():
    print("####### Cálculo de Manejo de Insumos #######")
    # uso lower para poder facilitar erros de digitação do usuario
    cultura = input("Digite a cultura (Berinjela ou Cana): ").lower()
    
    if cultura == 'berinjela':
        if not plantio_berinjela:
            print("Dados de plantio de Berinjela não encontrados. Por favor, insira os dados primeiro.")
            return
        # Aqui seleciona o terceiro item do vetor "berinjela"
        area = plantio_berinjela[2]
    elif cultura == 'cana':
        if not plantio_cana:
            print("Dados de plantio de Cana não encontrados. Por favor, insira os dados primeiro.")
            return
    # Aqui seleciona o terceiro item do vetor "cana"
        area = plantio_cana[2]
    else:
        print("Cultura inválida. Escolha 'Berinjela' ou 'Cana'.")
        return

    try:
        insumo_litro_m2 = float(input("Digite a quantidade de insumo por metro quadrado (em Litros/m²): "))
        ruas_lavoura = int(input("Digite o número de ruas na lavoura: "))
        
        # Fórmula simplificada: total de insumo = área * insumo por m2
        litros_necessarios = area * insumo_litro_m2
        
        print(f"\nPara a área de {area:.2f} m² com a quantidade de ruas {ruas_lavoura}:")
        print(f"Serão usados {litros_necessarios:.2f} litros de insumo.")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números.")

# Aqui iremos manipular a entrada de dados do usuario e também armazenar as áreas
def entrada_dados():
    print("\n##### Entrada de Dados #######")
    cultura = input("Digite a cultura para entrada de dados (Berinjela ou Cana): ").lower()
    
    if cultura == 'berinjela':
        limpar_tela()
        print("Entrada de dados para Berinjela.")
        novos_dados = calcular_area_berinjela()
        if novos_dados:
            plantio_berinjela.clear()
            plantio_berinjela.extend(novos_dados)
            areas_da_berinjela.append(novos_dados[2]) # Armazena a área para análise
            print("Dados de Berinjela inseridos com sucesso!")
    elif cultura == 'cana':
        limpar_tela()
        print("Entrada de dados para Cana.")
        novos_dados = calcular_area_cana()
        if novos_dados:
            plantio_cana.clear()
            plantio_cana.extend(novos_dados)
            areas_da_cana.append(novos_dados[2]) # Armazena a área para análise
            print("Dados de Cana inseridos com sucesso!")
    else:
        print("Cultura inválida. Escolha 'Berinjela' ou 'Cana'.")

# Aqui mostra os dados no terminal, ele mostra de acordo com os vetores
def saida_dados():
    limpar_tela()
    print("\n#### Analise de dados ###")
    print("\nDados do último plantio de Berinjela:")
    if plantio_berinjela:
        print(f"  Comprimento: {plantio_berinjela[0]:.2f} m")
        print(f"  Largura: {plantio_berinjela[1]:.2f} m")
        print(f"  Área Total: {plantio_berinjela[2]:.2f} m²")
    else:
        print("  Nenhum dado de Berinjela disponível.")

    print("\nDados do último plantio de Cana:")
    if plantio_cana:
        print(f"  Base: {plantio_cana[0]:.2f} m")
        print(f"  Altura: {plantio_cana[1]:.2f} m")
        print(f"  Área Total: {plantio_cana[2]:.2f} m²")
    else:
        print("  Nenhum dado de Cana disponível.")
    
    print("\n--- Áreas Salvas para Análise Estatística ---")
    print(f"Áreas de Berinjela: {areas_da_berinjela}")
    print(f"Áreas de Cana: {areas_da_cana}")
    if not areas_da_berinjela and not areas_da_cana:
        print("Nenhuma área salva ainda.")

def salvar_areas_para_analise():
    """Salva todas as áreas de Berinjela e Cana em um arquivo CSV."""
    try:
        with open('gitProjeto\\areas_plantio.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(['cultura', 'area_m2'])
            for area in areas_da_berinjela:
                writer.writerow(['berinjela', area])
            for area in areas_da_cana:
                writer.writerow(['cana', area])
        
        print("\nDados de áreas salvos com sucesso no arquivo 'areas_plantio.csv'!")
    except Exception as e:
        print(f"\nErro ao salvar o arquivo: {e}")

# Atualiza dados de acordo com as posições citadas em cada vetor
def atualizar_dados():
    print("\n###### Atualização de Dados ####")
    cultura = input("Digite a cultura para atualizar (Berinjela ou Cana): ").lower()
    
    if cultura == 'berinjela':
        dados = plantio_berinjela
        nomes = ['Comprimento', 'Largura', 'Área Total']
    elif cultura == 'cana':
        dados = plantio_cana
        nomes = ['Base', 'Altura', 'Área Total']
    else:
        print("Cultura inválida.")
        return

    if not dados:
        print("Nenhum dado para atualizar.")
        return
        
    for i, nome in enumerate(nomes):
        print(f"{i}: {nome} - Valor atual: {dados[i]:.2f}")
    
    try:
        posicao = int(input("Digite a posição (0, 1 ou 2) do dado a ser atualizado: "))
        if 0 <= posicao < len(dados):
            novo_valor = float(input(f"Digite o novo valor para '{nomes[posicao]}': "))
            dados[posicao] = novo_valor
            print("Dado atualizado com sucesso!")
        else:
            print("Posição inválida.")
    except (ValueError, IndexError):
        print("Entrada inválida. Digite um número para a posição.")

# Aqui deletamos todos os dados de uma cultura especifica
def deletar_dados():
    print("\n##### Deleção de Dados #####")
    cultura = input("Digite a cultura para deletar os dados (Berinjela ou Cana) ou digite AREAS para deletar as areas guardadas no sistema: ").lower()
    
    if cultura == 'berinjela':
        if plantio_berinjela:
            plantio_berinjela.clear()
            print("Dados de Berinjela deletados com sucesso!")
        else:
            print("Não há dados de Berinjela para deletar.")
    elif cultura == 'cana':
        if plantio_cana:
            plantio_cana.clear()
            print("Dados de Cana deletados com sucesso!")
        else:
            print("Não há dados de Cana para deletar.")
    elif cultura == 'areas':
        areas_da_berinjela.clear()
        areas_da_cana.clear()
        print("Todas as áreas salvas foram deletadas.")
    else:
        print("Cultura inválida.")

# Aqui o usuario consegue manipular facilmente os dados.
# perceba que usamos a repetiçao a te o usuario quebrar o loop.
def menu_principal():
    while True:
        limpar_tela()
        print("-------------------------------------")
        print("       FarmTech Solutions v1.4       ")
        print("-------------------------------------")
        print("1. Entrada de Dados de Plantio")
        print("2. Saída de Dados de Plantio e Áreas Salvas")
        print("3. Atualizar um Dado Específico")
        print("4. Deletar Dados de uma Cultura")
        print("5. Calcular Manejo de Insumos")
        print("6. Salvar Áreas para Análise em R")
        print("7. Sair do Programa")
        print("-------------------------------------")
        
        escolha = input("Digite a sua opção: ")
        
        # Fazemos um encadeamento de if para escolha do usuario
        if escolha == '1':
            entrada_dados()
        elif escolha == '2':
            saida_dados()
        elif escolha == '3':
            atualizar_dados()
        elif escolha == '4':
            deletar_dados()
        elif escolha == '5':
            calcular_manejo_insumos()
        elif escolha == '6':
            salvar_areas_para_analise()
        elif escolha == '7':
            print("Saindo do programa. Obrigado por usar a FarmTech!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 7.")
            
        input("\nPressione Enter para continuar...") # Pausa para o usuário ler a mensagem

# Inicia o programa
if __name__ == "__main__":
    menu_principal()