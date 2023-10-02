"""
    Credit_card_bal_gt_limit_pandas_2.py, just explored web to get glimpse of Pandas and used this to excercise
    git and github commands.  Instructions are great.
    I needed to issue these commands to identify myself so git know who is committing the changes

    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"
"""
import pandas as pd

dim_card_details_amex = pd.DataFrame({
    'card_id': [0, 1],
    'user_id': [0, 1],
    'card_type': ['Platnium', 'Gold'],
    'account_open_date': ['9/102', '7/101'],
    'card_expiry': ['12/1/22', '11/1/23'],
    'card_limit': [50000, 30000]
})

fact_daily_transactions_amex = pd.DataFrame({
    'transaction_date': ['2013-05-01 00:00:00', '2013-05-02 00:00:00', '2013-05-03 00:00:00'],
    'card_id': [0, 1, 1],
    'user_id': [0, 1, 1],
    'amount': [5335.76, 2500.00, 31000.00],
    'transaction_type': ['Swipe Transaction', 'Online Purchase', 'Online Purchase'],
    'merchant_city': ['Monterey Park', 'San Francisco', 'Los Angeles'],
    'merchant_state': ['CA', 'CA', 'NV']
})

# Rename 'user_id' column to 'transaction_user_id' in fact_daily_transactions_amex
fact_daily_transactions_amex.rename(columns={'user_id': 'transaction_user_id'}, inplace=True)

# Merge DataFrames with 'user_id' included in 'on' parameter
merged_data = pd.merge(
    fact_daily_transactions_amex,
    dim_card_details_amex[['card_id', 'user_id', 'card_type', 'card_limit']],
    on='card_id'
)
print('---- columns of dataframe: merged_data ----')
# _ = [print(column) for column in merged_data.columns]
print(f'1. merged_data = {merged_data.head(5)}\n')

# Calculate total transactions for each card including 'card_type' and 'merchant_city' as a list
total_transactions = merged_data.groupby(['user_id', 'card_id', 'card_type', 'card_limit'], as_index=False).agg(
    {'amount': 'sum', 'merchant_city': list})
print(f'2. total_transactions {total_transactions.head(5)}\n')

# Identify cards that have exceeded their limit
exceeded_limit_cards = total_transactions[total_transactions['amount'] > total_transactions['card_limit']]
print(f'3. exceeded limit_cards: {exceeded_limit_cards.head(5)}')

# Display the results
for index, row in exceeded_limit_cards.iterrows():
    user_id = row['user_id']
    card_id = row['card_id']
    card_type = row['card_type']
    merchant_cities = row['merchant_city']
    total_transaction_amount = row['amount']
    card_limit = row['card_limit']
    print(
        f"User ID: {user_id}, Card ID: {card_id}, Card Type: {card_type}, "
        f"Merchant Cities: {', '.join(merchant_cities)}, "
        f"Total transactions on the card: {total_transaction_amount}, Card Limit: {card_limit}")
