# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("📊 Simple exploration of COVID-19 research papers (metadata.csv)")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df = df[['title', 'abstract', 'publish_time', 'journal', 'source_x']]
    df = df.dropna(subset=['title', 'publish_time'])
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
year_range = st.sidebar.slider("Select Year Range", 
                               int(df['year'].min()), 
                               int(df['year'].max()), 
                               (2019, 2021))

filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Show sample data
st.subheader("Sample Data")
st.dataframe(filtered.head(10))

# Publications by year
st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax, palette="viridis")
ax.set_title("Publications per Year")
st.pyplot(fig)

# Top journals
st.subheader("Top 10 Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax, palette="magma")
ax.set_title("Top 10 Journals")
st.pyplot(fig)

# Word cloud of titles
st.subheader("Word Cloud of Titles")
text = " ".join(filtered['title'].dropna().values)
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
fig, ax = plt.subplots(figsize=(10,5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Sources
st.subheader("Top Sources")
source_counts = filtered['source_x'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(y=source_counts.index, x=source_counts.values, ax=ax, palette="coolwarm")
ax.set_title("Top 10 Sources")
st.pyplot(fig)
