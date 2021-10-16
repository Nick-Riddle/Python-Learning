class Value:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value - value * instance.commission


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.3)
new_account.amount = 25
print(new_account.amount)