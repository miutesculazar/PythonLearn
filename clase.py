class GetAndPrint:
    def __init__(self, nr_cuv=2):
        self.cuv = ''
        self.nr_cuv = nr_cuv

    def getString(self):
        for i in range(self.nr_cuv):
            if i == self.nr_cuv - 1:
                self.cuv += input('Dati un cuvant: ') + '.'
            else:
                self.cuv += input('Dati un cuvant: ') + ' '

    def printString(self):
        out = self.cuv.upper()
        print(f'output: {out}')


class numar:

    def __init__(self, valoare):
        self.valoare = valoare

    def inaltime(self):
        print(self.valoare)


def main():
    # obj = GetAndPrint()
    # obj.getString()
    # obj.printString()

    eu = numar(2)
    tu = numar(3)

    eu.inaltime()
    tu.inaltime()


if __name__ == '__main__':
    main()
