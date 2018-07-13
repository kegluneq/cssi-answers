#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance
        self.transactions = []

    def __str__(self):
        return "Account %s has balance $%d" % (self.label, self.balance)

    def withdraw(self, amount):
        # Returns True if the withdrawal was successful, false otherwise.
        if amount > self.balance:
            print("You can't withdraw more money than is the account.")
            return False
        elif amount < 0:
            print("You can't withdraw negative money. Stop trying to cheat.")
            return False

        self.balance -= amount
        self.transactions.append(Transaction("withdrawal", amount, None))
        return True

    def deposit(self, amount):
        # Returns True if the deposit was successful, false otherwise.
        if amount < 0:
            print("Why would you want to deposit negative money?")
            return False

        self.balance += amount
        self.transactions.append(Transaction("deposit", amount, None))
        return True

    def rename(self, new_label):
        # not new_label checks for entirely empty labels
        # new_label.isspace() makes sure that it's not only space characters
        if not new_label or new_label.isspace():
            print("You can't leave the account's label empty.")
        else:
            self.label = new_label

    def transfer(self, dest_account, amount):
        # Returns True if the transfer was successful, false otherwise
        if self.withdraw(amount):
            success = dest_account.deposit(amount)
            self.transactions.append(Transaction("transfer", amount, dest_account.label))
            return success
        return False

class Transaction(object):
    def __init__(self, transaction_type, amount, dest_account_label):
        self.time = time.time()
        self.type = transaction_type
        self.amount = amount
        self.dest_account_label = dest_account_label

    def __str__(self):
        description = "%s: %s" % (self.time, self.type)
        if self.type == "transfer":
            description += " to account '%s'" % self.dest_account_label
