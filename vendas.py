import pandas as pd
import matplotlib.pyplot as plt

# Lê os dados
df = pd.read_csv('vendas.csv')

# Cria nova coluna com o total da venda
df['total'] = df['quantidade'] * df['preco']

# Agrupa por produto e soma
resumo = df.groupby('produto')['total'].sum()

# Gera gráfico de pizza
resumo.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Participação nas Vendas por Produto')
plt.ylabel('')

# Salva a imagem
plt.savefig('vendas.png')

print("✅ Gráfico de vendas gerado com sucesso!")
