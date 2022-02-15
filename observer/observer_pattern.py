from abc import ABCMeta, abstractmethod


# Assunto/Topico
class AgenciaNoticias:
    def __init__(self):
        self.__inscritos = []
        self.__ultima_noticia = None

    def inscrever(self, inscrito):
        self.__inscritos.append(inscrito)

    def desinscrever(self, inscrito=None):
        if not inscrito:
            return self.__inscritos.pop()
        else:
            return self.__inscritos.remove(inscrito)

    def notificar_todos(self):
        for subs in self.__inscritos:
            subs.notificar()

    def adicionar_noticia(self, noticia):
        self.__ultima_noticia = noticia

    def mostrar_noticia(self):
        return f"Noticia Urgente: {self.__ultima_noticia}"

    @property
    def inscritos(self):
        return [type(valor).__name__ for valor in self.__inscritos]


# Interface Observer
class TipoInscricao(metaclass=ABCMeta):
    @abstractmethod
    def notificar(self):
        pass


# Observador A
class InscritosSMS(TipoInscricao):
    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f"{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}")


# Observador A
class InscritosEmail(TipoInscricao):
    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f"{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}")


# Observador A
class InscritosOutroMeio(TipoInscricao):
    def __init__(self, agencia_noticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f"{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}")


if __name__ == '__main__':
    agencia_noticias = AgenciaNoticias()

    inscritos_sms = InscritosSMS(agencia_noticias)
    inscritos_email = InscritosEmail(agencia_noticias)
    inscritos_other = InscritosOutroMeio(agencia_noticias)

    print(f"Inscritos: {agencia_noticias.inscritos}")

    agencia_noticias.adicionar_noticia("Observer e um baita pattern!")
    agencia_noticias.notificar_todos()

    print(f"Descadastrado: {type(agencia_noticias.desinscrever()).__name__}")
    print(f"Inscritos: {agencia_noticias.inscritos}")
