from abc import ABCMeta, abstractmethod


# Interface
class Wallet(metaclass=ABCMeta):

    @abstractmethod
    def pay(self):
        pass


class Bank(Wallet):
    def __init__(self):
        self.card = None
        self.account = None

    def __get_account(self):
        self.account = self.card
        return self.account

    def __actual_value(self):
        print(f"Banco:: Checando se a conta {self.__get_account()} tem saldo.")
        return True

    def set_card(self, card):
        self.card = card

    def pay(self):
        if self.__actual_value():
            print("Banco:: pagando o bar...")
            return True
        else:
            print("Banco:: Você não tem saldo suficiente!")
            return False


# Proxy
class DebitCard(Wallet):
    def __init__(self):
        self.bank = Bank()

    def pay(self):
        card = input('Proxy:: Informe o numero do cartão:')
        self.bank.set_card(card)
        return self.bank.pay()


class Cliente:
    def __init__(self):
        print('Cliente:: Quero comprar!')
        self.debit_card = DebitCard()
        self.bought = False

    def make_payment(self):
        self.bought = self.debit_card.pay()

    def __del__(self):
        if self.bought:
            print('Cliente:: Finalmente comprei!')
        else:
            print('Cliente:: Preciso de mais dinheiro')


if __name__ == "__main__":
    client = Cliente()
    client.make_payment()

