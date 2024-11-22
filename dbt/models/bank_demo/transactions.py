from snowflake.snowpark.functions import col
from snowflake.snowpark import Row
from faker import Faker

def model(dbt, session):
    dbt.config(
        packages = ["faker==8.8.1"],
        transient = False
    )
     
    fake = Faker("en_US")
    Faker.seed(12345)
    
    raw_transactions = dbt.source("raw", "raw_transactions")
    transactions = raw_transactions.select(raw_transactions.col("TX_ID"), raw_transactions.col("SENDER_ACCOUNT_ID"),
                                       raw_transactions.col("RECEIVER_ACCOUNT_ID"), raw_transactions.col("TX_TYPE"),
                                       raw_transactions.col("TX_AMOUNT")).collect()
    final_rows = []
    
    for row in transactions:
        print(f"Row: {row}")
        final_row = Row(transaction_id=row['TX_ID'], sender_account_id=row['SENDER_ACCOUNT_ID'], receiver_account_id=row['RECEIVER_ACCOUNT_ID'], 
                             transaction_type=row['TX_TYPE'], net_cash_flow_amount=row['TX_AMOUNT'], transaction_time=fake.date_time_between(start_date='-2y'))
        final_rows.append(final_row)
    
    final_df = session.create_dataframe(final_rows)
    
    return final_df