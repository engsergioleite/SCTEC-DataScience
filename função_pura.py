def pure_increments (elements, index):
    new_elements = elements.copy()
    new_elements[index] += 1
    return new_elements 

lista = [1,2,3,4,5,6,7,8,9,10]

print(pure_increments(lista, 0))

print(lista)

