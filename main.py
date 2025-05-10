import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

st.set_page_config(page_title="FINANCE APP",page_icon="$",layout="wide")
def load_transactions(file):
    try:
        df = pd.read_csv(file)
        df.columns=[col.strip() for col in df.columns] #remove spaces from col names
        df["Amount"]= df["Amount"].str.replace(",","").astype(float)
        df["Date"] = pd.to_datetime(df["Date"],format="%d %b %Y")

        st.write(df)
        return df
    except Exception as e:
        st.error(f"ERROR PROCESSING FILE:{str(e)}")
        return None
def main():
    st.title("FINANCE DASHBOARD")
    uploaded_file=st.file_uploader("Upload bank statement here",type=["csv"])
    
    if uploaded_file is not None:
        df = load_transactions(uploaded_file)
        if df is not None:
            credit_df= df[df["Debit/Credit"]== "Credit"]
            debit_df= df[df["Debit/Credit"]== "Debit"]

            tab1,tab2 =st.tabs(["DEBITS","CREDITS"])
            with tab1:
                st.write(debit_df)
            with tab2:
                st.write(credit_df)

if __name__ == "__main__":
    main()