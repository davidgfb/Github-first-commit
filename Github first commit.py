nCommits=int(input("¿Cuantos commits hay?\n"))
pos=nCommits-36
url=input("Ve a commits, clicka ""older"" e introduce la url obtenida\n")
posMas=0

for posCaracter in range(len(url)):
    if url[posCaracter]=="+":
        posMas=posCaracter

url=url[:posMas+1:]+str(pos) #para dejar el "+"
print("Aqui tienes que lo disfrutes:\n",url)
