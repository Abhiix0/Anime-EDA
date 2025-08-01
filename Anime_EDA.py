import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Step 1: Load the datasets
    anime_df = pd.read_csv("anime/anime.csv")
    ratings_df = pd.read_csv("anime/rating.csv")

    print("Anime Dataset:")
    print(anime_df.head())
    print("\nRatings Dataset:")
    print(ratings_df.head())

    # Step 2: Understand the data structure
    print("\nShape of Anime Dataset:", anime_df.shape)
    print("Shape of Ratings Dataset:", ratings_df.shape)
    print("\nAnime Dataset Info:")
    print(anime_df.info())
    print("\nRatings Dataset Info:")
    print(ratings_df.info())
    print("\nMissing Values in Anime:")
    print(anime_df.isnull().sum())
    print("\nMissing Values in Ratings:")
    print(ratings_df.isnull().sum())

    # Step 3: Data Cleaning
    # Convert 'episodes' to numeric before dropping rows
    anime_df['episodes'] = pd.to_numeric(anime_df['episodes'], errors='coerce')
    anime_df['episodes'] = anime_df['episodes'].fillna(0).astype(int)
    # Drop rows with missing values in essential columns only
    anime_df = anime_df.dropna(subset=['name', 'genre', 'type', 'rating', 'members'])

    # Clean ratings_df (-1 means user didn’t rate)
    ratings_df['rating'] = ratings_df['rating'].replace(-1, pd.NA)
    ratings_df_clean = ratings_df.dropna().copy()
    ratings_df_clean['rating'] = ratings_df_clean['rating'].astype(float)

    print("\nCleaned Anime Dataset:", anime_df.shape)
    print("Cleaned Ratings Dataset:", ratings_df_clean.shape)

    # Step 4: Merge Anime Data with Ratings Data
    merged_df = pd.merge(ratings_df_clean, anime_df, on='anime_id')
    print("Merged columns:", merged_df.columns)
    print("\nMerged Data Shape:", merged_df.shape)

    # Use the correct column name for rating
    rating_col = "rating"
    if rating_col not in merged_df.columns:
        for col in merged_df.columns:
            if "rating" in col:
                rating_col = col
                break

    # Top Rated Anime
    top_rated = merged_df.groupby("name")[rating_col].mean().sort_values(ascending=False).head(10)
    print("\nTop Rated Anime:")
    print(top_rated)

    # Step 5: Data Visualization & Analysis
    sns.set(style="darkgrid")

    # Genre Popularity (Top 10)
    anime_genres = anime_df.dropna(subset=["genre"]).copy()
    anime_genres["genre"] = anime_genres["genre"].str.split(", ")
    genres_exploded = anime_genres.explode("genre")
    genre_counts = genres_exploded["genre"].value_counts().head(10)

    plt.figure(figsize=(10,6))
    sns.barplot(x=genre_counts.values, y=genre_counts.index, palette="rocket")
    plt.title("Top 10 Most Common Anime Genres")
    plt.xlabel("Number of Shows")
    plt.ylabel("Genre")
    plt.tight_layout()
    plt.show()
    plt.close()

    # Top 10 Most Rated Anime by Users
    most_rated = merged_df["name"].value_counts().head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=most_rated.values, y=most_rated.index, palette="mako")
    plt.title("Most Rated Anime by Users")
    plt.xlabel("Number of Ratings")
    plt.ylabel("Anime")
    plt.tight_layout()
    plt.show()
    plt.close()

    # Rating Distribution of All Anime
    plt.figure(figsize=(8,5))
    sns.histplot(anime_df["rating"].dropna(), bins=30, kde=True, color="skyblue")
    plt.title("Distribution of Anime Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Number of Shows")
    plt.tight_layout()
    plt.show()
    plt.close()

    # Average Rating by Type (TV, Movie, OVA, etc.)
    avg_rating_by_type = anime_df.groupby("type")["rating"].mean().sort_values(ascending=False)
    plt.figure(figsize=(8,6))
    sns.barplot(x=avg_rating_by_type.values, y=avg_rating_by_type.index, palette="coolwarm")
    plt.title("Average Rating by Anime Type")
    plt.xlabel("Average Rating")
    plt.ylabel("Type")
    plt.tight_layout()
    plt.show()
    plt.close()

    # Step 6: Further Analysis
    # Top genres by average rating
    genre_df = merged_df.copy()
    genre_df['genre'] = genre_df['genre'].str.split(', ')
    genre_df = genre_df.explode('genre')
    top_genres = genre_df.groupby('genre')[rating_col].mean().sort_values(ascending=False).head(10)
    print("\nTop Rated Genres:")
    print(top_genres)

    # Most watched anime by member count
    top_watched = anime_df.sort_values('members', ascending=False).head(10)
    print("\nMost Watched Anime:")
    print(top_watched[['name', 'members', 'rating']])

    # Most frequently rated anime
    most_rated = merged_df['name'].value_counts().head(10)
    print("\nMost Frequently Rated Anime:")
    print(most_rated)

    # Anime types sorted by average rating
    type_ratings = merged_df.groupby("type")[rating_col].mean().sort_values(ascending=False)
    print("\nAnime Type Ratings:")
    print(type_ratings)

    # Distribution of ratings (how many times each score appears)
    rating_dist = merged_df[rating_col].value_counts().sort_index()
    print("\nRating Distribution:")
    print(rating_dist)

    # Step 7: Function to recommend anime by genre
    def recommend_by_genre(genre_name, top_n=10):
        genre_filtered = merged_df[merged_df['genre'].str.contains(genre_name, case=False, na=False)]
        genre_grouped = genre_filtered.groupby("name")[rating_col].mean()
        top_anime = genre_grouped.sort_values(ascending=False).head(top_n)
        return top_anime

    # Test the function!
    print("\n🔍 Top Mystery Anime:")
    print(recommend_by_genre("Mystery"))
    print("\n🔍 Top Romance Anime:")
    print(recommend_by_genre("Romance"))

if __name__ == "__main__":
    main()
