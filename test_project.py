from pytube import YouTube # type: ignore
from project import Get_video_itag, Get_audio_itag
import pytest # type: ignore

yt = YouTube("https://www.youtube.com/watch?v=jNQXAC9IVRw")
def test_Get_video_itag():
    assert Get_video_itag(yt) == 18

def test_Get_audio_itag():
    assert Get_audio_itag(yt) == 139