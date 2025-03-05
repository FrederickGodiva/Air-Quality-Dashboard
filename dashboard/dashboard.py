# Import Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("./dashboard/df.csv")


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


@st.cache_data
def max_pm(df):
    """
    Returns bar charts showing the top 5 stations with the highest PM2.5 and PM10 levels.
    """
    max_pm25 = df.groupby(by="station").agg({
        "PM2.5": "max",
    }).sort_values(by="PM2.5", ascending=False).head(5)

    max_pm10 = df.groupby(by="station").agg({
        "PM10": "max",
    }).sort_values(by="PM10", ascending=False).head(5)

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 12))

    sns.barplot(x="PM2.5", y="station", data=max_pm25, hue="station",
                palette="colorblind", ax=ax[0])
    ax[0].set_xlabel(None)
    ax[0].set_ylabel(None)
    ax[0].set_title("Stasiun Polusi PM2.5 Terbanyak",
                    loc="center", fontsize=18)
    ax[0].tick_params(axis='y', labelsize=12)

    sns.barplot(x="PM10", y="station", data=max_pm10, hue="station",
                palette="colorblind", ax=ax[1])
    ax[1].set_xlabel(None)
    ax[1].set_ylabel(None)
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("Stasiun Polusi PM10 Terbanyak", loc="center", fontsize=18)
    ax[1].tick_params(axis='y', labelsize=12)

    plt.suptitle("Stasiun Polusi PM2.5 dan PM10 Terbanyak", fontsize=32)

    return fig


@st.cache_data
def temperature_pm_correlation(df):
    """
    Returns scatter plots showing the correlation between temperature and PM2.5/PM10 levels.
    """
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

    sns.scatterplot(x=df['TEMP'], y=df['PM2.5'], ax=ax[0])
    ax[0].set_xlabel("Temperature")
    ax[0].set_ylabel("PM2.5")
    ax[0].set_title("Pengaruh Temperatur terhadap PM2.5",
                    loc="center", fontsize=18)
    ax[0].tick_params(axis='y', labelsize=12)

    sns.scatterplot(x=df['TEMP'], y=df['PM10'], ax=ax[1])
    ax[1].set_xlabel("Temperature")
    ax[1].set_ylabel("PM10")
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("Pengaruh Temperatur terhadap PM10",
                    loc="center", fontsize=18)
    ax[1].tick_params(axis='y', labelsize=12)

    return fig


@st.cache_data
def windspeed_pm_correlation(df):
    """
    Returns a scatter plots showing the effect of wind speed on PM2.5 and PM10.
    """
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 10))

    sns.scatterplot(x=df['WSPM'], y=df['PM2.5'], ax=ax[0])
    ax[0].set_xlabel("Wind Speed")
    ax[0].set_ylabel("PM2.5")
    ax[0].set_title("Pengaruh Kecepatan Angin terhadap PM2.5",
                    loc="center", fontsize=18)
    ax[0].tick_params(axis='y', labelsize=12)

    sns.scatterplot(x=df['WSPM'], y=df['PM10'], ax=ax[1])
    ax[1].set_xlabel("Wind Speed")
    ax[1].set_ylabel("PM10")
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("Pengaruh Kecepatan Angin terhadap PM10",
                    loc="center", fontsize=18)
    ax[1].tick_params(axis='y', labelsize=12)

    return fig


@st.cache_data
def temperature_station(df):
    """
    Returns a lineplot of the average temperature changes over time for each station.
    """
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
    monthly_avg_temp = df.groupby([df['station'], df['date'].dt.to_period('M')])[
        'TEMP'].mean().reset_index()
    monthly_avg_temp['date'] = monthly_avg_temp['date'].dt.to_timestamp()

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.lineplot(data=monthly_avg_temp, x='date', y='TEMP',
                 hue='station', marker='o', ax=ax)
    ax.set_title('Temperature Change by Station')
    ax.set_ylabel('Average Temperature')
    plt.xticks(rotation=45)

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

st.subheader(f"Air Quality Trends at {station}")
st.pyplot(air_quality_trends(filtered_df))

st.subheader(f"Pollutant Distribution at {station}")
st.pyplot(pollutant_distribution(filtered_df))

st.subheader("Correlation Between PM2.5 and PM10")
st.pyplot(pm_correlation(filtered_df))

col1, col2 = st.columns(2)
with col1:
    st.subheader("PM2.5")
    st.pyplot(pm_2_5(filtered_df))
with col2:
    st.subheader("PM10")
    st.pyplot(pm_10(filtered_df))


st.subheader("Stations With the Highest PM2.5 and PM10 Levels")
st.pyplot(max_pm(df))

st.subheader("Correlation Between Temperature with PM2.5 and PM10")
st.pyplot(temperature_pm_correlation(df))

st.subheader("Effect of Wind Speed on Pollutants")
st.pyplot(windspeed_pm_correlation(df))

st.subheader(f"Temperature Changes at {station}")
st.pyplot(temperature_station(filtered_df))
