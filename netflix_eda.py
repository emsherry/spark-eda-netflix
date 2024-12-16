# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Netflix dataset
df = pd.read_csv('/opt/spark/work-dir/netflix_titles.csv')

# Display basic information about the dataset
print('Dataset Info:')
print(df.info())

print('\nDataset Description:')
print(df.describe())

# Display the first few rows
print('\nFirst 5 rows of the dataset:')
print(df.head())

# Check for missing values
print('\nMissing values in the dataset:')
print(df.isnull().sum())

# Distribution of movies and TV shows
print('\nDistribution of Movies and TV Shows:')
sns.countplot(x='type', data=df)
plt.title('Distribution of Movies and TV Shows')
plt.show()

# Genre distribution
print('\nTop 10 Genres:')
top_genres = df['listed_in'].value_counts().head(10)
print(top_genres)
top_genres.plot(kind='bar', title='Top 10 Genres')
plt.ylabel('Frequency')
plt.show()

# Distribution of release year
print('\nDistribution of Release Year:')
sns.histplot(df['release_year'], kde=True)
plt.title('Distribution of Release Year')
plt.show()

# Movies and TV shows count per year
print('\nMovies and TV Shows count per year:')
yearly_count = df.groupby('release_year')['type'].value_counts().unstack().fillna(0)
yearly_count.plot(kind='bar', stacked=True, title='Movies and TV Shows Count per Year')
plt.ylabel('Count')
plt.show()
