def print_numbers_times_2(numbers_list):
	for number in numbers_list:          #Este es un ciclo O(n) porque porque es un ciclo que va a ejecutarse n cantidad ed veces
		print(number * 2)
		

#_________________________________________________________________________________________________________________________________________________________



def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:
		for element_b in list_b:
			if element_a == element_b:    # Según lo analizado , este es un algoritmo que puede ejecutarse dependiendo de la cantidad de elementos de lista a y lista b
				return True                #Siguiendo el ejemplo de la correcion si hay 3 elementos en la list_a y 4 en la list_b, quiere decir que hay 12 ejecuciones del codigo 
                                        # entonces si comparo que "x" es los elementos de list_a y "z" los elementos de la list_b sería: O(x*z) en este caso ==  O(4*3)
	return False


#__________________________________________________________________________________________________________________________________________________________________________________

def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):# Según la revisión que hice entonces este sería O(1) porque en este caso el bucle no aumenta con "n" cuando este mismo es mayor a 10
		print(list_to_print[index])
		
#___________________________________________________________________________________________________________________________________________________________________________________

def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:    # Este algoritmo posee 3 bucles anindados y depende de la cantidad de elementos que se iteran en cada lista
				result_list.append(f'{element_a} {element_b} {element_c}')  #de elementos que se iteren en cada lista,     por ejemplo x= list_a, z=list_b,w=list_c
                                                                            #entonces O(x*z*w) siendo lo mismo que asumamos O(2*4*3)
	return result_list 