from snowflake.snowpark.functions import col
from snowflake.snowpark import Row
from faker import Faker

def model(dbt, session):
    dbt.config(
        packages = ["faker==8.8.1"]
    )
     
    fake = Faker("en_US")
    Faker.seed(12345)
    
    raw_accounts = dbt.source("raw", "raw_accounts")
    accounts = raw_accounts.select(raw_accounts.col("account_id"), raw_accounts.col("init_balance")).collect()
    
    final_accounts = []
    for row in accounts:
        print(f"Row: {row}")
        final_row = Row(account_unit_id=row['ACCOUNT_ID'], net_amount=row['INIT_BALANCE'], population_time=fake.date_time_between(start_date='-2y'))
        final_accounts.append(final_row)
    
    
    final_df = session.create_dataframe(final_accounts)
    
    return final_df