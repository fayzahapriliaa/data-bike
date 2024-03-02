import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
day_df = pd.read_csv("day.csv")

# Page Title
st.title('Analisis Data Bike Sharing Dashboard')


# Show DataFrame
st.header('Bike Sharing Day:')
st.dataframe(day_df.head())

# Aggregations
bikes_per_season = day_df.groupby('season')['cnt'].sum()

# Create bar chart for bikes per season
st.header('Grafik Jumlah Sepeda Dipinjam per Musim:')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=bikes_per_season.index, y=bikes_per_season.values, palette="viridis", ax=ax)
plt.title('Jumlah Sepeda yang Dipinjam per Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Sepeda Dipinjam')
st.pyplot(fig)

# ...

# User Type per Year
user_type_per_year = day_df.groupby('yr')[['registered', 'casual']].sum()

# Create bar chart for user type per year
st.header('Grafik Jumlah Pengguna Terdaftar dan Casual per Tahun:')
fig, ax = plt.subplots(figsize=(10, 6))
user_type_per_year.plot(kind='bar', color=['orange', 'green'], ax=ax)
plt.title('Jumlah Pengguna Terdaftar dan Casual per Tahun')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Pengguna')
plt.xticks(rotation=0)
plt.legend(['Registered', 'Casual'])
st.pyplot(fig)

# ...

# User Type per Season
user_type_per_season = day_df.groupby(['season'])[['registered', 'casual']].sum()
st.header('Grafik Jumlah Pengguna Terdaftar dan Casual per Musim:')
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x=user_type_per_season.index - 0.2, y=user_type_per_season['registered'], width=0.4, color='orange', label='Registered', ax=ax)
sns.barplot(x=user_type_per_season.index + 0.2, y=user_type_per_season['casual'], width=0.4, color='green', label='Casual', ax=ax)
plt.title('Jumlah Pengguna Terdaftar dan Casual per Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Pengguna')
plt.xticks(user_type_per_season.index, user_type_per_season.index)
plt.legend()
st.pyplot(fig)

# ...

