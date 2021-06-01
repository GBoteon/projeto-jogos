from operator import itemgetter

scoresDict = {}
scoresDict_List = []
ranking = []

# Faz a leitura do arquivo txt
with open('scores.txt', "r+") as textFile:
    lines = textFile.readlines()
    scoresList = list(map(lambda s: s.strip(), lines))

# Cria um dicionário sendo chave = linha(n) / valor = linha(n+1)
for i in range(0, len(scoresList)-1, 2):
    scoresDict[scoresList[i]] = scoresList[i+1]

# Tentativas de ordenação decrescente do dicionário pelo valor. Incluir os elementos do dict, após a ordenação, na lista scoreDict_List.
# Tentativa.01 OBS: Esta ordenando pelo primeiro caractere  dos valores e não pelos valores inteiros.
for i in sorted(scoresDict, key=scoresDict.get, reverse=True):
    print(i, scoresDict[i])
print("--------")

# Tentativa.02 OBS: Esta ordenando pelo primeiro caractere  dos valores e não pelos valores inteiros.
scoresDict_List = list(sorted(scoresDict.items(), key=itemgetter(1)))
print(scoresDict_List)

# Percorrendo a lista scoreDict_List, separando assim chave e valor em index um seguido do outro.
for i in scoresDict_List:
    ranking.append(i[0])
    ranking.append(i[1])

# Imprimindo nome e seu respectivo ranking na tela.
for i in range(0, 5, 2):
    print(f"{ranking[i]} : {ranking[i+1]}")


# scoresDict_List = list(scoresDict.items()) ----[Não apagar]----

# ----[Adicionando linhas ao arquivo .txt]----

# lines.insert(len(scoresList) + 1, "Roberto:" + "\n")
# lines.insert(len(scoresList) + 1, "2000" + "\n")
# textFile.writelines(lines)
# textFile.close()
# print("--------------")
# with open('scores.txt', "r+") as textFile:
#     lines = textFile.readlines()
#     scoresList = list(map(lambda s: s.strip(), lines))
#     for i in range(0, len(scoresList)-1, 2):
#         print(scoresList[i] + scoresList[i+1])
