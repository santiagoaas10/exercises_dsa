num1 = 11
num2 = num1

print('Befor num1 is updated:')
print('num1= ', num1)
print('num2= ', num2)

print('\nnum1 points to; ', id(num1))  # mem address where num1 (11) is stored
print('\nnum2 points to; ', id(num2)) # mem address where num2 (11) is stored
#they are pointing to the same


num2 = 22

print('num2 updated:')
print('num1= ', num1)
print('num2= ', num2)

print('\nnum1 points to; ', id(num1))  # mem address where num1 (11) is stored
print('\nnum2 points to; ', id(num2)) # mem address where num2 (22) is stored
#they changed, los integers son inmutables (el 11 no se cambio, se mantuvo igual y el 22 fue asignado a otra direccion de memoria)


print('\n -------------------------- ')
print('\n -------------------------- ')
print('\n -------------------------- ')

print('ahora veamos si pasa lo mismo con los diccionarios')

dict1 = {'value':11}
dict2 = dict1
print('dict1: ',dict1)
print('dict2: ',dict2)


print('\ndict1 points to; ', id(dict1))  # mem address where num1 (11) is stored
print('\ndict2 points to; ', id(dict2)) # mem address where num2 (22) is stored

#lets change and see what happens:
dict2['value']=22
print('updating dict2')
print('dict1: ',dict1)
print('dict2: ',dict2)
print('\ndict1 points to; ', id(dict1))  # mem address where num1 (11) is stored
print('\ndict2 points to; ', id(dict2)) # mem address where num2 (22) is stored

#SE ACTUALIZO TAMBN EL VALUE DEL DICCIONARIO 1 CON LO QUE HICIMOS EN LA LINEA 40 :0000, OJO 
#Y DICCIONARIO 1 Y DICCIONARIO 2 ESTAN AUN APUNTANDO A LA MISMA DIRECCION, MORALEJA:
#MORALEJA: A DIFERENCIA DE LOS ENTEROS, LOS DICCIONARIOS SI SON MUTABLES