# 🛒 Automação Inteligente de Busca e Comparação de Preços  

![Python](https://img.shields.io/badge/Python-3.10%2B-FFD43B?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-Web%20Automation-43B02A?logo=selenium) 
![Excel](https://img.shields.io/badge/Excel-Reports-217346?logo=microsoft-excel) 
![Outlook](https://img.shields.io/badge/Outlook-E--mail-0078D4?logo=microsoft-outlook) 
![Status](https://img.shields.io/badge/Status-Funcional-8A2BE2) 

Automatize sua pesquisa de preços em **Google Shopping** e **Buscapé** com Python + Selenium.  
O sistema coleta resultados, aplica filtros personalizados e envia um **relatório em Excel por e-mail**. 

> ⚠️ **Importante:** por se tratar de automação web, **alterações no site (Google Shopping e Buscapé)** podem exigir **ajustes no código** (especialmente na seleção de elementos).



## 📖 Visão Geral  
O projeto elimina a necessidade de buscas manuais por preços, automatizando:  
- Navegação em **Google Shopping** e **Buscapé**  
- Filtros inteligentes de **preço mínimo/máximo** e **termos banidos**  
- Geração de planilhas Excel com os melhores resultados  
- Envio automático do relatório por **e-mail via Outlook**  

💡 Ideal para **consumidores atentos a promoções** e **empresas que monitoram concorrência**.  



## 🎯 Funcionalidades  
✔️ Busca automática em múltiplos sites (Google Shopping + Buscapé)  
✔️ Filtros de preço e exclusão de termos indesejados  
✔️ Relatórios organizados em Excel com múltiplas abas  
✔️ Envio automático por e-mail com anexo  



## 🛠️ Tecnologias Utilizadas  
- **Python 3.10+**  
- **Selenium** → Automação de navegador  
- **WebDriver Manager** → Gestão automática do ChromeDriver  
- **Pandas + OpenPyXL** → Manipulação e exportação para Excel  
- **win32com.client (Outlook API)** → Envio de relatórios por e-mail  



## 📂 Estrutura do Projeto  
```plaintext
automacao-busca-precos/
│
├── Automação_busca_preços.py   # Script principal
├── buscas.xlsx         # Planilha de entrada (produtos e critérios)
├── ofertas_por_produto.xlsx    # Arquivo gerado com resultados (saída)
└── README.md                    # Documentação
```


## ⚙️ Funcionamento
1. **Planilha `buscas.xlsx` com colunas:**
- Nome do produto
- Termos banidos
- Preço mínimo
- Preço máximo

2. **Processamento:**
- Busca automática no Google Shopping e Buscapé
- Filtro inteligente dos resultados
- Ordenação por menor preço

3. **Saída:**
- Planilha `ofertas_por_produto.xlsx` organizada em abas por produto
- Envio por e-mail via Outlook com a planilha em anexo


## 🚀 Como Executar
1. **Baixar o projeto**
   ```plaintext
   git clone https://github.com/seuusuario/automacao-busca-precos.git
   cd automacao-busca-precos
   ```

2. **Instalar as dependências**
   ```plaintext 
   pip install selenium pandas openpyxl webdriver-manager pywin32
   ```
3. Prepare a planilha `buscas.xlsx` com os produtos e critérios.

4. Configure o e-mail no script (`Automação_busca_preços.py`):.
- Endereço do remetente
- Senha/token
- Destinatário

5. Execute o projeto:
   ```plaintext  
   python Automação_busca_preços.py
   ```

## ⚠️ Observações Importantes

🔄 Devido às constantes atualizações nos sites (Google Shopping e Buscapé), pode ser necessário adaptar o código periodicamente para garantir o funcionamento correto da automação.



## 📌 Possíveis Extensões
- Integração com APIs de marketplaces (Amazon, Mercado Livre, etc.)
- Dashboard web interativo para acompanhar resultados
- Notificações via Telegram/WhatsApp
- Execução agendada (cron/Task Scheduler)



## 🤝 Contribuição

Contribuições são bem-vindas!
Abra uma issue ou envie um pull request com melhorias.



## 📜 Licença

Este projeto é de licença pública — você pode usar, modificar e distribuir livremente.
