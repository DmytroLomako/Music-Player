import customtkinter as ctk
import os
import pygame

pygame.mixer.init()
app = ctk.CTk()
app.title('Music Player')
app.geometry('400x400')

name_music = ctk.CTkLabel(app, text = 'Music name', font = ('Arial', 20))
name_music.pack(pady = 50)
button_frame = ctk.CTkFrame(app)
button_frame.pack()
is_pause = False

list_music = [
    os.path.abspath(__file__ + '/../music/better-day-186374.mp3'),
    os.path.abspath(__file__ + '/../music/perfect-beauty-191271.mp3'),
    os.path.abspath(__file__ + '/../music/sweet-serenade-222444.mp3')
]
index_music = 0
def load_music():
    global index_music
    pygame.mixer.music.load(list_music[index_music])
    name_music.configure(text = f'{list_music[index_music].split('/')[-1]}')

def pause_music():
    global is_pause
    if is_pause == False:
        pygame.mixer.music.pause()
        is_pause = True
        button_pause.configure(text = 'Play')
    else:
        pygame.mixer.music.unpause()
        is_pause = False
        button_pause.configure(text = 'Pause')
def prev_music():
    global index_music
    if index_music == 0:
        pass
    else:
        index_music -= 1
        load_music()
    pygame.mixer.music.play()
def next_music():
    global index_music
    index_music += 1
    if index_music >= len(list_music):
        index_music = 0
    load_music()
    pygame.mixer.music.play()

button_prev = ctk.CTkButton(button_frame, text = '<<', width = 20, command = prev_music)
button_prev.grid(row = 0, column = 0, padx = 10)
button_pause = ctk.CTkButton(button_frame, text = 'Pause', command= pause_music)
button_pause.grid(row = 0, column = 1, padx = 10)
button_next = ctk.CTkButton(button_frame, text = '>>', width = 20, command = next_music)
button_next.grid(row = 0, column = 2, padx = 10)
load_music()
pygame.mixer.music.play()
app.mainloop()