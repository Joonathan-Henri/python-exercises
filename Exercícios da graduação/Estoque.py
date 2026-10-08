
ARQUIVO_ESTOQUE = "estoqueTay.txt"   # um produto por linha: nome;preco;quantidade
ARQUIVO_BACKUP = "estoqueMatheus.bak"

def carregar_estoque(caminho=ARQUIVO_ESTOQUE):
    estoque = []
    try:
        
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo.readlines():
                if not linha.strip():          # ignora linha em branco no fim
                    continue
                nome, preco, qtd = linha.strip().split(";")
                estoque.append({
                    "nome": nome,
                    "preco": float(preco),     # "3.5"  -> 3.5  (senão vira texto)
                    "quantidade": int(qtd),    # "100"  -> 100
                })
    except FileNotFoundError:
        # 1ª execução: o arquivo ainda não existe — o sistema NÃO pode quebrar
        print("(estoqueTay.txt não encontrado — iniciando estoque vazio)")
    return estoque

def salvar_estoque(estoque, caminho=ARQUIVO_ESTOQUE):

    with open(caminho, "w", encoding="utf-8") as arquivo:
        for p in estoque:

            arquivo.write(f'{p["nome"]};{p["preco"]};{p["quantidade"]}\n')


def backup_arquivo(origem=ARQUIVO_ESTOQUE, destino=ARQUIVO_BACKUP):
    try:
        with open(origem, "rb") as arq_origem:          # rb = ler bytes crus
            with open(destino, "wb") as arq_destino:    # wb = gravar bytes

                while chunk := arq_origem.read(4096):
                    arq_destino.write(chunk)
        print(f"Backup criado: {destino}")
    except FileNotFoundError:
        print(f"Origem não encontrada: {origem} (salve o estoque antes).")


    # ---------------------------------------------------------------------------
# BLOCO 2 — ENTRADA VALIDADA (Capítulo 6)
# Toda leitura do teclado passa por try/except: usuário digita bobagem,
# o sistema avisa e pede de novo — nunca morre com traceback.
# ---------------------------------------------------------------------------
 
def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Erro: o campo não pode ficar vazio. Tente novamente.")


def ler_float(mensagem):

    while True:
        entrada = input(mensagem).strip()
        try:
            valor = float(entrada.replace(",", "."))
            if valor < 0:
                print("Erro: o valor não pode ser negativo.")
                continue
            return valor
        except ValueError:
            print(f'Erro: "{entrada}" não é um número válido. Ex.: 79,90')


def ler_int(mensagem):
    while True:
        entrada = input(mensagem).strip()
        try:
            valor = int(entrada)
            if valor < 0:
                print("Erro: a quantidade não pode ser negativa.")
                continue
            return valor
        except ValueError:
            print(f'Erro: "{entrada}" não é um número inteiro. Ex.: 10')


# ---------------------------------------------------------------------------
# BLOCO 3 — OPERAÇÕES DO ESTOQUE
# Cada função altera a lista e o menu salva em disco logo em seguida
# (salvar a cada mudança: queda de energia não avisa).
# ---------------------------------------------------------------------------
 
def buscar_produto(estoque, nome):
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            return produto
    return None
 
 
def cadastrar_produto(estoque):
    """Opção 1 — valida duplicidade antes de inserir."""
    print("\n--- Cadastro de produto ---")
    nome = ler_texto("Nome do produto: ")
    if ";" in nome:
        # ";" é o separador do arquivo — permitir aqui corromperia o estoque.txt
        print('Erro: o nome não pode conter ";".')
        return
    if buscar_produto(estoque, nome):                 # trava duplicado
        print(f'Erro: "{nome}" já está cadastrado. Use a opção 3 para alterar.')
        return
    preco = ler_float("Preço unitário (R$): ")
    qtd = ler_int("Quantidade inicial: ")
    estoque.append({"nome": nome, "preco": preco, "quantidade": qtd})
    print(f'Produto "{nome}" cadastrado com sucesso!')
 
 
def listar_produtos(estoque):
    """Opção 2 — tabela alinhada com f-strings."""
    print("\n--- Produtos em estoque ---")
    if not estoque:
        print("(estoque vazio)")
        return
    print(f'{"Nome":<20}{"Preço (R$)":>12}{"Qtd":>8}{"Subtotal":>14}')
    for p in estoque:
        subtotal = p["preco"] * p["quantidade"]
        print(f'{p["nome"]:<20}{p["preco"]:>12.2f}{p["quantidade"]:>8}{subtotal:>14.2f}')
 
 
def atualizar_quantidade(estoque):
    """Opção 3 — entrada/saída de mercadoria (substitui a quantidade)."""
    print("\n--- Atualizar quantidade ---")
    nome = ler_texto("Nome do produto: ")
    produto = buscar_produto(estoque, nome)
    if produto is None:
        print(f'Erro: "{nome}" não encontrado no estoque.')
        return
    print(f'Quantidade atual de "{produto["nome"]}": {produto["quantidade"]}')
    produto["quantidade"] = ler_int("Nova quantidade: ")
    print("Quantidade atualizada!")
 
 
def remover_produto(estoque):
    """Opção 4 — pede confirmação antes de remover."""
    print("\n--- Remover produto ---")
    nome = ler_texto("Nome do produto: ")
    produto = buscar_produto(estoque, nome)
    if produto is None:
        print(f'Erro: "{nome}" não encontrado no estoque.')
        return
    confirma = input(f'Confirma remover "{produto["nome"]}"? (s/n): ').strip().lower()
    if confirma == "s":
        estoque.remove(produto)
        print("Produto removido.")
    else:
        print("Remoção cancelada.")
 
 
def valor_total(estoque):
    """Opção 5 — Capítulo 5 em ação: lambda + map + sum em uma linha.
 
    Equivale ao for que acumula subtotais, mas no estilo funcional:
    map aplica a lambda em cada produto; sum soma o resultado.
    """
    total = sum(map(lambda p: p["preco"] * p["quantidade"], estoque))
    print(f"\nValor total do estoque: R$ {total:.2f}")

# ---------------------------------------------------------------------------
# BLOCO 4 — MENU PRINCIPAL
# Laço infinito + try/except: opção inválida nunca derruba o sistema.
# ---------------------------------------------------------------------------
 
def exibir_menu():
    print("\n========= SISTEMA DE ESTOQUE =========")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar quantidade")
    print("4 - Remover produto")
    print("5 - Valor total do estoque")
    print("6 - Gerar backup")
    print("0 - Sair")
    print("======================================")
 
 
def main():
    # O sistema ACORDA lembrando: carrega o disco antes do menu (Cap. 7)
    estoque = carregar_estoque()
    print(f"{len(estoque)} produto(s) carregado(s) do disco.")
 
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
 
        if opcao == "1":
            cadastrar_produto(estoque)
            salvar_estoque(estoque)        # salva a CADA mudança
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            atualizar_quantidade(estoque)
            salvar_estoque(estoque)
        elif opcao == "4":
            remover_produto(estoque)
            salvar_estoque(estoque)
        elif opcao == "5":
            valor_total(estoque)
        elif opcao == "6":
            backup_arquivo()
        elif opcao == "0":
            salvar_estoque(estoque)        # garantia final antes de sair
            print("Estoque salvo. Até a próxima!")
            break
        else:
            # Opção inválida: avisa e volta ao menu — sem traceback
            print(f'Opção inválida: "{opcao}". Digite um número de 0 a 6.')
 
 
# Só executa o menu quando o arquivo é rodado diretamente
# (permite importar as funções em outro módulo/teste sem abrir o menu)
if __name__ == "__main__":
    main()