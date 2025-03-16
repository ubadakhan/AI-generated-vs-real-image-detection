import os
from kaggle.api.kaggle_api_extended import KaggleApi


api = KaggleApi()
api.authenticate()  

dataset = "birdy654/cifake-real-and-ai-generated-synthetic-images"  
download_path = "./synthetic_data"  

if not os.path.exists(download_path):
    os.makedirs(download_path)

api.dataset_download_files(dataset, path=download_path, unzip=True)

#print(f"Dataset downloaded to {download_path}")