from customer import Customer
from bank import Bank

if __name__ == '__main__':
    ku_bank = Bank("KU Bank")
    alice = Customer(1, 1234, "Alice")
    bob = Customer(2, 2345, "Bob")

    ku_bank.add_customer(alice)
    ku_bank.add_customer(bob)

    print(  ku_bank.validate_customer(1, 1234)  )
    print(  ku_bank.validate_customer(5, 1234)  )
