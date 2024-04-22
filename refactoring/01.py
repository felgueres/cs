import locale
from decimal import Decimal

plays = {
    "hamlet": {"name": "Hamlet", "type": "tragedy"},
    "as-like": {"name": "As You Like It", "type": "comedy"},
    "othello": {"name": "Othello", "type": "tragedy"},
}

invoices = [
    {
        "customer": "BigCo",
        "performances": [
            {"playID": "hamlet", "audience": 35},
            {"playID": "othello", "audience": 40},
            {"audience": 55, "playID": "as-like"},
        ],
    }
]

def format_currency(amount):
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
    return locale.currency(Decimal(amount), grouping=True)

def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f"Statement for {invoice['customer']}\n"

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]
        this_amount = 0

        if play["type"] == "tragedy":
            this_amount = 40000
            if perf["audience"] > 30:
                this_amount += 1000 * (perf["audience"] - 30)
        elif play["type"] == "comedy":
            this_amount = 30000
            if perf["audience"] > 20:
                this_amount += 10000 + 500 * (perf["audience"] - 20)
            this_amount += 300 * perf["audience"]
        else:
            raise ValueError(f"unknown type: {play['type']}")

        volume_credits += max(perf["audience"] - 30, 0)
        result += f"{play['name']}: {format_currency(this_amount / 100)} ({perf['audience']} seats)\n"
        total_amount += this_amount
    result += f"Amount owed is {format_currency(total_amount / 100)}\n"
    result += f"You earned {volume_credits} credits\n"
    return result
