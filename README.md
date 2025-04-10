# 📊 Projeto de Análise de Vendas com Docker

Este projeto faz uma análise simples de vendas a partir de um arquivo CSV e gera um gráfico de pizza com a participação de cada produto nas vendas totais. Tudo isso é executado dentro de um container Docker! 🐳

## 💼 Tecnologias usadas

- Python 3.10
- Pandas
- Matplotlib
- Docker

## 📁 Estrutura do projeto

projeto-vendas-docker/ ├── vendas.csv # Dados de entrada ├── vendas.py # Script de análise ├── vendas.png # Gráfico gerado ├── Dockerfile # Receita do ambiente Docker ├── requirements.txt # Bibliotecas usadas └── README.md # Documentação


## 🚀 Como rodar com Docker

1. Clone o repositório:

```bash
git clone https://github.com/GabiSilvaBelo/projeto-vendas-docker.git
cd projeto-vendas-docker

Construa a imagem:
docker build -t projeto-vendas 

Rode o container:
docker run -v "$(pwd)":/app projeto-vendas

Veja o gráfico gerado em vendas.png

[Gráfico de Vendas](vendas.png)


Autor(a)

Feito com 💜 por Gabriela Belo da Silva