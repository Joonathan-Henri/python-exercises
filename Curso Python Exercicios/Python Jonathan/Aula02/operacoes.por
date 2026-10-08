programa {
  funcao inicio() {
    real a,b, soma, sub, multi, div

    escreva("Digite o primeiro número: ")
    leia(a)
    escreva("Digite o segundo número: ")
    leia(b)
    limpa()

    soma = a + b // o igual sozinho é  atribuição == é igual
    sub = a - b
    multi = a * b
    div = a / b
    
    escreva("\nA soma dos números é igual a: ", soma)
    escreva("\nA subtração dos números é igual a: ", sub)
    escreva("\nA multiplicação dos números é igual a: ", multi)
    escreva("\nA divisão dos números é igual a: ", div)

  }
}
