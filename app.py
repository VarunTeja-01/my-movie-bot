import streamlit as tf
import sqlite3
import pandas as pd

# Set page configuration for a professional layout
tf.set_page_config(
    page_title="Telugu Movie Recommendation Dashboard",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
tf.markdown("""
    <style>
    .main-title {
        font-size: 38px;
        color: #FF4B4B;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 18px;
        color: #555555;
        text-align: center;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# App Titles
tf.markdown('<div class="main-title">🎬 Telugu Movie Recommendation Dashboard</div>', unsafe_allow_html=True)
tf.markdown('<div class="sub-title">Explore, analyze, and find the absolute best-rated Telugu movies!</div>', unsafe_allow_html=True)

# Database Helper Functions
def get_available_genres():
    """Fetches unique genres from movies database."""
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT Genre FROM movies ORDER BY Genre ASC")
    genres = [row[0] for row in cursor.fetchall()]
    conn.close()
    return genres

def get_movies_by_genre(genre):
    """Retrieves all movies for a given genre, sorted by Rating in descending order."""
    conn = sqlite3.connect('movies.db')
    # Using pandas to load SQL query results directly into a DataFrame
    query = """
        SELECT Title, Genre, Release_Year as 'Release Year', Rating 
        FROM movies 
        WHERE UPPER(Genre) = UPPER(?) 
        ORDER BY Rating DESC
    """
    df = pd.read_sql_query(query, conn, params=(genre,))
    conn.close()
    return df

def get_genre_counts():
    """Gets count of movies per genre for data visualization."""
    conn = sqlite3.connect('movies.db')
    query = """
        SELECT Genre, COUNT(*) as 'Movie Count' 
        FROM movies 
        GROUP BY Genre 
        ORDER BY [Movie Count] DESC
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Initialize Sidebar
tf.sidebar.header("🔍 Recommendation Filters")
tf.sidebar.write("Filter the cinematic collection to find matches!")

# Load Genres for Dropdown
try:
    available_genres = get_available_genres()
except sqlite3.OperationalError:
    available_genres = ["Love", "Fantasy", "Horror", "Action", "Comedy", "Drama"]
    tf.sidebar.error("Database 'movies.db' not found. Please run 'setup_db.py' first!")

selected_genre = tf.sidebar.selectbox("Choose a Genre", available_genres)

# Main Screen Layout - Grid of columns
col1, col2 = tf.columns([3, 2])

with col1:
    tf.subheader(f"🏆 Top-Rated {selected_genre} Movies")
    try:
        movies_df = get_movies_by_genre(selected_genre)
        # Display polished interactive dataframe
        tf.dataframe(
            movies_df, 
            use_container_width=True,
            hide_index=True
        )
        tf.success(f"Showing {len(movies_df)} top {selected_genre} movies sorted by rating!")
    except Exception as e:
        tf.error(f"Error fetching movies: {e}")

with col2:
    tf.subheader("📊 Movie Count per Genre")
    try:
        counts_df = get_genre_counts()
        # Set Genre as index for streamlit's built-in bar chart
        chart_data = counts_df.set_index("Genre")
        tf.bar_chart(chart_data)
        
        # Display total database stats in an attractive metric card
        total_movies = counts_df['Movie Count'].sum()
        tf.metric(label="Total Movies in Database", value=int(total_movies))
    except Exception as e:
        tf.error(f"Error generating chart: {e}")

# Database Educational Section
with tf.expander("🎓 Learn SQL: How the database query works under the hood"):
    tf.markdown("""
    ### 1. Retrieving filtered records with custom sorting:
    ```sql
    SELECT Title, Genre, Release_Year, Rating 
    FROM movies 
    WHERE UPPER(Genre) = UPPER(?) 
    ORDER BY Rating DESC
    ```
    * **`SELECT ...`**: Specifies the movie attributes to load.
    * **`WHERE UPPER(Genre) = UPPER(?)`**: Filters the results based on the genre selected in the dropdown sidebar. Case-insensitive matching ensures flawless queries.
    * **`ORDER BY Rating DESC`**: Directs the database to sort the outputs in descending order of rating, ensuring the highest-rated recommendations appear at the top.

    ### 2. Aggregating data for visualization:
    ```sql
    SELECT Genre, COUNT(*) as 'Movie Count' 
    FROM movies 
    GROUP BY Genre
    ```
    * **`COUNT(*)`**: Calculates the number of records (movies) in each category.
    * **`GROUP BY Genre`**: Groups individual movies together by their `Genre` so that `COUNT(*)` counts how many movies belong to each unique genre.
    """)
