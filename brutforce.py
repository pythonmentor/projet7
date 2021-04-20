import csv
from collections import defaultdict
from itertools import product

MAX_COST = 500


def get_data(path):
    """Loads the data from a CSV file."""
    data = defaultdict(list)
    with open(path) as csvfile:
        for line in csv.DictReader(csvfile):
            name = line['name']
            price = int(line['price'])
            profit = price * int(line['profit']) / 100
            data['name'].append(name)
            data['price'].append(price)
            data['profit'].append(profit)
    return data


def combine(data):
    """Iterates over all the possible combinations of the data."""
    names = product(*[('', name) for name in data['name']])
    prices = product(*[(0, price) for price in data['price']])
    profits = product(*[(0, profit) for profit in data['profit']])
    yield from zip(names, prices, profits)


def main():
    """Main entry point."""
    opt = {'actions': None, 'cost': 0, 'profit': 0}
    for actions, prices, profits in combine(get_data('data/dataset-test.csv')):
        cost = sum(prices)
        profit = sum(profits)
        if cost <= MAX_COST and profit > opt['profit']:
            opt['actions'] = actions
            opt['cost'] = cost
            opt['profit'] = profit

    print(
        "La combinaison idéale est:\n"
        f" - actions : {', '.join(name for name in opt['actions'] if name)}\n"
        f" - prix total : {opt['cost']} EUR\n"
        f" - profit total : {opt['profit']:.2f} EUR\n"
    )


if __name__ == "__main__":
    main()