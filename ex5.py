class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return "Som do animal"

    def apresentar(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return "Miau!"

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return "Au au!"

def fala_animal(a: Animal):
    return a.falar()

def main():
    user = input("Digite G para gato e C para cachorro: ").upper().strip()
    nome = input("Digite o nome do animal: ")
    idade = input("Digite a idade do animal: ")
    if user == "G":
        g = Gato(nome, idade)
        print(fala_animal(g))
        print(g.apresentar())
    elif user == "C":
        c = Cachorro(nome, idade)
        print(fala_animal(c))
        print(c.apresentar())
    else:
        print("Animal não detectado!")

if __name__ == "__main__":
    main()