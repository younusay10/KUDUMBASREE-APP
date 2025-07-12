import streamlit as st
import pandas as pd
import datetime

# Load or create data
def load_data():
    try:
        df = pd.read_csv("kudmastry_data.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Amount_Contributed", "Amount_Received", "Date", "Purpose"])
        df.to_csv("kudmastry_data.csv", index=False)
    return df

# Save data
def save_data(df):
    df.to_csv("kudmastry_data.csv", index=False)

st.title("🌿 Kudmastry Family Contribution App")

menu = st.sidebar.selectbox("Menu", ["View Records", "Add Contribution", "Add Disbursement"])

df = load_data()

if menu == "View Records":
    st.subheader("📋 All Transactions")
    st.dataframe(df)

elif menu == "Add Contribution":
    st.subheader("➕ Add New Contribution")
    name = st.text_input("Member Name")
    amount = st.number_input("Amount Contributed", min_value=0.0)
    date = st.date_input("Date", value=datetime.date.today())
    if st.button("Add Contribution"):
        new_entry = pd.DataFrame([[name, amount, 0, date, "Contribution"]],
                                 columns=df.columns)
        df = pd.concat([df, new_entry], ignore_index=True)
        save_data(df)
        st.success("Contribution Added!")

elif menu == "Add Disbursement":
    st.subheader("💸 Add New Disbursement")
    name = st.text_input("Receiver Name")
    amount = st.number_input("Amount Received", min_value=0.0)
    date = st.date_input("Date", value=datetime.date.today())
    purpose = st.text_area("Purpose")
    if st.button("Add Disbursement"):
        new_entry = pd.DataFrame([[name, 0, amount, date, purpose]],
                                 columns=df.columns)
        df = pd.concat([df, new_entry], ignore_index=True)
        save_data(df)
        st.success("Disbursement Added!")

st.sidebar.markdown("Made for Kudmastry Program 👨‍👩‍👧‍👦")
