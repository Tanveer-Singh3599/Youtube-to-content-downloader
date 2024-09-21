import pytubefix
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from os import remove

#Taking url Input from user (Youtube link).
URL = input("Enter URL: ")
Var = pytubefix.YouTube(URL)

#Block of code to print title and age restricted details about given url.
print(f"The url you entered is of vidoe titled ({Var.title}).")
x = input("Want to continue?  Y/n: ").lower()

#Block of code will execute if user agrees to continue.
if x == "y":
    #Taking inputs from user about format and quality.
    format = input("Enter 'a' for audio(mp3) and 'v' for video(mp4): ").lower()
    
    #Download Audio files.
    if format == "a":
        stream = Var.streams.filter(only_audio=True).order_by('abr').last()
        stream.download()
        print("Audio file download successfully.")
    
    #Download Video files.
    else:
        
        while True: 
            Video_quality = input("Enter Video Quality in pixels: ")
            res=f"{Video_quality}p"
            stream = Var.streams.filter(type="video", res=res, progressive="True")
            print(stream)
            #Block of code will execute if the given Video Quality is available.
            try:
                Video_Stream = Var.streams.filter(type="video", res=res).first()
                Audio_Stream = Var.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').first()
                
                video = Video_Stream.download(filename="vid.mp4")
                audio = Audio_Stream.download(filename="aud.mp4")
                
                video_clip = VideoFileClip("vid.mp4")
                audio_clip = AudioFileClip("aud.mp4")
                
                name = f"{Var.title}.mp4"
                vid = video_clip.set_audio(audio_clip)
                vid.write_videofile(name)
                
                remove("vid.mp4")
                remove("aud.mp4")
                break
            
            except AttributeError:
                print("Video does not have Video Quality you entered. Try with some other Video Quality.")