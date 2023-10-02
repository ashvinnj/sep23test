import pandas as pd

# Sample data
dim_card_details_amex = pd.DataFrame({
    'card_id': [0, 1],  # Adding another card_id
    'user_id': [0, 1],  # Adding another user_id
    'card_type': ['Platnium', 'Gold'],  # Card type for the second card
    'account_open_date': ['9/102', '7/101'],  # Account open date for the second card
    'card_expiry': ['12/1/22', '11/1/23'],  # Card expiry for the second card
    'card_limit': [50000, 30000]  # Card limit for the second card
})

fact_daily_transactions_amex = pd.DataFrame({
    'transaction_date': ['2013-05-01 00:00:00', '2013-05-02 00:00:00', '2013-05-03 00:00:00'],  # Adding another transaction
    'card_id': [0, 1, 1],  # Assigning the second card_id
    'user_id': [0, 1, 1],  # Assigning the second user_id
    'amount': [5335.76, 2500.00, 3000.00],  # Adding another transaction amount
    'transaction_type': ['Swipe Transaction', 'Online Purchase', 'Onilne Purchase'],  # Transaction type for the second transaction
    'merchant_city': ['Monterey Park', 'San Francisco', 'Los Angles'],  # Merchant city for the second transaction
    'merchant_state': ['CA', 'CA', 'NV']
    # Merchant state for the second transaction
})

# Merge DataFrames
merged_data = pd.merge(fact_daily_transactions_amex, dim_card_details_amex, on='card_id')
print(merged_data.head(5))
print(merged_data.tail(5))

# Calculate total transactions for each card including 'card_type' and 'merchant_city' as a list
total_transactions = merged_data.groupby(['user_id', 'card_id', 'card_type']).agg({'amount': 'sum', 'card_limit': 'first', 'merchant_city': list}).reset_index()
print(total_transactions.tail(5))

# Identify cards that have exceeded their limit
exceeded_limit_cards = total_transactions[total_transactions['amount'] > total_transactions['card_limit']]

# Display the results
for index, row in exceeded_limit_cards.iterrows():
    user_id = row['user_id']
    card_id = row['card_id']
    card_type = row['card_type']
    merchant_cities = row['merchant_city']
    total_transactions = row['amount']
    card_limit = row['card_limit']

    print(
        f"User ID: {user_id}, Card ID: {card_id}, Card Type: {card_type}, "
        f"Merchant Cities: {', '.join(merchant_cities)}, "
        f"Total transactions on the card: {total_transactions}, Card Limit: {card_limit}")
