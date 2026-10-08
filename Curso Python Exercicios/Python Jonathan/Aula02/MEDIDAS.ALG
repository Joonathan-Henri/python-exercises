Algoritmo "Medidas"

Var
A,B,C,areaQuadrado, areaTriangulo,areaTrapezio: real

Inicio
escreva("Digite a medida de A: ")
leia(A)
escreva("Digite a medida de B: ")
leia(B)
escreva("Digite a medida de C: ")
leia(C)

areaQuadrado <- A * A
areaTriangulo <- A * B / 2
areaTrapezio <-(A + B) * C / 2

escreval("Área do Qudrado = ", areaQuadrado:6:4)
escreval("Área do Triângulo = ", areaTriangulo:6:4)
escreval("Área do Trapézio = ", areaTrapezio:6:4)

Fimalgoritmo