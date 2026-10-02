import pandas as pd

df = (pd.read_csv('customer_shopping_behavior.csv')
      .rename(columns=lambda c: c.strip().lower().replace(' (usd)', '_usd').replace(' ', '_'))
      .drop_duplicates()
      .assign(
          review_rating=lambda d: d['review_rating'].fillna(d.groupby('category')['review_rating'].transform('median')),
          frequency_of_purchases=lambda d: d['frequency_of_purchases'].replace({'Fortnightly': 'Bi-Weekly', 'Every 3 Months': 'Quarterly'}))
      .apply(lambda s: s.str.strip() if s.dtype in ('object', 'str') else s)
      .query('18 <= age <= 100 and purchase_amount_usd > 0')
      .reset_index(drop=True))

df.to_csv('customer_shopping_behavior_clean.csv', index=False)
print(df.shape, df.isna().sum().sum())