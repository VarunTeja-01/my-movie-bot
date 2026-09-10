import sqlite3

def create_database():
    # Step 1: Connect to the SQLite database.
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    
    # Step 2: Drop table if it exists to clean up previous schemas
    cursor.execute("DROP TABLE IF EXISTS movies")
    
    # Step 3: Create the 'movies' table.
    # We include 'Title', 'Genre', 'Release_Year', and 'Rating' to showcase the "best of the ratings" requirement.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            Title TEXT NOT NULL,
            Genre TEXT NOT NULL,
            Release_Year INTEGER NOT NULL,
            Rating REAL NOT NULL
        )
    ''')
    
    # Step 4: Define a massive list of 200+ top Telugu movies across Action, Drama, Comedy, Horror, Love, and Fantasy.
    telugu_movies = [
        # --- LOVE (ROMANCE) (35 movies) ---
        ("Sita Ramam", "Love", 2022, 8.6),
        ("Arjun Reddy", "Love", 2017, 8.0),
        ("Geetha Govindam", "Love", 2018, 7.7),
        ("Ye Maaya Chesave", "Love", 2010, 8.1),
        ("Bommarillu", "Love", 2006, 8.3),
        ("Tholi Prema", "Love", 1998, 8.4),
        ("Ninnu Kori", "Love", 2017, 7.6),
        ("Fidaa", "Love", 2017, 7.5),
        ("Ala Modalaindi", "Love", 2011, 7.7),
        ("Arya", "Love", 2004, 7.8),
        ("Arya 2", "Love", 2009, 7.4),
        ("Oohalu Gusagusalade", "Love", 2014, 7.9),
        ("Pelli Choopulu", "Love", 2016, 8.2),
        ("Majili", "Love", 2019, 7.3),
        ("Baby", "Love", 2023, 7.4),
        ("Hi Nanna", "Love", 2023, 8.3),
        ("Uppena", "Love", 2021, 7.1),
        ("Kushi", "Love", 2001, 8.1),
        ("Nuvvu Nenu", "Love", 2001, 7.8),
        ("Jayam", "Love", 2002, 7.2),
        ("Anand", "Love", 2004, 8.1),
        ("Godavari", "Love", 2006, 8.0),
        ("Gunde Jaari Gallanthayyinde", "Love", 2013, 7.3),
        ("Ishq", "Love", 2012, 7.6),
        ("Darling", "Love", 2010, 7.4),
        ("Mr. Perfect", "Love", 2011, 7.2),
        ("Orange", "Love", 2010, 6.7),
        ("Vaana", "Love", 2008, 7.2),
        ("Shyam Singha Roy", "Love", 2021, 7.6),
        ("Jersey", "Love", 2019, 8.5), # Love & Drama
        ("Happy", "Love", 2006, 7.5),
        ("Iddarammayilatho", "Love", 2013, 6.2),
        ("Sashi", "Love", 2021, 6.5),
        ("Malli Malli Idi Rani Roju", "Love", 2015, 8.0),
        ("Chalo", "Love", 2018, 7.0),

        # --- FANTASY (33 movies) ---
        ("Baahubali: The Beginning", "Fantasy", 2015, 8.0),
        ("Baahubali 2: The Conclusion", "Fantasy", 2017, 8.2),
        ("Magadheera", "Fantasy", 2009, 7.7),
        ("Eega", "Fantasy", 2012, 7.7),
        ("Yamadonga", "Fantasy", 2007, 7.3),
        ("Bimbisara", "Fantasy", 2022, 7.1),
        ("Karthikeya 2", "Fantasy", 2022, 8.0),
        ("Jagadeka Veerudu Athiloka Sundari", "Fantasy", 1990, 8.3),
        ("Aditya 369", "Fantasy", 1991, 8.4),
        ("Bhairava Dweepam", "Fantasy", 1994, 8.1),
        ("Anji", "Fantasy", 2004, 6.5),
        ("Ghatothkachudu", "Fantasy", 1995, 7.8),
        ("Arundhati", "Fantasy", 2009, 7.4), # Fantasy/Horror
        ("Damarukam", "Fantasy", 2012, 6.2),
        ("Devi", "Fantasy", 1999, 7.0),
        ("Ammoru", "Fantasy", 1995, 7.6),
        ("Mayabazar", "Fantasy", 1957, 8.9),
        ("Sri Manjunatha", "Fantasy", 2001, 7.5),
        ("Gopala Gopala", "Fantasy", 2015, 7.3),
        ("Nani", "Fantasy", 2004, 6.9),
        ("Srimadvirat Veerabrahmendra Swami Charitra", "Fantasy", 1984, 8.2),
        ("Akhanda", "Fantasy", 2021, 6.9),
        ("Srinivasa Kalyanam", "Fantasy", 2018, 6.5),
        ("Ohmkaram", "Fantasy", 1997, 7.2),
        ("Suvarnabhumi", "Fantasy", 1999, 6.8),
        ("Gouthami Putra Satakarni", "Fantasy", 2017, 7.1),
        ("Khaleja", "Fantasy", 2010, 7.8),
        ("Aravinda Sametha Veera Raghava", "Fantasy", 2018, 7.5),
        ("Radhe Shyam", "Fantasy", 2022, 5.3),
        ("Gaami", "Fantasy", 2024, 7.0),
        ("Hanu-Man", "Fantasy", 2024, 7.9),
        ("Sarkaru Vaari Paata", "Fantasy", 2022, 6.0),
        ("Kalki 2898 AD", "Fantasy", 2024, 7.6),

        # --- HORROR (34 movies) ---
        ("Virupaksha", "Horror", 2023, 7.2),
        ("Masooda", "Horror", 2022, 7.3),
        ("Prema Katha Chitram", "Horror", 2013, 7.5),
        ("Raju Gari Gadhi", "Horror", 2015, 6.8),
        ("Raju Gari Gadhi 2", "Horror", 2017, 5.8),
        ("Ganga (Kanchana 2)", "Horror", 2015, 6.2),
        ("Geethanjali", "Horror", 2014, 7.0),
        ("Deyyam", "Horror", 1996, 7.1),
        ("Anando Brahma", "Horror", 2017, 7.0),
        ("Taxiwala", "Horror", 2018, 7.1),
        ("Bhaagamathie", "Horror", 2018, 7.0),
        ("U-Turn", "Horror", 2018, 7.0),
        ("Kanchana", "Horror", 2011, 6.6),
        ("Muni", "Horror", 2007, 6.3),
        ("Chinna", "Horror", 2023, 8.1),
        ("Polimera", "Horror", 2021, 7.3),
        ("Polimera 2", "Horror", 2023, 7.5),
        ("Pindam", "Horror", 2023, 6.2),
        ("Mangalavaaram", "Horror", 2023, 6.8),
        ("Ekkadiki Pothavu Chinnavada", "Horror", 2016, 7.4),
        ("Kashmora", "Horror", 2016, 6.1),
        ("Avunu", "Horror", 2012, 6.8),
        ("Avunu 2", "Horror", 2015, 5.1),
        ("Jessie", "Horror", 2019, 5.9),
        ("Siva Ganga", "Horror", 2016, 5.3),
        ("Tripura", "Horror", 2015, 5.2),
        ("W/O Ram", "Horror", 2018, 6.9),
        ("Aruvam", "Horror", 2019, 5.4),
        ("Heza", "Horror", 2019, 6.5),
        ("Drishya Kavya", "Horror", 2020, 6.1),
        ("Dhiya", "Horror", 2018, 6.4),
        ("Nenunnanu", "Horror", 2004, 7.1),
        ("Tantra", "Horror", 2024, 6.0),
        ("Yatra", "Horror", 2019, 7.5),

        # --- ACTION (35 movies) ---
        ("RRR", "Action", 2022, 7.8),
        ("Pushpa: The Rise", "Action", 2021, 7.6),
        ("Salaar: Part 1 - Ceasefire", "Action", 2023, 6.5),
        ("Pokiri", "Action", 2006, 8.0),
        ("Chatrapathi", "Action", 2005, 7.7),
        ("Devara: Part 1", "Action", 2024, 7.2),
        ("Okkadu", "Action", 2003, 8.1),
        ("Athadu", "Action", 2005, 8.2),
        ("Vikramarkudu", "Action", 2006, 7.8),
        ("Gabbar Singh", "Action", 2012, 7.1),
        ("Mirchi", "Action", 2013, 7.2),
        ("Srimanthudu", "Action", 2015, 7.5),
        ("Janatha Garage", "Action", 2016, 7.2),
        ("Bharat Ane Nenu", "Action", 2018, 7.5),
        ("Sarileru Neekevvaru", "Action", 2020, 6.2),
        ("Guntur Kaaram", "Action", 2024, 6.1),
        ("Ala Vaikunthapurramuloo", "Action", 2020, 7.2),
        ("Vaikuntapuram", "Action", 1984, 7.4),
        ("Dookudu", "Action", 2011, 7.4),
        ("Business Man", "Action", 2012, 7.1),
        ("Temper", "Action", 2015, 7.4),
        ("Nannaku Prematho", "Action", 2016, 7.6),
        ("Legend", "Action", 2014, 6.8),
        ("Simha", "Action", 2010, 6.9),
        ("Race Gurram", "Action", 2014, 7.3),
        ("Julayi", "Action", 2012, 7.2),
        ("Attarintiki Daredi", "Action", 2013, 7.3),
        ("Waltair Veerayya", "Action", 2023, 6.4),
        ("Veera Simha Reddy", "Action", 2023, 5.2),
        ("Damaka", "Action", 2022, 6.3),
        ("Karthikeya", "Action", 2014, 7.7),
        ("Goodachari", "Action", 2018, 7.8),
        ("Major", "Action", 2022, 8.1),
        ("Wild Dog", "Action", 2021, 6.3),
        ("V", "Action", 2020, 6.9),

        # --- COMEDY (33 movies) ---
        ("Jathi Ratnalu", "Comedy", 2021, 7.3),
        ("Ee Nagaraniki Emaindi", "Comedy", 2018, 7.9),
        ("Nuvvu Naaku Nachav", "Comedy", 2001, 8.8),
        ("Manmadhudu", "Comedy", 2002, 8.3),
        ("Venky", "Comedy", 2004, 8.3),
        ("King", "Comedy", 2008, 7.1),
        ("Ready", "Comedy", 2008, 7.6),
        ("Dubai Seenu", "Comedy", 2007, 7.1),
        ("Dhee", "Comedy", 2007, 8.0),
        ("Aha Naa Pellanta", "Comedy", 1987, 8.7),
        ("Adhurs", "Comedy", 2010, 7.8),
        ("Baadshah", "Comedy", 2013, 6.9),
        ("Mathu Vadalara", "Comedy", 2019, 8.2),
        ("Brochevarevarura", "Comedy", 2019, 8.0),
        ("Agent Sai Srinivasa Athreya", "Comedy", 2019, 8.4),
        ("Chitram Bhalare Vichitram", "Comedy", 1991, 8.3),
        ("Appula Appa Rao", "Comedy", 1992, 8.1),
        ("Jamboo Lakidi Pamba", "Comedy", 1993, 8.2),
        ("April 1st Vidudhala", "Comedy", 1991, 8.0),
        ("Gamyam", "Comedy", 2008, 8.1),
        ("Ami Thumi", "Comedy", 2017, 7.0),
        ("Geetha Arts", "Comedy", 2015, 7.2),
        ("Bhale Bhale Magadivoy", "Comedy", 2015, 7.7),
        ("Kick", "Comedy", 2009, 7.7),
        ("Sudigadu", "Comedy", 2012, 6.7),
        ("Run Raja Run", "Comedy", 2014, 7.3),
        ("Express Raja", "Comedy", 2016, 6.4),
        ("Eedo Rakam Aado Rakam", "Comedy", 2016, 6.8),
        ("F2: Fun and Frustration", "Comedy", 2019, 6.2),
        ("F3: Fun and Frustration", "Comedy", 2022, 5.1),
        ("Om Bheem Bush", "Comedy", 2024, 6.9),
        (" Samajavaragamana", "Comedy", 2023, 7.8),
        ("Mad", "Comedy", 2023, 7.5),

        # --- DRAMA (33 movies) ---
        ("Mahanati", "Drama", 2018, 8.5),
        ("C/o Kancharapalem", "Drama", 2018, 8.9),
        ("Sankarabharanam", "Drama", 1980, 9.0),
        ("Swathi Kiranam", "Drama", 1992, 8.5),
        ("Sagara Sangamam", "Drama", 1983, 8.8),
        ("Prasthanam", "Drama", 2010, 8.1),
        ("Vedam", "Drama", 2010, 8.1),
        ("Kancharapalem", "Drama", 2018, 8.9),
        ("Shathamanam Bhavati", "Drama", 2017, 7.2),
        ("Gamyam", "Drama", 2008, 8.1),
        ("Balagam", "Drama", 2023, 8.1),
        ("Writer Padmabhushan", "Drama", 2023, 7.1),
        ("Sir", "Drama", 2023, 7.3),
        ("Major", "Drama", 2022, 8.1),
        ("Republic", "Drama", 2021, 7.3),
        ("Naandhi", "Drama", 2021, 7.6),
        ("Color Photo", "Drama", 2020, 8.1),
        ("Palasa 1978", "Drama", 2020, 7.4),
        ("Kancharapalem", "Drama", 2018, 8.9),
        ("Mallesham", "Drama", 2019, 8.1),
        ("Leader", "Drama", 2010, 8.0),
        ("Anukokunda Oka Roju", "Drama", 2005, 8.1),
        ("Aa Naluguru", "Drama", 2004, 8.5),
        ("Mithunam", "Drama", 2012, 8.2),
        ("Rudraveena", "Drama", 1988, 8.6),
        ("Subhalekha", "Drama", 1982, 8.1),
        ("Challenge", "Drama", 1984, 8.0),
        ("Karthikeya", "Drama", 2014, 7.7),
        ("Bichagadu", "Drama", 2016, 7.5),
        ("Kshanam", "Drama", 2016, 8.2),
        ("Oopiri", "Drama", 2016, 7.9),
        ("Maharshi", "Drama", 2019, 7.2),
        ("Vakeel Saab", "Drama", 2021, 7.1),

        # --- ADDITIONAL 10 MOVIES SPANNING VARIED YEARS ---
        ("Devadasu", "Love", 1953, 8.3),
        ("Gundamma Katha", "Comedy", 1962, 8.5),
        ("Lava Kusa", "Fantasy", 1963, 8.2),
        ("Bhakta Prahlada", "Fantasy", 1967, 8.0),
        ("Daana Veera Soora Karna", "Fantasy", 1977, 8.6),
        ("Adavi Ramudu", "Action", 1977, 7.8),
        ("Kondaveeti Donga", "Action", 1990, 7.4),
        ("Alluda Majaka", "Comedy", 1995, 7.0),
        ("Murari", "Fantasy", 2001, 7.8),
        ("Simhadri", "Action", 2003, 7.6)
    ]
    
    # Let's clean title names (strip spaces)
    cleaned_telugu_movies = []
    for title, genre, year, rating in telugu_movies:
        cleaned_telugu_movies.append((title.strip(), genre.strip(), year, rating))

    # Step 5: Insert the sample movies into the table.
    cursor.executemany('''
        INSERT INTO movies (Title, Genre, Release_Year, Rating)
        VALUES (?, ?, ?, ?)
    ''', cleaned_telugu_movies)
    
    # Step 6: Commit (save) the changes to the database.
    conn.commit()
    conn.close()
    
    print(f"Database 'movies.db' successfully created and populated with {len(cleaned_telugu_movies)} best of Telugu movies!")

if __name__ == "__main__":
    create_database()
