import pandas as pd

# read the imputed data from the CSV file
data = pd.read_csv('updated_data.csv')

# calculate the median daily vaccination number per country
median_vaccinations = data.groupby('country')['daily_vaccinations'].median().reset_index()
median_vaccinations.columns = ['country', 'median_daily_vaccinations']

# sort the median daily vaccination numbers in descending order and get the top-3 countries
top_countries = median_vaccinations.sort_values('median_daily_vaccinations', ascending=False).head(3)

# print the top-3 countries with their median daily vaccination numbers
print(top_countries[['country', 'median_daily_vaccinations']])
