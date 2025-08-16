# Passo 1. Criar o navegador
import win32com.client as win32
# Importa o módulo principal do Selenium para controlar o navegador
from selenium import webdriver
# Importa a classe Service para configurar o ChromeDriver
from selenium.webdriver.chrome.service import Service
# Gerencia automaticamente o download do ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import pandas as pd
import re
import time

# Cria o serviço do ChromeDriver, baixando a versão compatível automaticamente
servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)

# Passo 2. Importar/Visualizar a base de dados
tabela_produtos = pd.read_excel('buscas.xlsx')
display(tabela_produtos)

# Passo 3. Definição da função de busca do Google Shooping


def busca_google_shopping(driver, produto, termos_banidos, preco_minimo, preco_maximo):
    produto = produto.lower()
    termos_banidos = termos_banidos.lower()
    lista_termos_banidos = termos_banidos.split(' ')
    lista_termos_nome_produto = produto.split(' ')

    preco_minimo = float(preco_minimo)
    preco_maximo = float(preco_maximo)
    lista_ofertas = []

    # Abrir Google
    driver.get("https://www.google.com.br/")

    # Pesquisar produto
    try:
        campo_busca = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="APjFqb"]')))
        campo_busca.send_keys(produto)
        campo_busca.send_keys(Keys.ENTER)
    except TimeoutException:
        print("Campo de busca não encontrado.")
        return []
    time.sleep(2)

    # Clicar na aba "Shopping"
    try:
        shopping_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="cnt"]/div[4]/div/div[1]/div/div/div[1]/div[2]/a/div')))
        shopping_btn.click()
    except TimeoutException:
        print("Aba 'Shopping' não encontrada.")
        return []
    time.sleep(2)

    # Capturar blocos
    blocos = driver.find_elements(
        By.CSS_SELECTOR, 'div[jsname="ZvZkAe"].njFjte')

    for bloco in blocos:
        aria_label = bloco.get_attribute("aria-label")
        if not aria_label:
            continue

        texto_completo = aria_label.lower()
        nome = aria_label.split(".")[0].strip().lower()

        # Filtra termos banidos
        tem_termo_banido = False
        for palavra in lista_termos_banidos:
            if palavra in texto_completo:
                tem_termo_banido = True
                break
        if tem_termo_banido:
            continue

        # Garante que todos os termos do produto estão presentes
        todos_termos_presentes = True
        for palavra in lista_termos_nome_produto:
            if palavra not in texto_completo:
                todos_termos_presentes = False
                break
        if not todos_termos_presentes:
            continue

        # Extrair preço
        preco_match = re.search(r'R\$[\s\xa0]*([\d\.]+,\d{2})', aria_label)
        if not preco_match:
            continue
        preco = preco_match.group(1).replace(".", "").replace(",", ".")
        preco = float(preco)

        if not (preco_minimo <= preco <= preco_maximo):
            continue

        # Abrir painel lateral
        bloco.click()
        time.sleep(2)

        # Obter link
        try:
            link_element = driver.find_element(By.CSS_SELECTOR, 'div.zTzk8e a')
            link = link_element.get_attribute("href")
        except NoSuchElementException:
            link = None

        # Fechar painel lateral
        try:
            fechar_btn = driver.find_element(
                By.CSS_SELECTOR, 'div.RSNrZe[aria-label="Fechar"]')
            fechar_btn.click()
            time.sleep(1)
        except NoSuchElementException:
            pass

        lista_ofertas.append((nome, preco, link))

    return lista_ofertas

# Passo 4. Definição da função de busca do Buscapé


