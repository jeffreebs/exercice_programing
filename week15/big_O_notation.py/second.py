def print_numbers_times_2(numbers_list):
	for number in numbers_list:          #Este es un ciclo O(n) porque porque es un ciclo que va a ejecutarse n cantidad ed veces
		print(number * 2)
		

#_________________________________________________________________________________________________________________________________________________________



def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:
		for element_b in list_b:
			if element_a == element_b:    # Este es de tipo O(n) porque se va a ejecutar n cantidad de veces pero no tiene mas de dos ciclos anidados para pertenecer al otro.
				return True
				
	return False


#__________________________________________________________________________________________________________________________________________________________________________________

def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):# Este es del tipo O(log n) porque va disminuyendo su cantidad deiteraciones cuanto más grande sea el input
		print(list_to_print[index])
		
#___________________________________________________________________________________________________________________________________________________________________________________

def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:    # Este es de tipo O(n^2) porque posee ciclos aninados
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 