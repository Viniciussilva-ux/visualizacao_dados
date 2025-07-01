import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# Histograma
plt.hist(df['salario'])
plt.show()

# Histograma - Parâmetros
plt.figure(figsize=(10,6))
plt.hist(df['salario'], bins=100, color='green', alpha=0.8)
plt.title('Histograma - Distribuição de Salários')
plt.xlabel('salario')
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Múltiplos Gráficos
plt.figure(figsize=(10,6))
plt.subplot(2, 2, 1) # 2 linhas, 2 colunas, 1 gráfico

# Gráfico de Dispersão
plt.scatter(df['salario'], df['salario'])
plt.title('Dispersão - Salario e Salario')
plt.xlabel('Salário')
plt.ylabel('Salário')

plt.subplot(1,2,2) # 1 linha , 2 colunas, 2 gráficos
plt.scatter(df['salario'], df['anos_experiencia'], color='#5883a8', alpha=0.6, s=30 ) # Cor hexadecimal online
plt.title('Dispersão - Idade e Anos de Experiência')
plt.xlabel('Salário')
plt.ylabel('Anos de Experiência')

# Mapa de Calor
corr= df[['salario', 'anos_experiencia']].corr()
plt.subplot(2, 2, 3) # 1 linha , 2 colunas , 3 gráfico
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salário e Idade')

plt.tight_layout() # Ajustar espaçamentos
plt.show()

