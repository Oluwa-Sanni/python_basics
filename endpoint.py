import pandas as pd
import requests
import json
import logging

# Configuration
EXCEL_FILE = "requests.xlsx"
API_URL = "https://api.example.com/v1/transactions"
API_KEY = "your_api_key_here"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Logging setup
logging.basicConfig(
    filename="api_calls.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def call_post_endpoint():
    df = pd.read_excel(EXCEL_FILE)

    for index, row in df.iterrows():
        payload = {
            "customerId": row["customer_id"],
            "amount": row["amount"],
            "accountNumber": row["account_number"],
            "narration": row["narration"]
        }

        try:
            response = requests.post(
                API_URL,
                headers=HEADERS,
                data=json.dumps(payload),
                timeout=30
            )

            if response.status_code == 200 or response.status_code == 201:
                logging.info(f"SUCCESS | Row {index + 1} | Response: {response.text}")
            else:
                logging.error(
                    f"FAILED | Row {index + 1} | "
                    f"Status: {response.status_code} | Response: {response.text}"
                )

        except requests.exceptions.RequestException as e:
            logging.exception(f"ERROR | Row {index + 1} | {str(e)}")

if __name__ == "__main__":
    call_post_endpoint()
