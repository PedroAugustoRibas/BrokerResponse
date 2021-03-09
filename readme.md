# Broker response:

Projeto que realiza a tratativa dos dados que são depositados no diretório '/files'.
***
### Tecnologias e Ferramentas utilizadas:
 * Liguagem:
    * Python 3.8
 * Bibliotecas: 
   * requests
   * unittest
 * Sistema operecional:
   * Xubuntu
 * IDE:
   * Pycharm community
 ***   
#### Configurando o projeto:
Para exucutar este projeto é necessário que seja resgatado as dependências do projeto:
`pip install -r requirements.txt`
***
#### Executar o projeto:
Após a instalação das dependências do projeto para insira um arquivo no '/files' e execute o comando: `python3.8 main.py`
***
#### Padrão de arquivo:
```
bff58d7b-8b4a-456a-b852-5a3e000c0e63;12;996958849;NEXTEL;21:24:03;sapien sapien non mi integer ac neque duis bibendum
b7e2af69-ce52-4812-adf1-395c8875ad30;69;949360612;CLARO;19:05:21;justo lacinia eget tincidunt eget
e7b87f43-9aa8-414b-9cec-f28e653ac25e;34;990171682;VIVO;18:35:20;dui luctus rutrum nulla tellus in sagittis dui
c04096fe-2878-4485-886b-4a68a259bac5;43;940513739;NEXTEL;14:54:16;nibh fusce lacus purus aliquet at feugiat
d81b2696-8b62-4b8b-af82-586ce0875ebc;21;983522711;TIM;16:42:48;sit amet eros suspendisse accumsan tortor quis turpis sed ante
```
***
#### Testes:
Testes que estão no projeto: 
 
* Black list:`python3.8 -m unittest -v tests/test_blacklist.py`
* Broker :`python3.8 -m unittest -v tests/test_broker.py`




