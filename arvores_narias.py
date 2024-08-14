class No:
    def __init__(self, chave):
        # Inicializa um nó com uma chave e referências para o primeiro filho e próximo irmão
        self.chave = chave
        self.primFilho = None
        self.proxIrmao = None

class ArvoreNAria:
    def __init__(self, chave_raiz):
        # Inicializa a árvore com um nó raiz usando a chave fornecida
        self.raiz = self.criar_novo_no(chave_raiz)
        print(f"Inicialização: Nó raiz com chave {chave_raiz} criado.")

    def criar_novo_no(self, chave):
        # Cria e retorna um novo nó com a chave especificada
        return No(chave)

    def inicializa(self, chave_raiz):
        # Reinicializa a árvore com uma nova chave de raiz
        self.raiz = self.criar_novo_no(chave_raiz)
        print(f"Inicialização: Nó raiz com chave {chave_raiz} criado.")

    def busca(self, chave, no):
        # Busca um nó com a chave especificada na árvore a partir do nó fornecido
        if no is None:
            return None
        if no.chave == chave:
            return no
        filho = no.primFilho
        while filho:
            # Recursivamente busca nos filhos do nó atual
            resultado = self.busca(chave, filho)
            if resultado:
                return resultado
            filho = filho.proxIrmao
        return None

    def insere(self, chave_pai, nova_chave):
        # Insere um novo nó como filho do nó com a chave_pai especificada
        pai = self.busca(chave_pai, self.raiz)
        if not pai:
            print(f"Inserção falhou: Nó pai com chave {chave_pai} não encontrado.")
            return False
        novo_no = self.criar_novo_no(nova_chave)
        if not pai.primFilho:
            # Se o nó pai não tem filhos, o novo nó se torna o primeiro filho
            pai.primFilho = novo_no
        else:
            # Se o nó pai já tem filhos, adiciona o novo nó como o último irmão
            filho = pai.primFilho
            while filho.proxIrmao:
                filho = filho.proxIrmao
            filho.proxIrmao = novo_no
        print(f"Inserção: Nó com chave {nova_chave} inserido como filho de {chave_pai}.")
        return True

    def exibir(self, no, nivel=0):
        # Exibe a árvore de forma hierárquica começando do nó fornecido
        if no is None:
            return
        print(" " * nivel * 2, no.chave)  # Indenta de acordo com o nível do nó
        filho = no.primFilho
        while filho:
            self.exibir(filho, nivel + 1)
            filho = filho.proxIrmao

    def remover(self, chave):
        # Remove o nó com a chave especificada, ajustando a árvore conforme necessário
        if self.raiz.chave == chave:
            # Caso especial: remoção da raiz
            self.raiz = None
            print(f"Remoção: Nó raiz com chave {chave} removido.")
            return True
        return self._remover(self.raiz, chave)

    def _remover(self, no, chave):
        # Método auxiliar recursivo para remover um nó com a chave especificada
        if no is None:
            return False
        pai = None
        filho = no.primFilho
        while filho:
            if filho.chave == chave:
                # Encontrou o nó a ser removido
                if pai:
                    pai.proxIrmao = filho.proxIrmao
                else:
                    no.primFilho = filho.proxIrmao
                if filho.primFilho:
                    # Se o nó removido tem filhos, promove o primeiro filho como novo filho principal
                    if pai:
                        pai.proxIrmao = filho.primFilho
                    else:
                        no.primFilho = filho.primFilho
                    ultimo_filho = filho.primFilho
                    while ultimo_filho.proxIrmao:
                        # Conecta o último filho à lista de irmãos restantes
                        ultimo_filho = ultimo_filho.proxIrmao
                    ultimo_filho.proxIrmao = filho.proxIrmao
                print(f"Remoção: Nó com chave {chave} removido.")
                return True
            pai = filho
            filho = filho.proxIrmao
        filho = no.primFilho
        while filho:
            if self._remover(filho, chave):
                return True
            filho = filho.proxIrmao
        return False

if __name__ == "__main__":
    arvore = ArvoreNAria(8)
    arvore.insere(8, 15)
    arvore.insere(8, 23)
    arvore.insere(8, 2)
    arvore.insere(15, 20)
    arvore.insere(15, 10)
    arvore.insere(15, 28)
    arvore.insere(2, 36)
    arvore.insere(2, 7)  # Inserindo 7 como filho do nó 2, não do 36

    print("Árvore N-ária:")
    arvore.exibir(arvore.raiz)

    print("\nBusca pelo nó com chave 10:")
    no = arvore.busca(10, arvore.raiz)
    if no:
        print("Nó encontrado:", no.chave)
    else:
        print("Nó não encontrado.")

    print("\nRemoção do nó com chave 36:")
    if arvore.remover(36):
        print("Nó removido com sucesso.")
    else:
        print("Nó não encontrado para remoção.")

    print("\nÁrvore após remoção:")
    arvore.exibir(arvore.raiz)
