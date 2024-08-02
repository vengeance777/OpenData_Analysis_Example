import pandas as pd
import matplotlib.pyplot as plt

# https://www.avoindata.fi/data/fi/dataset/tukes-avoindatajulkaisut/resource/99074f7a-2843-4ff7-9e0e-0e92340887db


def preview_file(file_path, lines = 100):
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        for _ in range (lines):
            print(file.readline().strip())

#Edit file path here
file_path = '/'
print("File Preview:")
preview_file(file_path, lines=100)

def load_data(file_path):
    try:
        df = pd.read_csv(file_path, encoding = 'ISO-8859-1', on_bad_lines='skip')
        print("File loaded succesfully")
        return df
    except Exception as e:
        print (f"Error loading file: {e}")
        return None


data = load_data(file_path)

if data is not None:
    # print used instead of display
    print("Basic Information:")
    #display(data.info())
    print(data.info())

    print("\nFirst 5 rows:")
    #display(data.head())
    print(data.head())

if data is not None:
    # print used instead of display
    # summary statistics
    print("Summary Statistics:")
    #display(data.describe())
    print(data.describe())

if data is not None:
    # check for missing values
    # print used instead of display
    print("n\Missing values:")
    #display(data.isnull().sum())
    print(data.isnull().sum())

    df = pd.read_csv(file_path, sep=';')
    # Convert the 'julkaisu_pvm' column to datetime
    df['julkaisu_pvm'] = pd.to_datetime(df['julkaisu_pvm'], dayfirst=True)
    # Use only year
    df['year'] = df['julkaisu_pvm'].dt.year


# Calculate the total counts for each 'vaaranlaji'
total_counts = df['vaaranlaji'].value_counts()

# Select the top 5 'vaaranlaji'
top_5_vaaranlaji = total_counts.nlargest(5).index

# Filter the data to include only the top 5 'vaaranlaji'
filtered_df = df[df['vaaranlaji'].isin(top_5_vaaranlaji)]

# Group by 'year' and count the occurrences of 'vaaranlaji'
grouped_df = filtered_df.groupby(['year', 'vaaranlaji']).size().unstack().fillna(0)

# Plotting
plot = grouped_df.plot(kind='line', figsize=(10, 6), title='Top 5 Vaarat ryhmittäin vuosittain')
plot.set_xlabel('Vuosi')
plot.set_ylabel('Counts of Vaaranlaji')
plot.grid(True)
plot.legend(title='Vaaranlaji')
plt.tight_layout()
plt.show()