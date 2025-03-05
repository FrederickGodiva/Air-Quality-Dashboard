# Import Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("./df.csv")


@st.cache_data
def filter_data(station, start_date, end_date):
    """
    Returns the dataset based on the selected station and date range.
    """
    return df[(df['station'] == station) & (df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))]


@st.cache_data
def air_quality_trends(df):
    """
    Returns a line plot showing trends of PM2.5, PM10, and NO2 over time.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df, x='date', y='PM2.5',
                 marker='o', ax=ax, label='PM2.5')
    sns.lineplot(data=df, x='date', y='PM10',
                 marker='x', ax=ax, label='PM10')
    sns.lineplot(data=df, x='date', y='NO2',
                 marker='^', ax=ax, label='NO2')
    ax.set_ylabel("Konsentrasi (µg/m³)")
    ax.set_xlabel("Tanggal")
    ax.legend()
    return fig


@st.cache_data
def pollutant_distribution(df):
    """
    Returns a histogram showing the distribution of PM2.5, PM10, and NO2.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.histplot(df[['PM2.5', 'PM10', 'NO2']], bins=15,
                 kde=True, element='step', ax=ax)
    ax.set_xlabel("Konsentrasi (µg/m³)")
    ax.set_ylabel("Frekuensi")
    ax.set_title("Distribusi PM2.5, PM10, dan NO2")
    return fig


@st.cache_data
def pm_correlation(df):
    """
    Returns a scatter plot showing the correlation between PM2.5 and PM10.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x='PM2.5', y='PM10', alpha=0.6)
    ax.set_xlabel("PM2.5 (µg/m³)")
    ax.set_ylabel("PM10 (µg/m³)")
    return fig


@st.cache_data
def pm_2_5(df):
    """
    Returns a histogram for PM2.5.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df['PM2.5'], bins=30, kde=True, ax=ax)
    ax.set_xlabel("PM2.5 (µg/m³)")
    ax.set_ylabel("Frekuensi")
    return fig


@st.cache_data
def pm_10(df):
    """
    Returns a histogram for PM10.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df['PM10'], bins=30, kde=True, ax=ax)
    ax.set_xlabel("PM2.5 (µg/m³)")
    ax.set_ylabel("Frekuensi")
    return fig


df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
stations = df['station'].unique()

# Set the date range
min_date = df['date'].min()
max_date = df['date'].max()

with st.sidebar:
    station = st.selectbox(
        "Select Station",
        stations
    )

    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

filtered_df = filter_data(station, start_date, end_date)

st.header("Air Quality Dashboard")
st.caption("Copyright © 2025 - Frederick Godiva")

st.subheader(f"Air Quality Trends in {station}")
st.pyplot(air_quality_trends(filtered_df))

st.subheader(f"Pollutant Distribution in {station}")
st.pyplot(pollutant_distribution(filtered_df))

st.subheader("Correlation between PM2.5 and PM10")
st.pyplot(pm_correlation(filtered_df))

col1, col2 = st.columns(2)
with col1:
    st.subheader("PM2.5")
    st.pyplot(pm_2_5(filtered_df))
with col2:
    st.subheader("PM10")
    st.pyplot(pm_10(filtered_df))
