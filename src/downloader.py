import os
import yt_dlp


DOWNLOADS = os.path.join(os.path.expanduser("~"),  "Downloads")


def download_mp3(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(DOWNLOADS, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        
def download_mp4(url, resolution):
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<={resolution}]+bestaudio/best',
        'outtmpl': os.path.join(DOWNLOADS, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        
def main():
    while True:
        url = input("Enter a Youtube URL[q to quit]: ").strip()
        if url.lower() == 'q':
            break
        
        confirm = input(f"You entered: {url}. Is this correct? (y/n): ").strip().lower()
        if confirm == 'y':
        
            print("\nChoose format to download:")
            print("1 = MP3")
            print("2 = MP4")

            choice = input("Enter your choice: ").strip()
        
            if choice == '1':
                download_mp3(url)
            elif choice == '2':
                print("\nChoose resolution:")
                print("1 = 720p")
                print("2 = 1080p")
                print("3 = 1440p")
                print("4 = 2160p")
                res_choice = input("Enter desired resolution: ").strip()
                if res_choice == '1':
                    download_mp4(url, resolution='720')
                elif res_choice == '2':
                    download_mp4(url, resolution='1080')
                elif res_choice == '3':
                    download_mp4(url, resolution='1440')
                elif res_choice == '4':
                    download_mp4(url, resolution='2160')
                else:
                    print("Invalid resolution choice.")
            else:
                print("Invalid format choice.")
        elif confirm == 'n':
            print("Please re-enter the URL.")
            continue
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

        
if __name__ == "__main__":
    main()