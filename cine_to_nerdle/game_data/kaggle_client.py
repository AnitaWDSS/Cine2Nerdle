import kagglehub

import configparser
config = configparser.ConfigParser()

# Download latest version
path = kagglehub.dataset_download("rishabjadhav/imdb-actors-and-movies")

print("Path to dataset files:", path)
print(f"{config.KAGGLE_API_TOKEN}")