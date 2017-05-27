# Programa que usa uma função recursiva para selecionar o código cutter
# correto de um arquivo .csv.
# Bruno de Sá - 25/05/2017.

from unicodedata import normalize
import csv

def processaCutter(nome):
    """Cria o dicionário com os valores do arquivo cutter.csv"""
    with open('cutter.csv', 'r') as arquivo:
        leitor = csv.DictReader(arquivo)
        dicionario = {}
        for linha in leitor:
            dicionario[removeAcentuacao(linha['texto']).lower()] = linha['codigo']
        lista = list(dicionario.items())
        lista = sorted(lista, key=lambda x: x[0])
    return selecionaCutter(removeAcentuacao(nome).lower(), lista, 0)

def selecionaCutter(nome, lista, i):
    """Função recursiva que seleciona o par chave - valor correto"""
    nova_lista = []
    
    for tupla in lista:
        if i >= len(nome):
            print(i)
            return int(lista[0][1])
            
        if i >= len(tupla[0]):
            continue
            
        if nome[i] == tupla[0][i]:
            nova_lista.append(tupla)
    
    if nova_lista:
        print("Iteração", i, nova_lista, "\n")
        return selecionaCutter(nome, nova_lista, i + 1)
    else:
        return lista[0][1]

def removeAcentuacao(texto):
    """Remove a acentuação e caracteres especiais no texto"""
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

nome = input("Insira um nome: ")
print("Cutter: ", processaCutter(nome))
