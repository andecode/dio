"""repete_txt.py

Solicita uma string e um número inteiro como entrada. Em seguida imprime a string
repetida o número de vezes informado (uma repetição por linha).
"""


def repeat_text(text, n):
	"""Retorna uma lista com `text` repetida `n` vezes.

	Lança ValueError se n for negativo e TypeError se n não for conversível para int.
	"""
	try:
		n = int(n)
	except Exception:
		raise TypeError('n deve ser um inteiro')

	if n < 0:
		raise ValueError('n deve ser não-negativo')

	result = []
	for _ in range(n):
		result.append(text)
	return result


if __name__ == '__main__':
	try:
		text = input('Digite uma string: ')
		raw_n = input('Digite um número inteiro: ')
		# valida e converte
		try:
			n = int(raw_n)
		except ValueError:
			print('Erro: o segundo valor deve ser um inteiro')
		else:
			if n < 0:
				print('Erro: n deve ser não-negativo')
			else:
				for _ in range(n):
					print(text)
	except Exception as e:
		print('Erro:', e)