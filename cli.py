import click
import requests

# Define a list of supported currencies (you can add more)
SUPPORTED_CURRENCIES = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'KES', 'BTS', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN',
    'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD',
    'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNH', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD',
    'EEK', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD',
    'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS',
    'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD',
    'MMK', 'MNT', 'MOP', 'MRO', 'MRU', 'MTL', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR',
    'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR',
    'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'SSP', 'STD', 'STN', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND',
    'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU',
    'XCD', 'XDR', 'XOF', 'XPD', 'XPF', 'XPT', 'YER', 'ZAR', 'ZMK', 'ZMW']

# Add your Open Exchange Rates API key here
API_KEY = '64c5d43b9ef448918d7c9eab33e9d291'
BASE_URL = 'https://openexchangerates.org/api/latest.json'

# Default base currency
DEFAULT_BASE_CURRENCY = 'USD'

@click.group()
def cli():
    '''
    CLI to work with currency rates
    '''
    pass

@click.command(name='list-currencies', help="List supported currencies")
def list_currencies():
    '''
    Lists supported currencies
    '''
    click.echo("Supported Currencies:")
    for currency in SUPPORTED_CURRENCIES:
        click.echo(currency)

@click.command(name='set-default-currency', help="Set a default currency for conversions")
@click.argument('currency')
def set_default_currency(currency):
    '''
    Set a default currency for conversions
    '''
    if currency not in SUPPORTED_CURRENCIES:
        click.echo(f'Currency {currency} is not supported.')
        return
    global DEFAULT_BASE_CURRENCY
    DEFAULT_BASE_CURRENCY = currency
    click.echo(f"Default currency set to {currency}")

@click.command(name='rate', help="Display currency rate for a single currency")
@click.argument('currency')
def display_currency_rate(currency):
    '''
    Display currency rate
    '''
    if currency not in SUPPORTED_CURRENCIES:
        click.echo(f'Currency {currency} is not supported.')
        return

    # Fetch exchange rate data for the base currency
    params = {
        'app_id': API_KEY,
        'base': DEFAULT_BASE_CURRENCY,
    }
    result = requests.get(f'{BASE_URL}?base={DEFAULT_BASE_CURRENCY}', params=params)
    
    if result.status_code != 200:
        click.echo(f'Error fetching exchange rates.')
        return

    result_dict = result.json()

    if 'rates' in result_dict:
        if currency in result_dict['rates']:
            rate = result_dict['rates'][currency]
            click.echo(f'1 {DEFAULT_BASE_CURRENCY} = {rate} {currency}')
        else:
            click.echo(f'Exchange rate not found for {currency}')
    else:
        click.echo(f'Error fetching exchange rates.')

@click.command(name='convert', help="Convert a currency amount to another currency,eg: cli convert 100 USD EUR")

@click.argument('amount', type=float)
@click.argument('from_currency')
@click.argument('to_currency')
def convert_currency(amount, from_currency, to_currency):
    '''
    Convert a currency amount
    '''
    if from_currency not in SUPPORTED_CURRENCIES or to_currency not in SUPPORTED_CURRENCIES:
        click.echo('One or both of the specified currencies are not supported.')
        return

    if from_currency == to_currency:
        click.echo('Cannot convert between the same currencies.')
        return

    # Fetch exchange rate data for the base currency
    params = {
        'app_id': API_KEY,
        'base': DEFAULT_BASE_CURRENCY,
    }
    result = requests.get(f'{BASE_URL}?base={DEFAULT_BASE_CURRENCY}', params=params)
    
    if result.status_code != 200:
        click.echo(f'Error fetching exchange rates.')
        return

    result_dict = result.json()

    if 'rates' in result_dict:
        if from_currency in result_dict['rates'] and to_currency in result_dict['rates']:
            rate_from = result_dict['rates'][from_currency]
            rate_to = result_dict['rates'][to_currency]
            converted_amount = amount * (rate_to / rate_from)
            click.echo(f'{amount} {from_currency} = {converted_amount} {to_currency}')
        else:
            click.echo(f'Exchange rate not found for one or both of the specified currencies.')
    else:
        click.echo(f'Error fetching exchange rates.')

# Add the commands to the CLI group
cli.add_command(list_currencies)
cli.add_command(set_default_currency)
cli.add_command(display_currency_rate)
cli.add_command(convert_currency)