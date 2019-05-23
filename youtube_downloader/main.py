from tkinter import *
import pytube
from pytube import YouTube
from moviepy.editor import *
import os
import time


class Program:
  def __init__(self):
    self.root = Tk()
    self.root.title('YouTube Downloader')

    # Get path of the current working directory for saving downloads
    self.dir_path = os.path.dirname(os.path.abspath(__file__))
    
    self.set_layout()

    self.root.mainloop()

  def set_layout(self):
    # Frame for buttons
    button_frame = Frame(self.root)
    button_frame.grid(row=3, column=1)

    # Label for displaying current program status/action
    self.display = Label(self.root, text='Input link below', fg='black')

    # Creating components of layout
    link = Label(self.root, text='Link')
    link_e = Entry(self.root, width=40)
    directory = Label(self.root, text='Save directory')
    directory_e = Entry(self.root, width=40, text=self.dir_path)
    mp3_button = Button(button_frame, text='MP3', command=lambda: 
                        self.download(link_e.get(), directory_e.get(), True))
    mp4_button = Button(button_frame, text='MP4', command=lambda:
                        self.download(link_e.get(), directory_e.get(), False))
    clear_button = Button(button_frame, text='Clear', command=lambda: 
                          link_e.delete(0, 'end'))

    # Arranging components of layout
    self.display.grid(row=0, column=1, padx=10, pady=(10, 5))
    link.grid(row=1, column=0, padx=10, pady=(5, 5), sticky=E)
    link_e.grid(row=1, column=1, padx=10, pady=(5, 5))
    directory.grid(row=2, column=0, padx=10, pady=(5, 5), sticky=E)
    directory_e.grid(row=2, column=1, padx=10, pady=(5, 5))
    mp3_button.grid(row=3, column=0, padx=10, pady=(5, 10))
    mp4_button.grid(row=3, column=1, padx=10, pady=(5, 10))
    clear_button.grid(row=3, column=2, padx=10, pady=(5, 10))

    # Insert current dir path to the entry
    directory_e.insert(0, self.dir_path)

  def download(self, url, dir_path, mp3):
    # Update dir path
    self.dir_path = dir_path

    try:
      self.yt = YouTube(url)

      # Get a stream with the best quality
      stream = self.yt.streams.filter(file_extension='mp4').first()

      self.display_info('blue', 'Downloading')

      if mp3:
        self.file_name = '{}_mp3'.format(self.yt.title)
      else:
        self.file_name = self.yt.title

      stream.download(output_path=self.dir_path, filename=self.file_name)

      self.file_name += '.mp4'

      if mp3:
        self.convert_to_mp3()

      self.display_info('green', 'Saved as {}'.format(self.file_name))

    except pytube.exceptions.RegexMatchError:
      self.display_info('red', 'The link is invalid')

    except FileNotFoundError:
      self.display_info('red', 'The save directory doesn\'t exist')

    self.freeze_and_reset_display()

  def convert_to_mp3(self):
    self.display_info('blue', 'Converting')
    # Load mp4 file
    video = VideoFileClip(os.path.join(self.dir_path, self.file_name))
    # Storing file name with mp4 extension in order to remove it in
    # the future
    file_to_remove = os.path.join(self.dir_path, self.file_name)
    # Change extension to mp3
    self.file_name = self.file_name[:-1].replace('_mp3', '') + '3'
    # Extract audio from the file
    video.audio.write_audiofile(os.path.join(self.dir_path, self.file_name))
    # Remove the mp4 file
    os.remove(os.path.join(self.dir_path, file_to_remove))
        
  def freeze_and_reset_display(self):
    # Display info for 1.5 seconds, then reset the display message
    time.sleep(1.5)
    self.display_info('black', 'Input link below')

  def display_info(self, fg, text):
    self.display['fg'] = fg
    self.display['text'] = text
    self.root.update()


def main():
  program = Program()


if __name__ == '__main__':
  main()