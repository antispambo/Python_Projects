from pytube import YouTube

link = input("Enter your link of youtube video: ")
you_link = YouTube(link)
you_stream = you_link.streams.get_highest_resolution()

print("Downloading...")
# path file
you_stream.download("Download\python")
print("Download completed !!")