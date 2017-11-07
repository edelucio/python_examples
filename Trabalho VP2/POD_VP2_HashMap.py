class UserFactory(object):
    def __init__(self, number):
        self.users = []
        for i in range(number):
            self.users.append(self.usergenerate())

    def usergenerate(self):
        from random import randint, uniform

        userName = ""
        userNameLength = randint(3, 18)
        userHeight = round(uniform(0.50, 2.30), 2)

        vowel = ["a", "e", "i", "o", "u"]
        consonants = ["b", "c", "d", "f", "g", "h", "j", "l", "m",
                      "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
        vowelAndConsonants = vowel + consonants

        for i in range(userNameLength):
            if i == 0:
                userName = userName + \
                    vowelAndConsonants[randint(
                        0, len(vowelAndConsonants) - 1)]
            elif i > 0 and userName[i - 1] in vowel:
                userName = userName + \
                    consonants[randint(0, len(consonants) - 1)]
            elif i > 0 and userName[i - 1] in consonants:
                userName = userName + vowel[randint(0, len(vowel) - 1)]

        return User(userName, userHeight)


class User(object):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name, self.height


class HashMap(object):
    def __init__(self, size):
        self.size = size
        self.slots = []
        self.data = []

        for i in range(self.size):
            self.slots.append([])
            self.data.append([])

    def hashfunction(self, key):
        import hashlib
        key = key.encode('utf-8')
        key = int(hashlib.md5(key).hexdigest(), 16)
        while key > self.size - 1:
            key = key // self.size
        return key

    def _find(self, key):
        hashvalue = self.hashfunction(key)

        index = 0
        found = False
        for item in self.slots[hashvalue]:
            if key == item:
                found = True
                break

            index = index + 1

        return found, index

    def remove(self, key):
        result = None
        hashvalue = self.hashfunction(key)

        found, index = self._find(key)
        if found:
            self.slots[hashvalue].pop(index)
            result = self.data[hashvalue].pop(index)

        return result

    def get(self, key):
        result = None
        hashvalue = self.hashfunction(key)

        found, index = self._find(key)
        if found:
            result = self.data[hashvalue][index]

        return result

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def put(self, key, data):
        hashvalue = self.hashfunction(key)

        if key not in self.slots[hashvalue]:
            self.slots[hashvalue].append(key)
            self.data[hashvalue].append(data)
        else:
            index = 0
            for item in self.slots[hashvalue]:
                if key == item:
                    break
                index = index + 1

            self.data[hashvalue][index] = data


class MainProgram(object):
    usersHash = None

    def main():
        while True:
            print("\n ### M E N U ###\n")
            print(" 1 - Inserir usuários")
            print(" 2 - Pesquisar usuário")
            print(" 3 - Buscar usuário")
            print(" 4 - Listar slots")
            print(" 5 - Sair\n")

            choice = input(" Digite uma das opções: ")

            if choice == "1":
                MainProgram.inserirdados()
            elif choice == "2":
                if(MainProgram.usersHash != None):
                    MainProgram.pesquisarDados()
                else:
                    print("\n Não há sequer uma tabela hash criada.")
            elif choice == "3":
                if(MainProgram.usersHash != None):
                    MainProgram.buscarDados()
                else:
                    print("\n Não há sequer uma tabela hash criada.")
            elif choice == "4":
                if(MainProgram.usersHash != None):
                    MainProgram.mostrarDados()
                else:
                    print("\n Não há sequer uma tabela hash criada.")
            elif choice == "5":
                return False
            else:
                print("\n Opção inválida!")

    def inserirdados():
        numeroDeRegistros = int(
            input("\n Quantos registros deseja gerar e inserir? "))

        MainProgram.usersHash = HashMap(numeroDeRegistros)
        userFactory = UserFactory(numeroDeRegistros)

        for user in userFactory.users:
            MainProgram.usersHash.put(user.name, user)

        print("\n Dados criados e inseridos com sucesso!")

    def pesquisarDados():
        chaveApesquisar = input("\n Digite o nome do usuário: ")

        resultadoDaPesquisa = MainProgram.usersHash.get(chaveApesquisar)

        if (resultadoDaPesquisa != None):
            print("\n Usuário não encontrado nos registros!")
        else:
            print("\nDado não encontrado!")

    def buscarDados():
        chaveApesquisar = input("\n Digite o nome do usuário: ")

        resultadoDaPesquisa = MainProgram.usersHash.get(chaveApesquisar)

        if (resultadoDaPesquisa != None):
            print(" Nome do usuário: ", resultadoDaPesquisa.name + "\n",
                  "Altura do usuário: ", resultadoDaPesquisa.height)
        else:
            print("\n Usuário não encontrado!")

    def mostrarDados():
        print(MainProgram.usersHash.slots)


if __name__ == '__main__':
    MainProgram.main()
