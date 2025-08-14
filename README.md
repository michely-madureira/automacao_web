# 🛒 Automação Web para Busca e Comparação de Preços
Projeto de automação web com Selenium para busca de informações

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/Licença-Pública-blue)



## 📄 Visão Geral
Este projeto implementa uma **automação web** utilizando **Python e Selenium** para realizar buscas de preços de produtos em plataformas como **Google Shopping** e **Buscapé**, aplicando filtros pré-definidos e enviando os resultados por e-mail.

O objetivo principal é **reduzir o tempo e esforço** gastos na busca manual de preços, oferecendo uma solução escalável e adaptável para diferentes cenários corporativos ou pessoais.



## 🎯 Objetivos do Projeto
- Automatizar a busca de preços de produtos em sites de e-commerce e comparadores de preços.
- Filtrar resultados com base em:
  - Faixa de preço mínima e máxima.
  - Exclusão de termos indesejados.
- Registrar e atualizar os resultados em planilha Excel.
- Enviar relatório por e-mail com links diretos de compra.



## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**
- **Selenium** – Automação de navegação
- **Pandas** – Manipulação de dados
- **OpenPyXL** – Leitura e escrita de planilhas Excel
- **smtplib** – Envio de e-mails via protocolo SMTP



## 📂 Estrutura do Projeto
```plaintext
automacao-busca-precos/
│
├── main.py              # Script principal
├── produtos.xlsx        # Lista de produtos e critérios de busca
├── requisitos.txt       # Lista de dependências do projeto
└── README.md            # Documentação do projeto
```



## ⚙️ Funcionamento
1. **Entrada de dados –** O arquivo produtos.xlsx contém:
- Nome do produto
- Preço mínimo
- Preço máximo
- Termos a evitar
2. **Processamento:**
- Pesquisa automática no Google Shopping e Buscapé.
- Filtragem de resultados por faixa de preço e termos.
- Registro das informações relevantes (preço, loja, link).
3. **Saída:**
- Planilha atualizada com os resultados encontrados.
- Envio de e-mail com resumo e links de compra.



## 🚀 Como Executar
1. **Baixar o projeto**
   ```bash
   git clone https://github.com/seuusuario/automacao-busca-precos.git
   cd automacao-busca-precos

2. **Instalar as dependências**
   ```bash  
   pip install -r requisitos.txt

3. **Configurar o e-mail**
- Abra o arquivo `main.py`
- Preencha:
	* E-mail remetente
	* Senha ou token de acesso
	* E-mail destinatário
4. **Adicionar a planilha de produtos**
- Coloque o arquivo `produtos.xlsx` na pasta principal do projeto.
5. **Rodar o projeto**
   ```bash  
   python main.py


## 📌 Possíveis Extensões
- Conexão com APIs de marketplaces para maior velocidade e precisão.
- Dashboard interativo para acompanhar resultados em tempo real.
- Envio de alertas via WhatsApp ou Telegram.
- Agendamento automático de execuções diárias.



## 📜 Licença
Este projeto é de licença pública — você pode usar, modificar e distribuir livremente.
