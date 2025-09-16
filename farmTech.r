install.packages(c("httr", "jsonlite"))
library(httr)
library(jsonlite)

# =================================================================
#                 PARTE 1: ANÁLISE DOS DADOS DE ÁREA
# =================================================================

# Verifica se o arquivo com os dados de área existe
if (file.exists("C://Users//Tata//Desktop//Arquivos_Programação//gitProjeto//areas_plantio.csv")) {
  
  # Lê o arquivo CSV para um dataframe
  dados_areas <- read.csv("C://Users//Tata//Desktop//Arquivos_Programação//gitProjeto//areas_plantio.csv")
  
  # Mostra os dados que foram lidos para confirmar
  print("--- Dados de Área lidos do arquivo CSV ---")
  print(dados_areas)
  
  # Filtra os dados de Berinjela e Cana para análise separada
  areas_berinjela <- dados_areas[dados_areas$cultura == 'berinjela', 'area_m2']
  areas_cana <- dados_areas[dados_areas$cultura == 'cana', 'area_m2']
  
  # Analisa os dados de Berinjela
  if (length(areas_berinjela) > 1) {
    print("--- Análise Estatística para a Berinjela ---")
    print(paste("Média das áreas:", round(mean(areas_berinjela), 2), "m²"))
    print(paste("Desvio Padrão das áreas:", round(sd(areas_berinjela), 2), "m²"))
  } else {
    print("Dados insuficientes para análise de Berinjela.")
  }
  
  # Analisa os dados de Cana
  if (length(areas_cana) > 1) {
    print("--- Análise Estatística para a Cana ---")
    print(paste("Média das áreas:", round(mean(areas_cana), 2), "m²"))
    print(paste("Desvio Padrão das áreas:", round(sd(areas_cana), 2), "m²"))
  } else {
    print("Dados insuficientes para análise de Cana.")
  }
  
} else {
  print("Erro: O arquivo 'areas_plantio.csv' não foi encontrado.")
  print("Por favor, execute a opção 'Salvar Áreas para Análise em R' do programa Python primeiro.")
}


# =================================================================
#                 PARTE 2: DADOS CLIMÁTICOS VIA API
# =================================================================

print("\n--- Conectando à API do OpenWeatherMap ---")

# --- CONFIGURAÇÕES DA API ---
# 1. SUBSTITUA 'SUA_CHAVE_DE_API_AQUI' pela sua chave de API
api_key <- "SUA_CHAVE_DE_API_AQUI"
# 2. Insira a cidade que você quer consultar
cidade <- "Sao Caetano do Sul"
# 3. Idioma da resposta
idioma <- "pt"

# --- CONSTRUÇÃO E REQUISIÇÃO DA URL ---
url <- paste0(
  "https://api.openweathermap.org/data/2.5/weather?",
  "q=", cidade,
  "&appid=", api_key,
  "&lang=", idioma,
  "&units=metric"
)

# Faz a requisição HTTP
resposta <- GET(url)

# --- PROCESSAMENTO E EXIBIÇÃO ---
if (status_code(resposta) == 200) {
  
  # Converte a resposta JSON para uma lista em R
  dados_clima <- fromJSON(content(resposta, "text"))
  
  # Extrai as informações e exibe no terminal
  temp_atual <- dados_clima$main$temp
  descricao_clima <- dados_clima$weather$description
  umidade <- dados_clima$main$humidity
  sensacao_termica <- dados_clima$main$feels_like
  
  print(paste("--- Previsão do Tempo para", dados_clima$name, "---"))
  print(paste("Temperatura atual:", temp_atual, "°C"))
  print(paste("Sensação térmica:", sensacao_termica, "°C"))
  print(paste("Condição do tempo:", descricao_clima))
  print(paste("Umidade do ar:", umidade, "%"))
  print("-----------------------------------------")
  
} else {
  print(paste("Erro ao coletar dados. Código de status:", status_code(resposta)))
  print("Verifique se a sua chave de API e o nome da cidade estão corretos.")
}


# =================================================================
#            PARTE 3: ASSOCIAÇÃO ENTRE DADOS E CLIMA
# =================================================================

# Avaliação para a Berinjela
if (exists("areas_berinjela") && length(areas_berinjela) > 0 && exists("temp_atual")) {
  
  print("\n--- Relatório de Análise e Condições Climáticas (Berinjela) ---")
  print(paste("Área Média de Plantio de Berinjela:", round(mean(areas_berinjela), 2), "m²"))
  print(paste("Condição Climática na Área (Fonte: OpenWeatherMap):"))
  print(paste("  - Temperatura:", temp_atual, "°C"))
  print(paste("  - Umidade:", umidade, "%"))
  
  if (as.numeric(umidade) > 70) {
    print("\nAlerta: Alta umidade pode aumentar o risco de doenças fúngicas. Fique atento ao manejo dos insumos.")
  } else if (as.numeric(temp_atual) < 15) {
    print("\nAlerta: Temperaturas mais baixas podem desacelerar o crescimento da cultura. Considere o manejo nutricional adequado.")
  } else {
    print("\nCondições climáticas atuais são favoráveis para a cultura.")
  }
  
  print("-------------------------------------------------")
  
}

# Avaliação para a Cana
if (exists("areas_cana") && length(areas_cana) > 0 && exists("temp_atual")) {
  
  print("\n--- Relatório de Análise e Condições Climáticas (Cana) ---")
  print(paste("Área Média de Plantio de Cana:", round(mean(areas_cana), 2), "m²"))
  print(paste("Condição Climática na Área (Fonte: OpenWeatherMap):"))
  print(paste("  - Temperatura:", temp_atual, "°C"))
  print(paste("  - Umidade:", umidade, "%"))
  
  if (as.numeric(temp_atual) < 20) {
    print("\nAlerta: A cana-de-açúcar pode ter o crescimento desacelerado com temperaturas abaixo de 20°C.")
    print("É crucial que os canaviais recebam a nutrição ideal nesse período.")
  } else if (as.numeric(temp_atual) > 30) {
    print("\nAlerta: Temperaturas muito elevadas, especialmente com baixa umidade, podem causar estresse hídrico.")
    print("Atenção ao manejo de irrigação e adubação para otimizar o potencial produtivo da cultura.")
  } else {
    print("\nCondições climáticas atuais são ideais para o desenvolvimento da cana-de-açúcar.")
  }
  
  print("-------------------------------------------------")
  
}

# Mensagem final caso nenhum dos relatórios seja gerado
if (!exists("areas_berinjela") && !exists("areas_cana")) {
  print("\nNão foi possível gerar um relatório de associação.")
  print("Certifique-se de que os dados foram coletados no programa Python.")
}