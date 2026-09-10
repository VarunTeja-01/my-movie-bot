import sqlite3

def run_movie_bot():
    print("=" * 65)
    print("        WELCOME TO THE TELUGU MOVIE RECOMMENDATION BOT       ")
    print("=" * 65)
    print("Explore the absolute best-rated Telugu movies ever made!")
    print("Search by genre: Love, Fantasy, Horror, Action, Comedy, or Drama.")
    print("Type 'exit' or 'quit' at any time to close the bot.")
    print("-" * 65)

    while True:
        # Step 1: Prompt the user for input.
        user_input = input("\nWhat genre of movie are you looking for? ").strip()
        
        # Step 2: Check if the user wants to exit.
        if user_input.lower() in ['exit', 'quit']:
            print("\nThank you for using the Telugu Movie Recommendation Bot! Goodbye!\n")
            break

        if not user_input:
            print("Please enter a valid genre (e.g., Action, Love, Fantasy, Horror, Comedy, Drama).")
            continue

        # Step 3: Connect to the 'movies.db' database file.
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()

        # Step 4: Execute a SELECT query with filtering and sorting.
        # How SQL commands work here:
        # - SELECT Title, Genre, Release_Year, Rating: Retrieve these columns from the movies table.
        # - FROM movies: Selects from our 'movies' table.
        # - WHERE UPPER(Genre) = UPPER(?): Filters by genre case-insensitively using the safe parameter '?'.
        # - ORDER BY Rating DESC: Sorts results by rating in descending order to show the "best of the ratings" first!
        query = """
            SELECT Title, Genre, Release_Year, Rating 
            FROM movies 
            WHERE UPPER(Genre) = UPPER(?) 
            ORDER BY Rating DESC
        """
        
        # Execute query safely with user's input as a tuple parameter.
        cursor.execute(query, (user_input,))
        
        # Step 5: Fetch all matching rows.
        results = cursor.fetchall()
        
        # Step 6: Close the connection.
        conn.close()

        # Step 7: Print the results in a gorgeous, highly organized tabular layout.
        if results:
            print(f"\nFound {len(results)} top-rated movie(s) in the '{user_input}' genre:")
            print("=" * 70)
            print(f"{'S.No':<5} | {'Title':<40} | {'Year':<6} | {'Rating ⭐':<8}")
            print("-" * 70)
            for idx, (title, genre, year, rating) in enumerate(results, 1):
                print(f"{idx:<5} | {title:<40} | {year:<6} | {rating:<8.1f}")
            print("=" * 70)
        else:
            print(f"\nSorry, no movies found for the genre '{user_input}'.")
            
            # Helper: show available genres dynamically.
            try:
                conn = sqlite3.connect('movies.db')
                cursor = conn.cursor()
                cursor.execute("SELECT DISTINCT Genre FROM movies ORDER BY Genre ASC")
                available_genres = [row[0] for row in cursor.fetchall()]
                conn.close()
                
                if available_genres:
                    print(f"Try searching for one of these genres: {', '.join(available_genres)}")
            except sqlite3.OperationalError:
                print("Tip: Make sure to run 'setup_db.py' first to create and populate the database!")

if __name__ == "__main__":
    run_movie_bot()
