import datetime

from account import *


class Day:
    """Stores current day/current user"""

    def __init__(self, Account):
        self.setDate()
        self.setAccount(Account)

    def getDate(self):
        return self.date

    def setDate(self):
        cur_date = datetime.datetime.now()
        self.date = cur_date.strftime("%x")

    def getAccount(self):
        return self.Account

    def setAccount(self, Account):
        self.Account = Account
