from pytube import Playlist, extract
import os

playlist_link = "https://youtube.com/playlist?list=PLWrhnsc6CvcqIT6eFANBxu0ltSjpm1oXI&si=8cva1nPVCp7_RZLY"
download_path = "./data_root/main/"
# filelist_path = "./filelists/"

playlist = Playlist(playlist_link)

for i in range(10):
    yt = playlist.videos[i]
    video = yt.streams.filter(progressive=True, file_extension="mp4").get_lowest_resolution()
    # audio = yt.streams.filter(only_audio=True).first()
    video_id = extract.video_id(playlist.video_urls[i])
    if i <= 7:
        video.download(output_path=f"{download_path}/train", filename=f"{video_id}.mp4")
        with open(f"./filelists/train.txt", "a") as f:
                f.write("data_root/"+video_id+"\n")
    if i == 8:
        video.download(output_path=f"{download_path}/val", filename=f"{video_id}.mp4")
        with open(f"./filelists/val.txt", "a") as f:
                f.write("data_root/"+video_id+"\n")
    elif i == 9:
        video.download(output_path=f"{download_path}/test", filename=f"{video_id}.mp4")
        with open(f"./filelists/test.txt", "a") as f:
                f.write("data_root/"+video_id+"\n")
    # audio.download(output_path="./audio/", filename=f"{video_id}.wav")
    print(f"Done video {i}")
