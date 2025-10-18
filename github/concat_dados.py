"""Pequeno utilitário para concatenar dois dados recebidos do usuário.

Esta versão provê:
- função `concatena(a, b)` que converte os valores para string e retorna a concatenação;
- execução interativa quando o módulo é executado como script;
- testes simples com `doctest` e verificação mínima via `__main__`.
"""

from typing import Any


def concatena(a: Any, b: Any) -> str:
	"""Concatena dois valores convertendo-os para string.

	Exemplos:

	>>> concatena('ola', ' mundo')
	'ola mundo'
	>>> concatena(1, 2)
	'12'
	>>> concatena(None, True)
	'NoneTrue'
	"""
	return str(a) + str(b)


def main() -> None:
	"""Modo interativo simples: pede dois valores e mostra a concatenação."""
	print('Digite dois valores para concatenar (pressione Enter após cada um):')
	try:
		a = input('Primeiro valor: ')
		b = input('Segundo valor: ')
	except (KeyboardInterrupt, EOFError):
		print('\nEntrada interrompida pelo usuário.')
		return

	resultado = concatena(a, b)
	print('\nResultado da concatenação:')
	print(resultado)


if __name__ == '__main__':
	# Executa um teste rápido de sanidade e em seguida o modo interativo
	import doctest

	failed, _ = doctest.testmod()
	if failed:
		print(f"Alguns testes falharam: {failed}")
	main()
