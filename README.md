   📊 CORD-19 Research Data Explorer

This repository contains my assignment for exploring the CORD-19 research dataset.  
It includes both a Jupyter Notebook for data analysis and a Streamlit web application for interactive visualization.

---

     📁 Project Structure
- `analysis.ipynb` → Jupyter notebook with step-by-step data analysis (loading, cleaning, exploration, visualization).
- `app.py` → Streamlit application for interactive exploration of the dataset.
- `metadata.csv` → Sample of the CORD-19 metadata file (not uploaded here due to size; see dataset link below).

---

    🎯 Objectives
By completing this project, I practiced:
- Loading and exploring real-world datasets using pandas  
- Handling missing values and preparing data for analysis  
- Creating meaningful visualizations with matplotlib and seaborn  
- Building a simple interactive Streamlit web app 
- Presenting insights effectively  

---

    🗂 Dataset
The dataset comes from the [CORD-19 Research Challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).

We used only the `metadata.csv` file, which contains:
- Paper titles and abstracts  
- Publication dates  
- Authors and journals  
- Source information  

---
     ⚙️ Installation & Setup

1. Clone the repository
```bash
git clone https://github.com/your-username/Frameworks_Assignment.git
cd Frameworks_Assignment
````

 2. Install dependencies

```bash
pip install pandas matplotlib seaborn streamlit
```

3. Run the Jupyter Notebook

```bash
jupyter notebook analysis.ipynb
```

 4. Run the Streamlit App

```bash
python -m streamlit run app.py
```

Open the provided `http://localhost:8501` link in your browser.

---

    📊 Features in the Notebook

* Data exploration: shape, columns, missing values
* Cleaning: handling missing data, formatting dates, word counts
* Visualizations:

  * Publications by year
  * Top journals
  * Word frequency in titles
  * Distribution by sources

---

    🌐 Features in the Streamlit App

* Interactive year range filter
* Visualizations (bar charts, word cloud)
* Data preview
* Summary insights

---

    📌 Reflections

* Handling a large dataset was challenging, but working with a sample helped.
* Learned how to debug missing values and format data for analysis.
* Streamlit was simple and effective for creating interactive dashboards.
