import json
import random
import string
from pathlib import Path


class Bank:

    database = "data.json"

    def __init__(self):
        if Path(self.database).exists():
            with open(self.database, "r") as f:
                self.data = json.load(f)
        else:
            self.data = []

    def update(self):
        with open(self.database, "w") as f:
            json.dump(self.data, f, indent=4)

    def generate_account(self):

        while True:
            alpha = ''.join(random.choices(string.ascii_letters, k=3))
            num = ''.join(random.choices(string.digits, k=3))
            sp = random.choice("!@#$%")

            acc = alpha + num + sp

            if not any(i["Account Number"] == acc for i in self.data):
                return acc

    def create_account(self, name, age, email, pin):

        if age < 18 or len(str(pin)) != 4:
            return "Invalid age or PIN"

        info = {
            "name": name,
            "age": age,
            "email": email,
            "Pin": pin,
            "Account Number": self.generate_account(),
            "Balance": 0
        }

        self.data.append(info)
        self.update()

        return info

    def find_user(self, acc, pin):

        for i in self.data:
            if i["Account Number"] == acc and i["Pin"] == pin:
                return i
        return None

    def deposit(self, acc, pin, amount):

        user = self.find_user(acc, pin)

        if not user:
            return "User not found"

        user["Balance"] += amount
        self.update()

        return user["Balance"]

    def withdraw(self, acc, pin, amount):

        user = self.find_user(acc, pin)

        if not user:
            return "User not found"

        if user["Balance"] < amount:
            return "Insufficient balance"

        user["Balance"] -= amount
        self.update()

        return user["Balance"]

    def delete(self, acc, pin):

        user = self.find_user(acc, pin)

        if not user:
            return "User not found"

        self.data.remove(user)
        self.update()

        return "Account deleted"