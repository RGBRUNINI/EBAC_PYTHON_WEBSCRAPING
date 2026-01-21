# PROJETO: Web Scraping de Dados Introdução 
# OBJETIVO: Inserir a coluna id_ibge no arquivo de população dos municípios
# AUTOR: RODRIGO GARCIA BRUNINI
# DATA: 20/01/2026 
# VERSÃO: 1.0

# Metodologia:
"""
Este script processa dados populacionais dos municípios brasileiros seguindo estas etapas:

1. LEITURA: Importa o arquivo Excel com dados de população municipal
2. PADRONIZAÇÃO: Ajusta códigos de UF (2 dígitos) e Município (5 dígitos) com zeros à esquerda
3. CRIAÇÃO DO ID: Gera o código IBGE único (7 dígitos) combinando UF + Município
4. REORGANIZAÇÃO: Posiciona a coluna id_ibge como primeira coluna da tabela
5. EXPORTAÇÃO: Salva o resultado final em formato CSV

Exemplo prático:
- Código UF: "35" (São Paulo)
- Código Município: "00001" 
- Resultado id_ibge: "3500001"

Glossário:
- DataFrame: Tabela de dados (como uma planilha Excel)
- fillna(""): Substitui células vazias por texto vazio
- zfill(n): Completa com zeros à esquerda até ter n dígitos
- id_ibge: Código padrão IBGE de 7 dígitos para identificar municípios
"""

import pandas as pd

# Caminhos
input_path = r"C:\Users\Rodrigo\Desktop\projetos\data\raw\populacao.xls"
output_path = r"C:\Users\Rodrigo\Desktop\projetos\data\raw\pop_corrigida.csv"
sheet_name = "Municípios"

# Leitura da planilha (header correto é 1)
df = pd.read_excel(input_path, sheet_name=sheet_name, header=1, dtype=str)

# Garante que são strings e remove NaN
df["COD. UF"] = df["COD. UF"].fillna("").str.zfill(2)
df["COD. MUNIC"] = df["COD. MUNIC"].fillna("").str.zfill(5)

# Cria o Id_ibge
df["id_ibge"] = df["COD. UF"] + df["COD. MUNIC"]

# Move Id_ibge para a primeira coluna
cols = ["id_ibge"] + [c for c in df.columns if c != "id_ibge"]
df = df[cols]

# Salva o resultado
df.to_csv(output_path, index=False, encoding="utf-8")
print("Arquivo gerado com sucesso em:")
print(output_path)

# Fim do script #