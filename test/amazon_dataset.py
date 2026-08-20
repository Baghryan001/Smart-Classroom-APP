import pandas as pd

df = pd.read_csv('../amazon_sales_dataset.csv')
print('*' * 37)
print('    AMAZON SALES DATA ANALYSIs')
print('*' * 37)

# 1

total_sales_transactions = df['order_id'].shape[0]

print(f'1. Total sales transactions: {total_sales_transactions}\n')

# 2

unique_products = df['product_id'].nunique()
print(f'2. Unique products count: {unique_products}\n')

# 3
unique_product_category = df['product_category'].nunique()
print(f'3. Unique product categories count: {unique_product_category}\n')

# 4

column_df = df.columns
print(f'4. Dataset columns: {column_df}\n')

# 5

missing_values = df.isna().sum().sum()
print(f'5. Total missing values: {missing_values}\n')

# 6

total_revenue = df['total_revenue'].sum()
print(f'6. Total Revenue: {total_revenue}\n')

# 7

average_order_value = total_revenue / total_sales_transactions
print(f'7. Average order value: {average_order_value}\n')

# 8

frequently_product_category = df['product_category'].mode()[0]
print(f'8. Most frequent category: {frequently_product_category}\n')

# 9

common_payment_method = df['payment_method'].mode()[0]
print(f'9. Most common payment method: {common_payment_method}\n')

# 10

top_product_id = df.groupby('product_id')['quantity_sold'].sum().idxmax()
print(f'10. Highest selling product id: {top_product_id}\n')

# 11

revenue_by_category = df.groupby('product_category')['total_revenue'].sum()
print(f'11. Total revenue by product category:\n {revenue_by_category}\n')

# 12

highest_order_value = df.groupby('product_category')['total_revenue'].mean().idxmax()
print(f'12. Generates the highest average order value generates the category: {highest_order_value}\n')

# 13
top_product_revenue = df.groupby('product_category')['total_revenue'].sum().sort_values(
    ascending=False
).head(10)
print(f'13. The top 10 products by revenue: {top_product_revenue}\n')

# 14

customer_rating = df.groupby('product_category')['rating'].mean()
print(f'14. Average customer rating by category: \n{customer_rating}\n')

# 15

top_region_total_revenue = df.groupby('customer_region')['total_revenue'].sum()
top_region_order_count = df.groupby('customer_region')['order_id'].count()
print(f'15. Total revenue by region:\n{top_region_total_revenue}\n')
print(f'Total orders count by region:\n{top_region_order_count}\n')

# 16 --


# 17

evenue_by_payment_method = df.groupby('payment_method')['total_revenue'].sum().sort_values(
    ascending=False
)
print(f'17. Revenue by payment method:\n{evenue_by_payment_method}\n')

# 18

top_reviews = df.groupby('product_id')['review_count'].max().sort_values(
    ascending=False).head(10)
print(f'18. Top 10 product id with the highest number of reviews:\n {top_reviews}\n')

# 19

average_sold_category = df.groupby('product_category')['quantity_sold'].mean().sort_values(
    ascending=False
)
print(f'19. Average quantity sold per category:\n{average_sold_category}\n')

# 20 --


# 21

df['revenue'] = df['discounted_price'] * df['quantity_sold']

final_revenue = df[['price', 'discounted_price', 'quantity_sold', 'revenue']].head(10)
print(f'21. Final revenue: \n{final_revenue}\n')

# 22

corr_discount_revenue = df['discount_percent'].corr(df['total_revenue'])
print(f'22.The relationship between discount percentage and revenue: {corr_discount_revenue}\n')

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
top_cat = (
    df.groupby('product_category')['total_revenue']
    .sum()
    .sort_values(ascending=False)
)
sns.barplot(x=top_cat.index, y=top_cat.values, palette='viridis')
plt.title('Total Revenue by Product Category')
plt.xlabel('Revenue ($)')
plt.ylabel('Category')
plt.show()
