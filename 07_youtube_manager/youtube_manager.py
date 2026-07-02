
import json

def load_videos():
    try:
        with open("youtube.txt","r") as file:
            result = json.load(file)
            return result
    except FileNotFoundError:
        return []

def save_data(videos):
    with open("youtube.txt","w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("-" * 30)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video["name"]}, Duration:{video["time"]}")
    print("-" * 30)
    
def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name":name, "time":time})
    save_data(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {"name":name, "time": time}
        save_data(videos)
    else:
        print("Invalid video number")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        print("Video deleted")
    else:
        print("Invalid video number")

def main():        
    videos = load_videos()
    while True:
        print("------- Youtube Manager | choose an option -------")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")

        choice = input("Select the option: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid option selected")

if __name__ == "__main__":
    main()