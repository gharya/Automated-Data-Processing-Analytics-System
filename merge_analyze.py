import pandas as pd
import os

def merge_and_analyze():
    insurance = pd.read_csv("data/input/insurance.csv")
    shipping = pd.read_csv("data/input/shipping.csv")

    result = pd.merge(
        insurance.assign(key=1),
        shipping.assign(key=1),
        on='key'
    ).drop('key', axis=1)

    result['risk_score'] = result['claim_amount'] * result['delayed'].apply(lambda x: 1.5 if x else 1)

    os.makedirs("data/output", exist_ok=True)
    result.to_csv("data/output/merged_results.csv", index=False)

    print("Merged and analyzed data saved to data/output/merged_results.csv")
