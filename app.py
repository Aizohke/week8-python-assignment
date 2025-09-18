import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ✅ Load data safely without dtype warnings
df = pd.read_csv("metadata.csv", low_memory=False)

st.title("Metadata Dashboard 📊")

st.subheader("Preview of Data")
st.dataframe(df.head())

# ✅ Plot: Publications per year
st.subheader("Publications per Year")
year_counts = df['Year'].value_counts().sort_index()

fig, ax = plt.subplots()
# Use explicit color assignment instead of deprecated palette+hue combo
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax, color="skyblue")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# ✅ Plot: Top Journals
st.subheader("Top Journals")
top_journals = df['Journal'].value_counts().head(10)

fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax, color="salmon")
ax.set_xlabel("Count")
ax.set_ylabel("Journal")
st.pyplot(fig)

# ✅ Plot: Sources
st.subheader("Top Sources")
source_counts = df['Source'].value_counts().head(10)

fig, ax = plt.subplots()
sns.barplot(y=source_counts.index, x=source_counts.values, ax=ax, color="lightgreen")
ax.set_xlabel("Count")
ax.set_ylabel("Source")
st.pyplot(fig)