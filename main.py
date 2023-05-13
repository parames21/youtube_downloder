from pytube import YouTube

def download_video():
    try:
        url = input("Enter the URL of the video you want to download: ")
        resolution = input("Enter the desired resolution (e.g., 720p): ")
        yt = YouTube(url)
        video = yt.streams.filter(res=resolution).first()
        video.download()
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error:", str(e))

# Example usage
download_video()