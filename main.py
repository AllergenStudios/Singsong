import time
from rich import print
import pyglet
import yt_dlp


window = pyglet.window.Window()

window.set_visible(False)

print("[blue]Singsong 1.0[/blue]")

def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

print("[bright_blue]Command list can be found on the Github.[/bright_blue]")

while True:

    logfile = open('C:\\Users\\coone\\AppData\\Roaming\\com.modrinth.theseus\\profiles\\Client Tweaks\\logs\\latest.log', "r")
    loglines = follow(logfile)
    for line in loglines:
        if 'startsong' in line:
            try:
                print(line)
                music = pyglet.resource.media("dlaudio.mp3")
                player = music.play()
            except Exception as exception:
                print(f"[red]Error occured while attempting to start/play a song, [/red]\n + {exception}")
        if 'pausesong' in line:
            try:
                player.pause()
            except Exception as exception:
                print(f"[red]Error occured while attempting to stop/pause a song, [/red]\n + {exception}")
        if 'resumesong' in line:
            try:
                player.play()
            except Exception as exception:
                print(f"[red]Error occured while attempting to resume a song, [/red]\n + {exception}")
        if 'downloadsong' in line:
            try:
                argument = line.split("downloadsong ",1)[1].replace("\n","")
                def download_audio(link):
                    import os
                    if os.path.exists("dlaudio.mp3"):
                        os.remove("dlaudio.mp3")
                    with yt_dlp.YoutubeDL(
                            {'extract_audio': True, 'format': 'bestaudio', 'outtmpl': 'dlaudio.mp3'}) as video:
                        info_dict = video.extract_info(link, download=True)
                        video_title = info_dict['title']
                        print(video_title)
                        video.download(link)
                        print(f"Successfully downloaded {video_title} from Youtube as dlaudio.mp3.")


                download_audio(argument)
            except Exception as exception:
                print(f"[red]Error occured while attempting to download a song.[/red]\n + {exception}")
if __name__ == "__main__":
    pyglet.app.run