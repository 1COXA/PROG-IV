import re
import os

# Padrões Regex
padroes = {
    "CEP": r"\b\d{5}-?\d{3}\b",
    "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "CPF": r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b",
    "CNPJ": r"\b\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}\b",
    "TELEFONE": r"\(?\d{2}\)?\s?9?\d{4}-?\d{4}",
    "PLACA_VEICULAR": r"\b[A-Z]{3}-?\d{4}\b|\b[A-Z]{3}\d[A-Z0-9]\d{2}\b",
    "IP": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "DATA": r"\b\d{2}/\d{2}/\d{4}\b",
    "URL": r"https?://[^\s]+"
}

arquivo = "dados.txt"

print(f"Pasta atual: {os.getcwd()}")
print("-" * 50)

try:
    with open(arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    encontrou = False

    print("RESULTADOS DA ANÁLISE")
    print("=" * 50)

    for numero_linha, linha in enumerate(linhas, start=1):
        for tipo, regex in padroes.items():
            resultados = re.findall(regex, linha)

            if resultados:
                encontrou = True

                for resultado in resultados:
                    print(f"Linha {numero_linha:02d} | {tipo:<15} | {resultado}")

    print("=" * 50)

    if not encontrou:
        print("Nenhum padrão encontrado no arquivo.")

except FileNotFoundError:
    print(f"ERRO: O arquivo '{arquivo}' não foi encontrado.")
    print("Verifique se ele está na mesma pasta do programa.")