# automacao_cadastro-de-empresas-em-site
Automação que faz o cadastro de várias empresas em um site contábil

Código criado para automatizar o cadastro de empresas em um site contábil.
No código foram utilizadas as bibliotecas Pandas, Selenium e Openpyxl. Tabém utilizados os módulos time e os
Estas bibliotecas são utilizadas para a manipulação de planilhas, arquivos e controle de navegador web.
Foram utilizas configurações para que os dados de e-mail e senha fiquem numa planilha externa e sejam utilizados em variáveis dentro do código.

O funcionamento do código de maneira geral consiste em abrir o site que será utilizado, obter os dados de email e senha para acessar, e, após o acesso, ir cadastrando campo a campo que é solicitado. Foram colocadas pequenas pausas no código para que seja possível a visualização dos cadastros. No fim do código o cadastro é realizado e se inicia, de forma automática, um novo cadastro de empresa. Este ciclo é feito pelo laço for. Quando os dados da planilha terminam, a página é fechada de forma automática.
