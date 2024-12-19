from pytube import YouTube

def download_youtube_video(url):
    try:
        # Create YouTube object
        yt = YouTube(url)
        
        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()
        
        # Display video details
        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")
        print(f"Length: {yt.length} seconds")
        print(f"Rating: {yt.rating}")
        
        # Download the video
        print("Downloading...")
        video_stream.download()
        print("Download completed!")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    download_youtube_video(url)
