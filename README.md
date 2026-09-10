import streamlit as str
import sqlite3

# 1. Page Configuration
str.set_page_config(page_title="GTM Movie Analytics Dashboard", layout="wide")
str.title("🎬 Movie Recommendation & Analytics Bot")
str.markdown("---")

# 2. Database Helper Function
def query_db(sql_command, params=()):
    # Connects directly to our local SQL database file
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(sql_command, params)
    data = cursor.fetchall()
    conn.close()
    return data

# 3. Sidebar Filter UI
str.sidebar.header("📊 Filter Controls")
# Get unique genres from SQL database to populate the dropdown dynamically
genres_data = query_db("SELECT DISTINCT Genre FROM movies")
genres_list = [row[0] for row in genres_data]

selected_genre = str.sidebar.selectbox("Select a Movie Genre:", ["All Genres"] + genres_list)

# 4. Main Query Logic
if selected_genre == "All Genres":
    results = query_db("SELECT Title, Genre, Release_Year FROM movies ORDER BY Release_Year DESC")
else:
    results = query_db("SELECT Title, Genre, Release_Year FROM movies WHERE Genre = ? ORDER BY Release_Year DESC", (selected_genre,))

# 5. Display the Interactive Data Table
str.subheader(f"🍿 Recommendations for: {selected_genre}")
if results:
    # Convert raw SQL tuples into a clean dictionary layout for Streamlit's data table
    formatted_data = [{"Title": row[0], "Genre": row[1], "Release Year": row[2]} for row in results]
    str.dataframe(formatted_data, use_container_width=True)
else:
    str.warning("No movies found for this category.")

# 6. Analytics Visual Chart Section
str.markdown("---")
str.subheader("📈 Inventory Metrics (Movies per Genre)")
chart_data = query_db("SELECT Genre, COUNT(*) FROM movies GROUP BY Genre")

if chart_data:
    # Transform SQL count metrics into a chart dictionary format
    genre_counts = {row[0]: row[1] for row in chart_data}
    str.bar_chart(genre_counts)
