# 📊 Anime EDA Project

Welcome to the **Anime Exploratory Data Analysis (EDA)** project! Dive deep into anime trends, viewer preferences, and ratings using Python, Pandas, and Seaborn.

---

## 📁 Dataset Overview

### 1. `anime.csv`

| Column    | Description                                                         |
| --------- | ------------------------------------------------------------------- |
| anime\_id | Unique ID from MyAnimeList                                          |
| name      | Full name of the anime                                              |
| genre     | Comma-separated list of genres                                      |
| type      | Format of anime (TV, Movie, OVA, etc.)                              |
| episodes  | Number of episodes (can be '?' for unknown)                         |
| rating    | Average community rating out of 10                                  |
| members   | Number of MyAnimeList users who have added this anime to their list |

### 2. `rating.csv`

| Column    | Description                                               |
| --------- | --------------------------------------------------------- |
| user\_id  | Anonymized ID of the user                                 |
| anime\_id | Anime rated by the user (matches with `anime.csv`)        |
| rating    | Rating given by the user (-1 means watched but not rated) |

---

## 🔧 Tech Stack

* Python 🐍
* Pandas
* Matplotlib
* Seaborn

---

## 🧠 Key Steps Performed

### ✅ Step 1: Load the Data

* Loaded both CSVs with `pd.read_csv()`
* Peeked at the first few rows to understand the structure

### ✅ Step 2: Data Understanding

* Inspected shapes, data types, and null values using `.info()` and `.isnull()`

### ✅ Step 3: Cleaning

* Dropped rows with missing data in `anime_df`
* Cleaned "episodes" column by replacing `?` with `0` and converting to `int`
* Replaced `-1` ratings in `rating.csv` with `NaN` and dropped them

### ✅ Step 4: Merge Datasets

* Merged `anime_df` and cleaned `ratings_df` on `anime_id`

### ✅ Step 5: Visualization

* **Top 10 Genres** by frequency
* **Most Rated Anime** by user count
* **Rating Distribution** across all anime
* **Average Rating by Type** (TV, OVA, Movie, etc.)

### ✅ Step 6: Deeper Insights

* **Top Rated Genres** (based on user ratings)
* **Most Watched Anime** (by member count)
* **Rating Distribution Counts**
* **Genre-based Recommender Function** to get the top anime for a given genre

---

## 🔍 Sample Insights

### 🎯 Top Genres by Rating

```
Mystery > Psychological > Drama > Seinen > Thriller...
```

### 💥 Most Watched Anime

* Naruto
* Death Note
* One Piece
* Attack on Titan

### 🧠 Top 10 Rated Anime (User-Driven)

* Shiroi Zou
* Robotan
* Play Ball 2nd
  ...

---

## 🧪 Try It Yourself

Clone the repo, install dependencies, and run:

```bash
python Anime_EDA.py
```

Make sure `anime.csv` and `rating.csv` are inside the `anime/` folder.

---

## 💡 Bonus Feature: Recommend Anime by Genre

Use the function:

```python
def recommend_by_genre("Romance")
```

To get top-rated anime in that genre!

---

## 📦 Data Management (Git LFS Powered)

This repo uses **[Git Large File Storage (Git LFS)](https://git-lfs.github.com/)** to handle the large `rating.csv` file (\~100MB).

### How to Clone Correctly

```bash
git clone https://github.com/Abhiix0/Anime-EDA.git
cd Anime-EDA
git lfs install
git lfs pull
```

If you skip LFS, the dataset may be missing!

---

## 🚀 Future Improvements

* Add an interactive Dash/Streamlit dashboard
* Build a collaborative filtering recommender system
* Deploy as a portfolio project

---

## 🧠 Made by Abhi

> "Analyze the patterns, observe the chaos. Every anime has data, and every dataset has a story."

---

**🌀 GitHub Repo:** [github.com/Abhiix0/Anime-EDA](https://github.com/Abhiix0/Anime-EDA)
