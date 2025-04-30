import pandas as pd
import os

def simulate_insurance_data(path):
    data = {
        'policy_id': range(1, 6),
        'claim_amount': [1000, 1500, 2000, 1200, 1700],
        'status': ['approved', 'pending', 'rejected', 'approved', 'pending']
    }
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

def simulate_shipping_data(path):
    data = {
        'shipment_id': range(1, 6),
        'destination': ['NY', 'LA', 'TX', 'WA', 'FL'],
        'delayed': [False, True, False, False, True]
    }
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

if __name__ == "__main__":
    os.makedirs("data/input", exist_ok=True)
    simulate_insurance_data("data/input/insurance.csv")
    simulate_shipping_data("data/input/shipping.csv")
