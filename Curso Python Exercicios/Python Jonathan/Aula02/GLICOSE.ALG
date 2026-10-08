Algoritmo "Glicose"


Var
  glicose: real

Inicio
 escreva("Digite a medida da glicose: ")
 leia(glicose)
  se(glicose <= 100) entao
   escreval("Classificação: normal")
   senao
   se(glicose <=140) entao
   escreval("Classificação: elevada")
   senao
   escreval("Classsificação: Diabetes")
   fimse
  fimse

Fimalgoritmo