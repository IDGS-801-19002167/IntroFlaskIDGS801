from io import open

# archivo1 = open('archivo.txt', 'a')
# archivo1.write('\n jsjsjs')
# archivo1.close()

archivo1 = open('archivo.txt')
# print(archivo1.read())
# archivo1.seek(3)
# print(archivo1.read())

# print(archivo1.readlines())

for datos in archivo1.readlines():
    print(datos)

archivo1.close()