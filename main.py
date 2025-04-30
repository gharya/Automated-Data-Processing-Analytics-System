from simulate_data import simulate_insurance_data, simulate_shipping_data
from merge_analyze import merge_and_analyze
from db import load_to_sqlite, query_database
from crypto_analytics import fetch_crypto_data, fetch_binance_data

def run_pipeline():
    print("1. Simulating data...")
    simulate_insurance_data("data/input/insurance.csv")
    simulate_shipping_data("data/input/shipping.csv")

    print("2. Merging and analyzing data...")
    merge_and_analyze()

    print("3. Loading data into SQLite and querying...")
    engine = load_to_sqlite()
    query_database(engine)

    print("4. Fetching cryptocurrency data...")
    fetch_crypto_data()
    fetch_binance_data()

if __name__ == "__main__":
    run_pipeline()