import moviepy.editor
from tkinter.filedialog import *

video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)
audio = video.audio

audio.write_audiofile("sample.mp3")
print("Completed!")