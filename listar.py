import os
#Usa a pasta atual (onde o script é executado)

pasta = os.getcwd()
#Nome do arquivo de saída

arquivo_saida = "lista_arquivos.txt"

with open(arquivo_saida, "w", encoding="utf-8") as f:
for nome_arquivo in os.listdir(pasta):
if os.path.isfile(nome_arquivo):
f.write(nome_arquivo + "\n")

print(f"Lista de arquivos salva em: {os.path.join(pasta, arquivo_saida)}")
