import os
os.environ["MODIN_ENGINE"] = "dask"  # Modin will use Dask
import modin.pandas as pd
import numpy as np
import streamlit as st

PATHS = [
    'datasets/CICDataset2017/Monday-WorkingHours.pcap_ISCX.csv',
    'datasets/CICDataset2017/Tuesday-WorkingHours.pcap_ISCX.csv',
    'datasets/CICDataset2017/Wednesday-workingHours.pcap_ISCX.csv',
    'datasets/CICDataset2017/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv',
    'datasets/CICDataset2017/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv',
    'datasets/CICDataset2017/Friday-WorkingHours-Morning.pcap_ISCX.csv',
    'datasets/CICDataset2017/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv',
    'datasets/CICDataset2017/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv']

df = pd.read_csv(PATHS[0])
total = len(PATHS) - 1
my_bar = st.progress(1/total)
for i in range(1,len(PATHS)):
    temp = pd.read_csv(PATHS[i])
    df = pd.concat([df,temp])
    my_bar.progress(i/total)

st.balloons()

#st.write(df)
