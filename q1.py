import pandas as pd
import numpy as np

# read the data from the CSV file
data = pd.read_csv('country_vaccination_stats.csv')

# create a new DataFrame with minimum daily vaccinations per country
min_vaccinations = data.groupby('country')['daily_vaccinations'].min().reset_index()
min_vaccinations.columns = ['country', 'min_daily_vaccinations']

# merge the original data with the minimum daily vaccinations data
data = data.merge(min_vaccinations, on='country')

# replace missing daily vaccination data with the minimum daily vaccination number of relevant countries
data['daily_vaccinations'] = np.where(data['daily_vaccinations'].isna(),
                                      data['min_daily_vaccinations'], data['daily_vaccinations'])

# fill missing data with 0 (zero)
data['daily_vaccinations'] = data['daily_vaccinations'].fillna(0)

# save the updated data to a new CSV file
data.to_csv('updated_data.csv', index=False)
