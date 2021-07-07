# Cria nó
class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


#Classe da árvore B
class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    # Print the tree
    def print_tree(self, x, l=0):
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)
     
    # Busca por chave 
    def search_key(self, k, x=None):
      if x is not None:
        i = 0
        while i < len(x.keys) and k > x.keys[i][0]:
          i += 1
          if i < len(x.keys) and k == x.keys[i][0]:
            return (x, i)
          elif x.leaf:
            return None
          else:
            return self.search_key(k, x.child[i])
        else:
            return self.search_key(k, self.root)

    #Inserção da chave
    def insert_key(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert_key(0, root)
            self.split(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k) 


    # Inseri nó
    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    #diferencia os nós que são filhos ou não
    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

     

      
def main():
    #passando arquivos para o vetor
    print("\nAlgumas cidades que serão trabalhadas no decorrer do arquivo:\n")
    text_file = open("Municipio.csv", "r")
    lines = text_file.readlines()
    text_file.close()
    
    #buscar arquivo por letra (Não consegui achar pela primeira letra, mas sim qual contém pelo menos uma letra no nome)
    print("Busca pela letra 'S': ")
    df = pd.read_csv("Municipio.csv")
    print(df[df['Municipio'].str.contains('S')])

    B = BTree(3)

    B.insert(('c',4))
    B.insert(('c',5))
    B.insert(('c',6))
    
    #imprime a chave numerica e alfabetica
    print("\nChaves numéricas e alfabéticas:")
    B.print_tree(B.root)
   
    #busca 
    num = 8
    if B.search_key(num) is True:
      print("\n Chave numerica ",num," encontrada")
      print(lines[num])
    else:
      print("\nChave numerica ",num," não encontrada")
    
    
    

if __name__ == '__main__':
    main()
    
    
