#1 Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.

def numeros_impares(lista):
    return [n for n in lista if n % 2 != 0]

#2 Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def numeros_primos(lista):
    return [n for n in lista if eh_primo(n)]

#3 Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.

def elementos_exclusivos(lista1, lista2):
    return list(set(lista1) ^ set(lista2))

#4 Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.

def segundo_maior(lista):
    lista_unica = list(set(lista))
    lista_unica.sort()
    return lista_unica[-2]

#5 Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.

def ordenar_por_nome(lista):
    return sorted(lista, key=lambda x: x[0])

#6 Como identificar e tratar outliers em uma coluna numérica usando desvio padrão ou quartis?


def tratar_outliers_iqr(df, coluna):
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inf = Q1 - 1.5 * IQR
    limite_sup = Q3 + 1.5 * IQR
    return df[(df[coluna] >= limite_inf) & (df[coluna] <= limite_sup)]


#7 Como concatenar vários DataFrames (empilhando linhas ou colunas), mesmo que tenham colunas diferentes? Dica: Utiliza-se pd.concat() especificando axis=0 (linhas) ou axis=1 (colunas). Quando há colunas diferentes, os valores ausentes são preenchidos com NaN.

import pandas as pd


df_resultado = pd.concat([df1, df2], axis=0)

df_resultado = pd.concat([df1, df2], axis=1)

#8 Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?

import pandas as pd

df = pd.read_csv("arquivo.csv")
print(df.head())

#9 Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?

# Para elecionar uma coluna
df["coluna"]

# Para filtrar por linhas
df_filtrado = df[df["coluna"] > 10]

#10 Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

# Para identificar
df.isna()

# Para remover
df.dropna()

# Para preencher com 0
df.fillna(0)


