from click.testing import CliRunner
import unittest
from cli import cli

class CurrencyRateTests(unittest.TestCase):

    def test_get_rate_usd(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['rate', 'USD'])
        self.assertEqual(result.exit_code, 0)

    def test_get_rate_unknown(self):
        currency = 'UNKNOWN'
        runner = CliRunner()
        result = runner.invoke(cli, ['rate', currency])
        self.assertNotEqual(result.exit_code, 0)
        self.assertEqual(result.output, f'Currency {currency} not found!\n')

if __name__ == '__main__':
    unittest.main()