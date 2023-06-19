import re

from models import Information
from view import Window


class Controller:
    def __init__(self) -> None:
        self.view = Window()
        self.model = Information()

    def start(self):
        self.view.set_on_click(self.process_user_message)
        self.view.show()

    def process_user_message(self):

        information = list(self.view.get_information())
        details = information[0]
        date = information[1]
        checkbox = information[2]
        first_account_number = self.model.number_of_account()

        total = self.check_matching(details)

        account_number = self.get_account_number(
            checkbox, date, first_account_number,
        )

        self.model.add_to_table(total, details, date, account_number)
        self.view.set_information_of_last_bill(account_number, details)

    @staticmethod
    def check_matching(details):
        order = 0
        lines = details.split("\n")

        for line in lines:
            pattern_for_costs = re.compile("(\\d+) (по) (\\d+)")
            match = pattern_for_costs.match(line)
            if match:
                count = int(match[1])
                cost = int(match[3])
                order = order + (count * cost)
        total = order
        return total

    @staticmethod
    def get_account_number(checkbox, date, first_account_number):
        if checkbox:
            account_number = first_account_number
            print(account_number)
        elif date.year == 2021:
            account_number = 0
        else:
            account_number = first_account_number + 1
            print(account_number)
        return account_number
