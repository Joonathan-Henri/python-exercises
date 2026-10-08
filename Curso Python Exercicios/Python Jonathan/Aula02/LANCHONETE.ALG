Algoritmo "Lanchonete"

Var
Cod, qtd: inteiro
vlPago: real

Inicio
  escreva("Digite o código do produto: ")
  leia(Cod)
  escreva("Quantidade comprada: ")
  leia(qtd)
  
  escolha Cod
  caso 1
     vlPago <- 5 * qtd
  caso 2
     vlPago <- 3.5 * qtd
  caso 3
     vlPago <- 4.8 * qtd
  caso 4
      vlPago <- 8.9 * qtd
  caso 5
      vlPago <- 7.32 * qtd
  fimescolha

  escreval ("Valor a pagar: R$ ", vlPago:4:2)

Fimalgoritmo