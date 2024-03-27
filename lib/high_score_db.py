import sqlite3

def create_table():
    conn = sqlite3.connect('high_score.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS LeaderBoard
                      (id INTEGER PRIMARY KEY, initials TEXT, score INTEGER)''')
    conn.commit()
    conn.close()

def update_leaderboard(initials, score):
    conn = sqlite3.connect('high_score.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO LeaderBoard (initials, score) VALUES (?, ?)", (initials, score))
    conn.commit()
    conn.close()

def get_leaderboard():
    conn = sqlite3.connect('high_score.db')
    cursor = conn.cursor()
    cursor.execute("SELECT initials, score FROM LeaderBoard ORDER BY score ASC LIMIT 3")
    leaderboard = cursor.fetchall()
    result = "LEADERBOARD \n"
    for row in leaderboard:
        for item in row:
            result += " "  * (5 - len(str(item))) + str(item) 
        result += " shots \n"      
    conn.close()
    
    return result + "\n"

# def main():
#     create_table()

#     # Example usage:
#     # Update the database with new initials and score
#     update_leaderboard('AB', 100)
#     update_leaderboard('CD', 150)

#     # Get the entire leaderboard sorted by score in descending order
#     leaderboard = get_leaderboard()
#     print("Leaderboard (sorted by score in descending order):")
#     for row in leaderboard:
#         print(row)

# if __name__ == "__main__":
#     main()
