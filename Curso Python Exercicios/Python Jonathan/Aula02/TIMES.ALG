Algoritmo "Times"


Var
 time: caractere

Inicio
 escreva("Digite o nome do time de futebol: ")
 leia(time)
 
 se(time = "Flamengo")ou(time ="Fluminense")ou(time = "Vasco")ou(time = "Botafogo") entao
    escreval("É um time CARIOCA!")
    
senao
   se(time = "São Paulo")ou(time ="Palmeiras")ou(time = "Santos")ou(time = "Corinthians") entao
    escreval("É um time PAULISTA!")
  senao
    escreval("Esse time não está nos nossos cadastros")
   fimse
 fimse


Fimalgoritmo