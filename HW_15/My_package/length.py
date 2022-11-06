"""this length conversion module
"""
from prettytable import PrettyTable


def length(mile: int) -> str:
    """
    converts from miles to kilometers.
    @param mile: value in miles
    :return: text table with values in miles and kilometers

    ```
    +------+-----------+
    | mile | kilometer |
    +------+-----------+
    |  1   |   1.609   |
    +------+-----------+
    ```
    """

    result = mile * 1.609
    # kelvin_value = 5. / 9. * (fahrenheit - 32) + 273.15

    table = PrettyTable(['mile', 'kilometer'])
    table.add_row([mile, result])

    return table.get_string()


print(length(1))
