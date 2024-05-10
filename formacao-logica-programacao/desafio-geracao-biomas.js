// Lê a quantidade de golpes informada pelo usuário. 
// O parseInt(()) vai converter os valores de entrada(string) para um valor numérico(Int).
const quantidadeGolpes = parseInt(gets());

// TODO: Defina aqui os tipos de minerais Carvao, Ferro, Diamante e Pedra
let minerais = ["Pedra", "Carvao", "Ferro", "Diamante"];

// Loop para cada golpe, de 1 até a quantidade informada
for (let i = 1; i <= quantidadeGolpes; i++) {
  // Calcula o índice do mineral usando o operador de módulo (%) para garantir que o índice esteja dentro do tamanho do array
  let minaIndex = i % minerais.length;
  
  // TODO: Agora exiba o índice i, concatene com o caractere ":", após, concatene com tipo de minerais[minaIndex]:
  print(i + ": " + minerais[minaIndex]);
}