"""Descrição: vamos solicitar como entrada dois números e depois vamos realizar
uma operação simples entre eles. O script valida entradas (aceita vírgula ou
ponto como separador decimal), trata divisão por zero e aceita as operações:
  +  soma
  -  subtração
  *  multiplicação
  /  divisão
  ** potência (ou ^ como atalho)

Uso: execute o script e siga as instruções interativas.
"""

def parse_number(text: str):
	"""Converte uma string para float aceitando vírgula ou ponto.

	Retorna um float ou levanta ValueError se não for um número válido.
	"""
	text = text.strip().replace(',', '.')
	return float(text)


def input_number(prompt: str):
	while True:
		s = input(prompt)
		try:
			return parse_number(s)
		except ValueError:
			print("Entrada inválida. Por favor digite um número (ex: 3.14 ou 2,5).")


def input_operation(prompt: str):
	valid = ['+', '-', '*', '/', '**', '^']
	while True:
		op = input(prompt).strip()
		if op in valid:
			return op
		print(f"Operação inválida. Escolha entre: {', '.join(valid)}")


def compute(a: float, b: float, op: str):
	if op == '+':
		return a + b
	if op == '-':
		return a - b
	if op == '*':
		return a * b
	if op == '/':
		if b == 0:
			raise ZeroDivisionError('Divisão por zero')
		return a / b
	if op == '**' or op == '^':
		return a ** b
	raise ValueError('Operação desconhecida')


def main():
	print('Calculadora simples - insira dois números e uma operação')
	a = input_number('Digite o primeiro número: ')
	b = input_number('Digite o segundo número: ')
	op = input_operation('Digite a operação (+, -, *, /, ** ou ^): ')
	try:
		resultado = compute(a, b, op)
	except ZeroDivisionError:
		print('Erro: divisão por zero não é permitida.')
		return
	except Exception as e:
		print(f'Erro ao calcular: {e}')
		return

	# Formata o resultado: se for inteiro exibe sem casas decimais
	if isinstance(resultado, float) and resultado.is_integer():
		resultado = int(resultado)
	print(f'Resultado: {a} {op} {b} = {resultado}')


if __name__ == '__main__':
	main()