def download_video(url):
    # Options for downloading
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download best video + best audio
        'outtmpl': '%(title)s.%(ext)s',        # Save with the video title
    }

    # Use yt-dlp to download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the video URL: ")
    download_video(video_url)