def busca_buscape(driver, produto, termos_banidos, preco_minimo, preco_maximo):
    produto = produto.lower()
    termos_banidos = termos_banidos.lower()
    lista_termos_banidos = termos_banidos.split(' ')
    lista_termos_nome_produto = produto.split(' ')

    preco_minimo = float(preco_minimo)
    preco_maximo = float(preco_maximo)
    lista_ofertas = []

    # Abrir Buscapé
    driver.get("https://www.buscape.com.br/")

    # Pesquisar produto
    try:
        campo_busca = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="new-header"]/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/input')))
        campo_busca.send_keys(produto)
        campo_busca.send_keys(Keys.ENTER)
    except TimeoutException:
        print("Campo de busca não encontrado.")
        return []

    # Aguardar carregamento
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'ProductCard_ProductCard_Inner__gapsh'))
        )
    except TimeoutException:
        print("Produtos não carregaram.")
        return []

    # Pegar resultados
    lista_resultados = driver.find_elements(
        By.CLASS_NAME, 'ProductCard_ProductCard_Inner__gapsh')

    for resultado in lista_resultados:
        # Extrai o nome
        try:
            nome = resultado.find_element(
                By.CLASS_NAME, 'ProductCard_ProductCard_Name__U_mUQ').text.lower()
        except NoSuchElementException:
            nome = None

        # Extrai o preço
        try:
            preco_str = resultado.find_element(
                By.CLASS_NAME, 'Text_MobileHeadingS__HEz7L').text
            preco_str = preco_str.replace("R$", "").replace(
                ".", "").replace(",", ".").strip()
            preco = float(preco_str)
        except NoSuchElementException:
            preco = None

        # Link
        try:
            link = resultado.get_attribute('href')
        except NoSuchElementException:
            link = None

        # Verifica se o nome do produto contém algum termo banido
        tem_termo_banido = False
        for palavra in lista_termos_banidos:
            if palavra in nome:
                tem_termo_banido = True
                break  # Não precisa continuar procurando, já achamos um termo banido

        if tem_termo_banido:
            continue  # pula para o próximo produto

        # Verifica se o nome do produto contém TODOS os termos obrigatórios
        todos_termos_presentes = True
        for palavra in lista_termos_nome_produto:
            if palavra not in nome:
                todos_termos_presentes = False
                break  # Se faltar um termo, não precisa continuar verificando

        if not todos_termos_presentes:
            continue  # pula para o próximo produto

        # Verifica se o preço está dentro da faixa desejada
        if preco_minimo <= preco <= preco_maximo:
            lista_ofertas.append((nome, preco, link))

    return lista_ofertas


# Passo 5. Execução da busca e armazenamento das tabelas de produtos
tabelas_produtos = {}  # Dicionário para armazenar as tabelas de cada produto

# Percorre cada linha da planilha e executa as buscas para cada produto
for linha in tabela_produtos.index:
    # Pega os dados da linha atual
    produto = tabela_produtos.loc[linha, 'Nome']
    termos_banidos = tabela_produtos.loc[linha, 'Termos banidos']
    preco_minimo = tabela_produtos.loc[linha, 'Preço mínimo']
    preco_maximo = tabela_produtos.loc[linha, 'Preço máximo']

    # Lista temporária para juntar resultados do Google e Buscapé
    lista_ofertas = []

    # Busca no Google Shopping
    lista_ofertas_google_shopping = busca_google_shopping(
        driver, produto, termos_banidos, preco_minimo, preco_maximo)
    if lista_ofertas_google_shopping:
        lista_ofertas.extend(lista_ofertas_google_shopping)
    else:
        print(f"O produto '{produto}' não foi encontrado no Google Shopping.")

    # Busca no Buscapé
    lista_ofertas_buscape = busca_buscape(
        driver, produto, termos_banidos, preco_minimo, preco_maximo)
    if lista_ofertas_buscape:
        lista_ofertas.extend(lista_ofertas_buscape)
    else:
        print(f"O produto '{produto}' não foi encontrado no Buscapé.")

    # Se encontrou algum produto, cria a tabela final e ordena pelo preço
    if lista_ofertas:
        tabela_ofertas_final = pd.DataFrame(
            lista_ofertas, columns=['Produto', 'Preço', 'Link'])
        tabela_ofertas_final = tabela_ofertas_final.sort_values(
            by='Preço', ascending=True).reset_index(drop=True)
        # Guarda a tabela no dicionário
        tabelas_produtos[produto] = tabela_ofertas_final
        print(f"\nOfertas encontradas para: {produto}")
        display(tabela_ofertas_final)


# Passo 7. Verifica se há pelo menos uma tabela de ofertas
nome_arquivo = Path("ofertas_por_produto.xlsx")  # Já define o Path aqui

if tabelas_produtos:
    # Cria o arquivo Excel com múltiplas abas
    with pd.ExcelWriter(nome_arquivo, engine="openpyxl") as writer:
        for produto, tabela in tabelas_produtos.items():
            # Limite de 31 caracteres para nome da aba
            nome_sheet = produto[:31]
            tabela.to_excel(writer, sheet_name=nome_sheet, index=False)

    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
else:
    nome_arquivo = None  # Marca que nenhum arquivo foi gerado

# Passo 8. Envia o e-mail com o arquivo anexado

if nome_arquivo and nome_arquivo.exists():
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'teste.nrlima@gmail.com'
    mail.Subject = 'Produto(s) Encontrado(s) na faixa de preço desejada'
    mail.HTMLBody = """
        <p>Prezados,</p>
        <p>Encontramos alguns produtos em oferta dentro da faixa de preço desejada. Segue tabela em anexo com detalhes:</p>
        <p>Qualquer dúvida estou à disposição</p>
        <p>Att.,</p>
        <p>Michely</p>
    """
    mail.Attachments.Add(str(nome_arquivo.resolve()))  # caminho absoluto
    mail.Send()
    print('E-mail enviado com sucesso!')
else:
    print("Nenhuma oferta foi encontrada. Nenhum arquivo foi gerado.")
