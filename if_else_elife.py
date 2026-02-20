hora = int(input("Digite a hora: ")) 
humor = input("Digite o humor (sono ou sedento ou outro) ")

if humor == "sono" and hora < 10:
    print("café")
elif humor == "sedento" or hora < 2:
    print("limonada")
else:
    print("água")