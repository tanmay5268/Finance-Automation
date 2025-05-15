import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os
import joblib

st.set_page_config(page_title="FINANCE APP",page_icon="$",layout="wide")
#-------------------------------------
model = joblib.load("transaction_categorizer.pkl")
vectorizer = joblib.load("vectorizer.pkl")
#-------------------------------------
def predict_categories(details):
    #details column ko vector me change krna
    details_vector= vectorizer.transform(details)
    #category vaale column me details ki predicted category store hogi
    return model.predict(details_vector)
#-------------------------------------

def load_transactions(file):
    try:
        #csv file upload and loading
        df = pd.read_csv(file)
        df.columns=[col.strip() for col in df.columns] #remove spaces from col names
        df["Amount"]= df["Amount"].str.replace(",","").astype(float)
        df["Date"] = pd.to_datetime(df["Date"],format="%d %b %Y")
 
        st.write(df)
        return df
    except Exception as e:
        st.error(f"ERROR PROCESSING FILE:{str(e)}")
        return None

#------------------------------------------------

def main():
    st.title("FINANCE DASHBOARD")
    st.sidebar.title("FINANCE DASHBOARD")
    uploaded_file=st.file_uploader("Upload bank statement here",type=["csv"])
    
    if uploaded_file is not None:
        df = load_transactions(uploaded_file)
        if df is not None:
            option = st.sidebar.radio(
                "Choose an option:",
                ["Filter by Categories", "Debit/Credit Filter", "Pie Chart Summarizer"]
            )
            if option == "Debit/Credit Filter":

                credit_df= df[df["Debit/Credit"]== "Credit"]
                debit_df= df[df["Debit/Credit"]== "Debit"]

                tab1,tab2 =st.tabs(["DEBITS","CREDITS"])
                with tab1:
                    st.write(debit_df)
                    total_debits = debit_df["Amount"].sum()
                    st.metric(label="Total debits", value=f"{total_debits}")
                with tab2:
                    st.write(credit_df)
                    total_credits = credit_df["Amount"].sum()
                    st.metric(label="Total credits", value=f"{total_credits}")
            elif option == "Filter by Categories":
                #prediction for details column
                df["Category"]= predict_categories(df["Details"])#abh iske under ai prediction ho chuki hai
                #adding dropdown menu
                categories = df["Category"].unique()
                selected_category = st.selectbox("select category to filter",categories)
                filtered_df= df[df["Category"]==selected_category]
                st.write(filtered_df)
            elif option == "Pie Chart Summarizer":
                
                try:
                        # Pie chart summarizing spending by category
                    category_summary = df.groupby("Category")["Amount"].sum().reset_index()
                    fig = px.pie(category_summary, values="Amount", names="Category", title="Spending by Category")
                except Exception as e:
                    print(f"{e}")
                finally:
                    st.plotly_chart(fig)
                
#------------------------------------------------
if __name__ == "__main__":
    main()