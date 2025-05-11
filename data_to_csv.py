import pandas as pd
data={"Details": [
        "Card Payment Received",
        "EMIRATES INSURANCE",
        "NOON.COM",
        "LULU HYPERMARKET",
        "UBER AE",
        "AMAZON AE",
        "SPINNEYS AE",
        "ADCB BANK FEE",
        "NETFLIX.COM",
        "ETIHAD AIRWAYS",
        "HILTON DUBAI",
        "BOOKING.COM",
        "APPLE.COM BILL",
        "ZOMATO AE"
    ],
    "Category": [
        "Income",
        "Insurance",
        "Shopping",
        "Groceries",
        "Transportation",
        "Shopping",
        "Groceries",
        "Bank Charges",
        "Entertainment",
        "Travel",
        "Travel",
        "Travel",
        "Subscriptions",
        "Food Delivery"
    ]
}
dataframe=pd.DataFrame(data)
print(dataframe)
try:
    dftocsv=dataframe.to_csv("labeled_transaction",index=False)
except Exception as e:
    print(f"ERROR:{e}")
finally:
    print(dftocsv)