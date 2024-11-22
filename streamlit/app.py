import streamlit as st
import snowflake.connector
import os
from dotenv import load_dotenv

st.set_page_config(page_title="data-mesh-bank-demo", initial_sidebar_state="collapsed", layout="wide")
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>

""",
    unsafe_allow_html=True,
)

@st.cache_resource
def get_conn():
    return snowflake.connector.connect(user="dmc_streamlit",
                                       password="",
                                       account="FRA00296",
                                       warehouse="DPS_ADMIN_WAREHOUSE",
                                       database="DPS_AEP_DEMO_DEV",
                                       schema="BANK_DEMO",
                                       client_session_keep_alive=True)

@st.cache_data
def load_data(_conn, query):
    with _conn.cursor() as cur:
        cur.execute(query)
        return cur.fetch_pandas_all()

load_dotenv()
conn = get_conn()
    
data = load_data(conn, "select * from DPS_AEP_DEMO_DEV.BANK_DEMO.CUSTOMER_SENDER_TRANSACTIONS")

# st.write(data)

# st.area_chart(data=data, x="FULL_NAME", y=['TRANSACTIONS_COUNT','TRANSACTIONS_AMOUNT'])

st.subheader("Sender transactions")

st.bar_chart(data, x="FULL_NAME", y=['TRANSACTIONS_COUNT','TRANSACTIONS_AMOUNT'])

data1 = load_data(conn, "select * from DPS_AEP_DEMO_DEV.BANK_DEMO.CUSTOMER_RECEIVER_TRANSACTIONS")

# st.write(data1)

# st.area_chart(data=data1, x="FULL_NAME", y=['TRANSACTIONS_COUNT','TRANSACTIONS_AMOUNT'])

st.subheader("Receiver transactions")

st.bar_chart(data1, x="FULL_NAME", y=['TRANSACTIONS_COUNT','TRANSACTIONS_AMOUNT'])

