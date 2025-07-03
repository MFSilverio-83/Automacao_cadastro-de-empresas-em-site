🤖 Automação de Cadastro de Empresas 🏢

Este projeto é uma solução de automação (RPA) desenvolvida para eliminar a tarefa manual e repetitiva de cadastrar múltiplas empresas em uma plataforma web contábil. Utilizando uma planilha Excel como fonte de dados, o robô realiza o login no sistema, preenche os formulários de cadastro de forma iterativa e encerra o processo automaticamente.

✨ Funcionalidades Principais
✅ Automação de ponta a ponta: Desde o login no site até o preenchimento de cada campo do formulário.

✅ Fonte de Dados Externa: Lê os dados das empresas a serem cadastradas diretamente de um arquivo Excel (empresas.xlsx).

✅ Gerenciamento de Credenciais Seguro: Carrega os dados de login (usuário e senha) de uma planilha separada (login.xlsx), evitando que informações sensíveis fiquem no código.

✅ Processo em Lote: Utiliza um laço de repetição (for) para cadastrar todas as empresas listadas na planilha de uma só vez.

✅ Feedback Visual: Inclui pausas estratégicas (time.sleep) que permitem acompanhar o processo de preenchimento em tempo real.

🚀 Tecnologias Utilizadas (Stack)
Linguagem: 🐍 Python 3

Automação Web: 🤖 Selenium

Manipulação de Dados: 📊 Pandas & Openpyxl

⚙️ Instalação e Configuração
Para executar este projeto, siga os passos abaixo.

1. Pré-requisitos
Python 3.8 ou superior.

Um navegador web como Google Chrome ou Firefox.

O WebDriver correspondente ao seu navegador. O Selenium precisa dele para controlar o navegador.

ChromeDriver: https://googlechromelabs.github.io/chrome-for-testing/

GeckoDriver (Firefox): https://github.com/mozilla/geckodriver/releases

💡 Dica: Após o download, coloque o executável do WebDriver em uma pasta que esteja no PATH do seu sistema, ou anote o caminho completo para ele.

2. Instalação
   
- Clone o repositório:

git clone https://github.com/seu-usuario/automacao_cadastro-de-empresas-em-site.git cd automacao_cadastro-de-empresas-em-site

- Crie e ative um ambiente virtual (altamente recomendado):

Windows
python -m venv venv
.\venv\Scripts\activate

macOS / Linux
python3 -m venv venv
source venv/bin/activate

- Instale as dependências a partir do arquivo requirements.txt:
pip install pandas selenium openpyxl

3. Preparação dos Arquivos de Dados
O robô precisa de dois arquivos Excel na mesma pasta do script para funcionar.

A. Planilha de Empresas (empresas.xlsx)
Crie um arquivo chamado empresas.xlsx com as colunas que o formulário do site exige. O nome das colunas deve ser claro para o seu uso no código.

Exemplo:
| CNPJ | Razao_Social | Nome_Fantasia | Endereco | Cidade | Estado | CEP | Telefone |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 11222333000144| Empresa Exemplo LTDA | Fantasia Exemplo | Rua das Flores, 123 | São Paulo | SP | 01000-000 | 11987654321 |
| 55666777000188| Companhia Teste S.A. | Teste Corp | Av. Principal, 456 | Rio de Janeiro| RJ | 02000-000 | 21912345678 |

B. Planilha de Login (login.xlsx) 🔑
Crie um arquivo chamado login.xlsx para armazenar as credenciais de acesso ao site de forma segura.

Exemplo:
| email | senha |
| :--- | :--- |
| seu_email@contabilidade.com | SuaSenhaSuperSecreta |

▶️ Como Executar
Com tudo configurado, basta executar o script principal no seu terminal:
python seu_script_de_automacao.py

O navegador será aberto e o processo de cadastro começará automaticamente. Acompanhe a magia acontecer! Ao final de todos os cadastros, o navegador será fechado.

💡 Observações e Customização
Seletores do Selenium: Este robô foi feito para um site específico. Os seletores (ex: By.ID, By.XPATH, By.NAME) usados para encontrar os campos de login e do formulário estão fixos no código. Se você quiser adaptar este robô para outro site, a principal alteração será atualizar esses seletores para que correspondam aos elementos da nova página.

Velocidade de Execução: As pausas (time.sleep()) são úteis para visualização e para aguardar o carregamento de elementos da página. Para uma execução mais rápida (em produção), você pode diminuir a duração dessas pausas ou substituí-las por esperas inteligentes do Selenium (WebDriverWait).

👤 Autor

Sinta-se à vontade para me contatar ou contribuir com o projeto!

[Marcio Freire Silverio]
