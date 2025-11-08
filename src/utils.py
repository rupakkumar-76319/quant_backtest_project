import pandas as pd

def load_data(file_path):
    data=pd.read_csv(file_path)
    print("Data loaded successfully!")
    print(data.head())
    return data

def prepare_data(data):

    # Convert Date formate to datetime formate.
    data['Date'] = pd.to_datetime(data['Date'])

    # Sort the data accoding to the date
    data= data.sort_values('Date')

    # Remove missing value 
    data=data.dropna()

    print("Data cleaned and ready for the analysis!")
    print(data.info())
    return data