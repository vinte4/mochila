class Ingresso:
    codi = 1

    def __init__(self, valor):
        self.cod = Ingresso.codi
        Ingresso.codi += 1
        self.valor = valor
        self.status = 'disponível'

    def vender(self):
        self.status = 'vendido'

    def __str__(self) -> str:
        imp = f' N.: {self.cod}\nStatus: {self.status}\nValor: {self.valor}'
        return imp


a = Ingresso(10)
print(a)

b = Ingresso(20)
print(b)


class Camarote(Ingresso):
    def __init__(self, valor, valorextra):
        super().__init__(valor)
        self.valor2 = valor + valorextra

    def __str__(self):
        imp = f' N.: {self.cod}\nStatus: {self.status}\nValor: {self.valor2}'
        return imp


c = Camarote(10, 1)
print(c)


class Show:
    aux = 0
    auxi = 0

    def __init__(self, artista, data, local):
        self.artista = artista
        self.data = data
        self.local = local
        self.ingresso = list()
        self.camarote = list()

    def __str__(self):
        impr = f' Informações do Show\nArtista: {self.artista}\nData: {self.data}\nLocal: {self.local}'
        return impr

    def gerarIngressos(self, qtde, valor, tipo=0):
        if tipo == 0:
            for i in range(qtde):
                self.ingresso.append(Ingresso(valor))
        else:
            valorextra = float(input('Valor adicional: '))
            for i in range(qtde):
                self.camarote.append(Camarote(valor, valorextra))

    def venderIngresso(self, qtde, tipo=0):
        if tipo == 0:
            for c in range(qtde):
                self.ingresso[Show.aux].vender()
                Show.aux += 1
        else:
            for c in range(qtde):
                self.camarote[Show.auxi].vender()
                Show.auxi += 1

    def relatorioIngresso(self):
        for c in range(len(self.ingresso)):
            print(self.ingresso[c])

    def relatorioCamarote(self):
        for c in range(len(self.camarote)):
            print(self.camarote[c])


d = Show('Lina', '30 de setembro de 2022', 'Aracaju-SE')
print()
print(d)
print()
d.gerarIngressos(3, 1)
print()
d.relatorioIngresso()
print()
d.gerarIngressos(5, 1, 1)
print()
d.relatorioCamarote()
print()

d.venderIngresso(1)

d.venderIngresso(2, 1)

d.relatorioIngresso()
print()
d.relatorioCamarote()
print()
print()
d.venderIngresso(1)
d.relatorioIngresso()
print()
d.venderIngresso(1, 1)
d.relatorioCamarote()
