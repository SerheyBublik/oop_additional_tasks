"""
Напишите класс BankAccount, имеющий следующие свойства и методы:

- __init__(self, balance): конструктор, принимающий начальный баланс счета
- balance: свойство, которое возвращает текущий баланс счета
- deposit(self, amount): метод, который позволяет внести деньги на счет
- withdraw(self, amount): метод, который позволяет снять деньги со счета
- close(self): метод, который закрывает счет и возвращает оставшиеся на нем деньги

Для свойства balance используйте декоратор @property.
"""


class BankAccount:

    def __init__(self, balance: int):
        self.start_balance = balance

    @property
    def balance(self):
        return self.balance

    def deposit(self, amount: int):
        balance = self.balance + amount
        return balance

    def withdraw(self, amount: int):
        balance = self.start_balance - amount
        return balance

    def close(self):
        balance = self.balance - self.balance
        return balance


account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit(500)
print(account.balance)  # 1500

account.withdraw(200)
print(account.balance)  # 1300

account.close()
print(account.balance)  # 0
