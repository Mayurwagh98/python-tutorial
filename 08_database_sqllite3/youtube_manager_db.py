import sqlite3

connection = sqlite3.connect("youtube_videos.db")

cursor = connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_videos():
    name = input("Enter the video name: ")
    time = input("Enter the video time: ")
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    connection.commit()
    print("Video added successfully!")

def update_videos():
    video_id = input("Enter the video id: ")
    new_name = input("Enter the new video name: ")
    new_time = input("Enter the new video time: ")
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    connection.commit()
    print("Video updated successfully!")

def delete_videos():
    video_id = input("Enter the video id: ")
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    connection.commit()
    print("Video deleted successfully!")

def main():
    while True:
        print("Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. exit app")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_videos()
            case "2":
                add_videos()
            case "3":
                update_videos()
            case "4":
                delete_videos()
            case "5":
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()