# Создайте класс BankAccount с атрибутами client_id, client_first_name, client_last_name, balance и
# методами add() и withdraw(), при помощи которых можно пополнять счет и выводить средства со счета соответственно.
# Атрибут balance должен инициализироваться по умолчанию значением 0.0 и меняться при срабатывании
# методов add() и withdraw().


class BankAccount:
    client_id = 0

    def __init__(self, first_name, last_name):
        self.client_id = BankAccount.client_id
        BankAccount.client_id += 1
        self.client_first_name = first_name
        self.client_last_name = last_name
        self.balance = 0.0

    def add(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
