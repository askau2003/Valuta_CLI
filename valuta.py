import os
import argparse # CLI


import requests # API-call
from dotenv import load_dotenv

def main():
    load_dotenv()

    # Create parser
    parser = argparse.ArgumentParser(
        prog="Valuta Converter",
        description="Convert currency with your terminal"
    )

    # Makes it able to have multiple commands
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Set API-key
    key_parser = subparsers.add_parser("setkey", help="Set your API key")
    key_parser.add_argument("key", help="Your API key")

    # Convert currency
    valuta_parser = subparsers.add_parser("convert", help="Convert currencies")
    valuta_parser.add_argument("currency1", help="Convert from")
    valuta_parser.add_argument("currency2", help="Convert to")
    valuta_parser.add_argument("amount", help="Amount to convert")

    # Close parser
    args = parser.parse_args()

    # If command is --key, creates a .env file and write the API-key
    if args.command == "setkey":
        with open(".env","w", encoding="utf-8") as f:
            f.write("API_KEY=" + args.key)
    
    # If command is convert, make an api call to ExchangeRate-API
    elif args.command == "convert":
        load_dotenv() # Don't think its needed
        api_key = os.getenv("API_KEY")

        currency1 = args.currency1
        currency2 = args.currency2
        amount = args.amount

        url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{currency1}/{currency2}/{amount}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("Conversion result:", data["conversion_result"])
            print("Conversion rate:", data["conversion_rate"])
        else:
            print("status_code:", response.status_code)


# Program entrypoint
if __name__ == "__main__":
    main()