import pandas as pd
import matplotlib.pyplot as plt

def load_json(file_path):
    
    try:
        dataframe = pd.read_json(file_path)
        return dataframe
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return None

def separate_groups(df):
    # Separate the dataset into two groups based on loudness
    below_eight_df = df[df['loudness'] < -8]
    above_or_equal_eight_df = df[df['loudness'] >= -8]
    return below_eight_df, above_or_equal_eight_df

def create_histogram(data, title, filename):
    # Create and save a histogram plot
    plt.hist(data, bins=20, color='blue', alpha=0.7)
    plt.title(title)
    plt.xlabel('Tempo')
    plt.ylabel('Frequency')
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    # Replace 'your_dataset.json' with the actual file path
    dataset_path = 'songdata.json'
    
    # Load the dataset
    spotify_df = load_json(dataset_path)

    if spotify_df is not None:
        # Separate the dataset into two groups based on loudness
        below_eight, above_or_equal_eight = separate_groups(spotify_df)

        # Create histograms for each group
        create_histogram(below_eight['tempo'], 'Tempo Distribution - Loudness < -8', 'hist1.png')
        create_histogram(above_or_equal_eight['tempo'], 'Tempo Distribution - Loudness >= -8', 'hist2.png')
