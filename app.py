import streamlit as st
from bank import Bank

bank = Bank()

st.title("🏦 Simple Banking System")

menu = [
"Create Account",
"Deposit Money",
"Withdraw Money",
"Show Details",
"Delete Account"
]

choice = st.sidebar.selectbox("Menu", menu)

# CREATE ACCOUNT
if choice == "Create Account":

    st.header("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("4 Digit PIN", type="password")

    if st.button("Create"):

        result = bank.create_account(name, age, email, int(pin))

        if isinstance(result, dict):
            st.success("Account Created")
            st.write(result)

        else:
            st.error(result)


# DEPOSIT
elif choice == "Deposit Money":

    st.header("Deposit")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount")

    if st.button("Deposit"):

        result = bank.deposit(acc, int(pin), amount)

        st.success(f"New Balance: {result}")


# WITHDRAW
elif choice == "Withdraw Money":

    st.header("Withdraw")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount")

    if st.button("Withdraw"):

        result = bank.withdraw(acc, int(pin), amount)

        st.success(result)


# SHOW DETAILS
elif choice == "Show Details":

    st.header("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):

        user = bank.find_user(acc, int(pin))

        if user:
            st.json(user)
        else:
            st.error("User not found")


# DELETE
elif choice == "Delete Account":

    st.header("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):

        result = bank.delete(acc, int(pin))

        st.warning(result)