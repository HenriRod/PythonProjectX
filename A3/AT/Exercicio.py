#print com as opções
print (" 1 - Para comprar Maçã ")
print (" 2 - Para comprar Laranja ")
print (" 3 - para comprar Banana ")

#input com int para receber o item selecionado & um input para a quantidade desejada
a = int(input(" Tecla o numero do seu produto!"))
b = int(input(" digite a quantidade desejada!"))


if a == 1:
    print(f" Voce escolheu {b} maças. o valor vai ficar em R$ {b*2.3}")
elif a == 2:
    print(f" Voce escolheu {b} laranja. o valor vai ficar em R$ {b*3.6}")
elif a == 3:
    print(f" Voce escolheu {b} banana. o valor vai ficar em R$ {b*1.85}")
else:
    print("Produto inexistente!")
