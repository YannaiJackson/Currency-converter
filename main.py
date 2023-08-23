import requests


def get_worth(currency):
    """
    accesses data in the API
    :param currency: worth vs dollar
    :return: a dict where the keys are rate abbreviations and the values are the value vs the dollar
    """
    response = requests.get("https://api.exchangerate.host/latest")
    json_data = response.json()
    currency_dict = json_data['rates']
    return currency_dict[currency]


# changing currency amount to USD
def base_currency(abbreviation, amount):
    """
    exchanges amount in currency chosen to amount in eur currency
    :param abbreviation: first currency abbreviation
    :param amount: amount to exchange
    :return: amount worth in eur
    """
    currency1 = get_worth(abbreviation)
    return amount/currency1


def conversion(abbreviation, amount_in_eur):
    """
    exchanges amount in eur to amount in chosen currency
    :param abbreviation: second currency abbreviation
    :param amount_in_eur: calculated in base_currency method
    :return: amount worth in second currency
    """
    # money times new currency
    currency2 = get_worth(abbreviation)
    return amount_in_eur*currency2


def main():
    """
    receives two abbreviation inputs and one amount input and summons other methods to calculate exchange
    :return: amount worth of first currency in second currency
    """
    abbreviation1 = input("enter first rate abbreviation: ").upper()
    amount = float(input("enter amount to exchange: "))
    amount_in_eur = base_currency(abbreviation1, amount)
    abbreviation2 = input("enter rate abbreviation to convert to: ").upper()
    result = conversion(abbreviation2, amount_in_eur)
    print(f'{amount} {abbreviation1} exchanges to {result} {abbreviation2}')


if __name__ == '__main__':
    main()

