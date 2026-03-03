# Valuta_CLI
**Python CLI for valuta conversion**  
*Mandatory 1 – Python, Spring 2026*

## Requirements
- Git  
- Python 3.14  
- Visual Studio Code or another code editor

## Setup
1. **Clone repository**  
   git clone https://github.com/askau2003/Valuta_CLI  
   code Valuta_CLI/

2. **Create and activate a virtual environment**  
   `python -m venv .venv`  
   Windows: `.venv\Scripts\activate`  
   macOS/Linux: `source .venv/bin/activate`

3. **Install dependencies**  
   pip install -r requirements.txt

4. **Get your API-key**  
    Get a free API key from [ExchangeRate API](https://www.exchangerate-api.com)

5. **Setup your API-key**  
   `python valuta.py --key {API_KEY}`

## Usage
**Run the following command to convert currency:**  
`python valuta.py convert {from_currency} {to_currency} {amount}`

**Example:**  
`python valuta.py convert EUR DKK 100`

**Output:**  
Conversion result: 746.33  
Conversion rate: 7.4633
