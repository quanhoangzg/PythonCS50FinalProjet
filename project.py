from pytube import YouTube # type: ignore # type: ignore
from pydub import AudioSegment # type: ignore
import os
import sys


def main():
    link = input("Enter a Youtube video link: ")
    yt = take_youtube(link)
    title = yt.title
    print(title)
    id_video = Get_video_itag(yt)
    id_audio = Get_audio_itag(yt)
    while True:
        vid = input("Do you want to download a mp4 video (Yes/No)? ")
        if vid.lower() in ['y','yes']:
            download_videos(id_video, yt)
        au = input("Do you want to download a mp3 audio (Yes/No)? ")
        if au.lower() in ['y','yes']:
            download_audio(id_audio, yt)
        print("Thank you or downloading!")
        break

def take_youtube(link):
    try: 
        yt = Youtube_video(link)
    except:
        sys.exit("Not a youtube video url!")

    return yt

def Youtube_video(link: str):
    return YouTube(
        link,
        use_oauth=False,
        allow_oauth_cache=True
    )



def Get_video_itag(yt: YouTube): 
    return yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().itag

def Get_audio_itag(yt: YouTube):
    return yt.streams.filter(only_audio=True).first().itag

def download_videos(id_video, yt):
    video_to_download = yt.streams.get_by_itag(id_video)
    Voutput_path = 'Videos'
    video_to_download.download(Voutput_path)

def download_audio(id_audio, yt):
    #Audio Stream
    audio_stream = yt.streams.get_by_itag(id_audio)

    #temporary audio.mp4 ifle
    title = yt.title
    temp_audio_file = 'Audios/audio_temp.mp4'
    output_mp3_file = f'Audios/{title}.mp3'

    # Download audio mp4 file
    Aoutput_path = 'Audios'
    audio_stream.download(filename="audio_temp.mp4", output_path=Aoutput_path)

    #convert mp4 to mp3:
    audio = AudioSegment.from_file(temp_audio_file)
    audio.export(output_mp3_file, format="mp3")

    #remove temp mp4 file:
    os.remove(temp_audio_file)

if __name__ == "__main__":
    main()