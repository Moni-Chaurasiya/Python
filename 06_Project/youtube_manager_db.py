import sqlite3

conn= sqlite3.connect('youtube_videos.db')
cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
    )
''')

def list_all_videos():
    print("\n")
    print("*" * 70)
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    print("\n")
    print("*" * 70)
    
def add_video():
    name=input("Enter video name: ")
    time=input("Enter video time: ")
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?)",(name,time))
    conn.commit()

def update_video():
    index=int(input("Enter the video number to update"))
    name=input("Enter the new video name")
    time=input("Enter the new video time")
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(name,time,index))
    conn.commit()
    
def delete_video():
    index=int(input("Enter the video index to delete"))
    cursor.execute("DELETE FROM videos where id = ?", (index,))
    conn.commit()

def main():
    
    while True:
        print("\n YouTube Manager  | choose an option")
        print("1. List all youtube video")
        print("2. Add a youtube video details")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice=input("Enter your choice")
        
        match choice:
            case '1':
                list_all_videos()
            case '2':
                add_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                break
            case _:
                print("invalid choice")
        
    
    conn.close()
    
if __name__=="__main__":
    main()