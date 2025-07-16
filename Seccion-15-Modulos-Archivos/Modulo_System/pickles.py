import pickle


lista = [1, 2, 3, 4, 5, 6,7,8]
ficheros = open("lista.pckl", "wb")
pickle.dump(lista, ficheros)
ficheros.close()
del(ficheros)

ficheros = open("lista.pckl","rb")
lista = pickle.load(ficheros)
print(lista)




import random

morat ={"nombre":"elmer","edad":15}

with open("nuevo.pckl","wb") as file:
    pickle.dump(morat,file)

with open("nuevo.pckl","rb") as files:
    data = pickle.load(files)
    print(data)


lista_numero =[round(random.random()*10) for x  in range(11)]
with open("lista.pckl","wb") as filess:
    pickle.dump(lista_numero,filess)

with open("lista.pckl","rb") as f :
    datas = pickle.load(f)
    print(datas)


