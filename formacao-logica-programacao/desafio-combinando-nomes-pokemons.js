//Desafio de código: Combinando Nomes e Pokémons

function combinandoNomesPokemons(palavra) {
    // Criando a parte final do nome do Pokémon
    let sufixo = "saur";
    
    // Combinando a parte inicial com o sufixo para formar o nome completo do Pokémon
    let palavraPokemon = palavra + sufixo;
    
    // Retornando o nome completo do Pokémon
    return palavraPokemon;
  }
  // Entrada da palavra usando o gets():
  var nomeEntrada = gets();
  
  // Chamando a função "combinandoNomesPokemons" com o nome pokemon informado e armazenando o resultado na variável "palavraGerada":
  var palavraGerada = combinandoNomesPokemons(nomeEntrada);
  
  // Exibindo a palavra gerada:
  print(palavraGerada);