import click


def make_change(amount):
    # List of Polish coin denominations in descending order
    coins = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    # Dictionary to store the count of each coin
    change = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    # Convert amount to groszy
    amount_in_groszy = int(amount * 100)

    for coin in coins:
        while amount_in_groszy >= coin:
            amount_in_groszy -= coin
            change[coin] += 1

    # Print the result
    for coin, count in change.items():
        if count > 0:
            if coin >= 100:
                click.echo(f"{count} x {coin // 100} złoty")
            else:
                click.echo(f"{count} x {coin} groszy")

    return change


@click.command()
@click.option("--amount", default=1.00, help="Amount to give change for.")
def main(amount):
    """
    A function to return the least amount of coins given a change amount.
    """

    make_change(amount)


if __name__ == "__main__":

    main()
