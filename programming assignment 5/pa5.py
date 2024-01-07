import pandas as pd
pd.set_option('display.max_columns', None)

# task a (dataframe a)
review_df_a = pd.read_csv('review_phx_hw.csv')

# missing values set to -1
review_df_a = review_df_a.fillna(value=-1)

# converting postal_code column to an int and then a str
review_df_a[['postal_code']] = review_df_a[['postal_code']].astype(int)
review_df_a[['postal_code']] = review_df_a[['postal_code']].astype(str)

# print the first and last 15 observations
print(review_df_a.head(n=15))
print(review_df_a.tail(n=15))

# task b (dataframe b)
review_df_b = review_df_a

# includes all observations not including -1 in the 'stars' and 'review_count' columns
review_df_b = review_df_b.loc[~(review_df_b['stars'] == -1) & ~(review_df_b['review_count'] == -1)]

# view same range to verify the code is executing properly
print(review_df_b.head(n=15))
print(review_df_b.tail(n=15))

# describing the 'review_count' and 'stars' columns
print(review_df_b[['review_count', 'stars']].describe())

# task c (dataframe c)
review_df_c = review_df_b

# closed restaurants, with 100-500 reviews, and above 3.0 stars are all included in df_c
review_df_c = review_df_c.loc[(review_df_c['is_open'] == 0) & (review_df_c['review_count'] > 100) & (review_df_c['review_count'] < 500) & (review_df_c['stars'] > 3.0)]
print(review_df_c)

# average rating and review count grouped by zipcodes
agg1 = review_df_c.groupby('postal_code').agg(
    mean_stars=('stars', 'mean'),
    mean_review=('review_count', 'mean')
).reset_index()
print(agg1)
print("This function found the average star rating and number of reviews in aggregated postal codes. There is no clear \n relationship between the number of reviews and the level of rating. Though, restaurants in 85007 had the highest \n average star rating while restaurants in 85008, 85024, and 85054 had the lowest average star ratings.")

# task d (dataframe d), selecting only postal codes 85004, 85006, and 85008 from dataframe b
review_df_d = review_df_b.loc[(review_df_b['postal_code'] == '85004') | (review_df_b['postal_code'] == '85006') | (review_df_b['postal_code'] == '85008')]
print(review_df_d)

# concatenating dataframes c and d together
review_df = [review_df_c, review_df_d]
review_df_final = pd.concat(review_df)

# dropping any duplicate values
review_df_final = review_df_final.drop_duplicates()
print(review_df_final)

# task e, sort by ascending postal code and descending rating
review_df_final = review_df_final.sort_values(by=['postal_code', 'stars'], ascending=[True, False])

# include only the columns of name, postal_code, stars, and review_count by dropping the remaining columns
review_df = review_df_final.drop(columns=['business_id', 'city', 'state', 'is_open'])
print(review_df)

# converting final dataframe to a csv file
review_df.to_csv('komalmatharu_pa5.csv', index=False)
