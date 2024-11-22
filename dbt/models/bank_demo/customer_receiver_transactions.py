from snowflake.snowpark.functions import sum as sum_, count as count_

def model(dbt, session):
    customers = dbt.ref("customer_accounts")
    transactions = dbt.ref("transactions")
    
    joined_df = customers.join(transactions, customers.col("account_id")==transactions.col("receiver_account_id"))\
        .select(customers.col("customer_id").alias("customer_id"), transactions.col("transaction_id").alias("transaction_id"), transactions.col("net_cash_flow_amount"))

    
    
    mid_df = joined_df.group_by("customer_id").agg(count_("*").alias("transactions_count"), sum_("net_cash_flow_amount").alias("transactions_amount"))
    customer_detail = dbt.ref("individual_customers")
    
    final_df = mid_df.join(customer_detail, mid_df.col("customer_id") == customer_detail.col("customer_id"))\
                .select(mid_df.col("customer_id").alias("customer_id"), customer_detail.col("full_name"), mid_df.col("transactions_count"), mid_df.col("transactions_amount"))
    
    return final_df