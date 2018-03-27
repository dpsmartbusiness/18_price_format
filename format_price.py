import argparse


def format_price(price):
    try:
        price = float(price)
    except (TypeError, ValueError):
        return None
    if price.is_integer():
        format_string = ',.0f'
    else:
        format_string = ',.2f'
    return format(price, format_string).replace(',', ' ')


def create_parser():
    parser = argparse.ArgumentParser(
        description='Format number to price'
    )
    parser.add_argument(
        'input_number',
        help='User number that will need to formatting to price. '
             'Required input formats: digits.digits, digits, '
             'digits.(zeros or nothing)'
    )
    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    formated_price = format_price(args.input_number)
    if formated_price:
        print('\nFormated price: {}'.format(formated_price))
    else:
        print('\nINPUT FORMAT ERROR. Required price format see in help')