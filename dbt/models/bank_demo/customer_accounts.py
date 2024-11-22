def model(dbt, session):
    raw_accounts = dbt.source("raw", "raw_accounts")

    final_df = raw_accounts.select(raw_accounts.col("customer_id"), raw_accounts.col("account_id"))
    
    return final_df