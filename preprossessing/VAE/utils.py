from sklearn.preprocessing import MinMaxScaler

def preprocess(df):
    scaler = MinMaxScaler()
    train_df[col] = scaler.fit_transform(train_df[col])
    valid_df[col] = scaler.transform(valid_df[col])
    return df

def train_params():
    params = {'num_columns': len(col),
          'num_labels': 15,
          'hidden_units': [96, 96, 896, 448, 448, 256],
          'dropout_rates': [0.03527936123679956, 0.038424974585075086, 0.42409238408801436, 0.10431484318345882, 0.49230389137187497, 0.32024444956111164, 0.2716856145683449, 0.4379233941604448],
          'ls': 0,
          'lr':1e-3,
         }

    return params
