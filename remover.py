import os
#Nome do arquivo com a lista de arquivos a remover

arquivo_remover = "remover.txt"
#Lê os nomes dos arquivos do txt

with open(arquivo_remover, "r", encoding="utf-8") as f:
arquivos = [linha.strip() for linha in f]
#Apaga cada arquivo listado

for arquivo in arquivos:
if os.path.isfile(arquivo):
os.remove(arquivo)
print(f"Arquivo removido: {arquivo}")
else:
print(f"Arquivo não encontrado: {arquivo}")

print("Processo concluído.")
