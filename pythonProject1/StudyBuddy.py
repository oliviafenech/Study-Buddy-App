import tkinter as tk
from random import random
from tkinter import messagebox


class StudyBuddy:
    def __init__(self, root):
      self.start_timer
      self.root = root
      self.root.title("study buddy")
      self.time_left_in_seconds = 0

        # variables
      self.time_left_in_seconds = 0
      self.paused = False  # Initialize the paused attribute
      self.quote_index = 0  # Keeps track of the current quote index
      self.quotes = [
          "Keep pushing forward!",
          "You're doing great!",
          "Time to rehydrate, drink some water",
          "Posture check: Stop slouching! :)",
          "Stay focused, almost there!",
          "Believe in yourself!",
          "Posture check: Sit up straight!",
          "Remember why you started!"]

        # instructions - how to use study buddy
      self.instructions = tk.Label(root, text = "How long do you want to study? (minutes):")
      self.instructions.pack(pady=10)

      # slider
      self.slider = tk.Scale(root, orient=tk.HORIZONTAL, from_=1, to=120, length=300)
      self.slider.pack(pady=10)
      self.slider.set(25)

        # start button to start timer
      self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer)
      self.start_button.pack(pady=10)

      #pause button
      self.pause_button = tk.Button(root, text="Pause Timer: Task completed early", command=self.pause_timer)
      self.pause_button.pack(pady=5)

        # countdown text
      self.countdown_text = tk.Label(root, text="", font=("Arial", 48), fg="red")
      self.countdown_text.pack()

      # Quote display
      self.quote_label = tk.Label(root, text="", font=("Helvetica", 35, "italic"), fg="Green")
      self.quote_label.pack(pady=10)



    def start_timer(self):
        self.time_left_in_seconds = int(self.slider.get()) * 60
        self.update_timer()
        self.quote_index = 0

    def pause_timer(self):
        self.paused = not self.paused  # Toggle pause state
        if not self.paused:
            self.update_timer()  # Resume timer if unpaused



    def update_timer(self):
     if self.time_left_in_seconds > 0 and not self.paused:
         minutes, seconds = divmod(self.time_left_in_seconds, 60)
         time_formatted = f"{minutes:02d}:{seconds:02d}"
         self.countdown_text.config(text=time_formatted)
         self.time_left_in_seconds -= 1
         self.root.after(1000, self.update_timer)
     else:
         self.countdown_text.config(text="00:00")
         pygame.mixer.music.load("cheering-and-clapping-crowd-1-5995.mp3")
         pygame.mixer.music.play()
         messagebox.showinfo("Yay!!", "You did that! Congrats")
         pygame.mixer.music.stop()


# Display a motivational quote every 5 minutes (300 seconds)
     if self.time_left_in_seconds % 300 == 0 and self.quote_index < len(self.quotes):
                self.show_motivational_quote()
                self.quote_index += 1
                self.root.after(1000, self.update_timer)  # Continue the countdown



    def show_motivational_quote(self):
        # Update the quote label with the next quote in the sequence
        if self.quote_index < len(self.quotes):
            quote = self.quotes[self.quote_index]
            self.quote_label.config(text=quote)
import pygame

pygame.mixer.init()
pygame.mixer.music.load("creative-technology-showreel-241274.mp3")
pygame.mixer.music.play()


if __name__ == '__main__':
    # create our main app window
    root = tk.Tk()
    StudyBuddy(root)
    root.mainloop()