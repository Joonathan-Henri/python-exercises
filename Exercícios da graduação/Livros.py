import pandas as pd
import os

# Localiza o arquivo books.csv na mesma pasta do código
pasta = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(pasta, "books.csv")

# Carrega o CSV e detecta automaticamente o separador
df = pd.read_csv(
    arquivo,
    sep=None,
    engine="python",
    on_bad_lines="skip"
)

# Remove possíveis espaços dos nomes das colunas
df.columns = df.columns.str.strip()

