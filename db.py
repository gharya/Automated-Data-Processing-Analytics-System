from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd

def load_to_sqlite():
    engine = create_engine('sqlite:///data/output/analytics.db')
    df = pd.read_csv("data/output/merged_results.csv")
    df.to_sql('insurance_shipping_analysis', con=engine, if_exists='replace', index=False)
    return engine

def query_database(engine):
    query = text("""
        SELECT destination, AVG(risk_score) as avg_risk
        FROM insurance_shipping_analysis
        GROUP BY destination;
    """)
    with engine.connect() as conn:
        result = conn.execute(query)
        for row in result:
            print(row)