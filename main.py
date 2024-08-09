import customtkinter as ctk
import os
import pygame
import random

pygame.mixer.init()
app = ctk.CTk()
app.title('Music Player')
app.geometry('600x400')

name_music = ctk.CTkLabel(app, text = 'Music name', font = ('Arial', 20))
name_music.place(y = 150, x = 375, anchor = 'center')
button_frame = ctk.CTkFrame(app)
button_frame.place(y = 200, x = 375, anchor = 'center')
is_pause = False
is_repeat = False
list_music = []
files = os.listdir(os.path.abspath(__file__ + '/../music'))
for i in files:
    list_music.append(os.path.abspath(__file__ + '/../music/' + i))
print(list_music)
index_music = 0
def load_music():
    global index_music
    pygame.mixer.music.load(list_music[index_music])
    name_music.configure(text = f'{list_music[index_music].split('/')[-1].split('.')[0]}')

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
    global index_music, is_pause
    if index_music == 0:
        pass
    else:
        index_music -= 1
        load_music()
    is_pause = False
    button_pause.configure(text = 'Pause')
    pygame.mixer.music.play()
def next_music():
    global index_music, is_pause
    index_music += 1
    if index_music >= len(list_music):
        index_music = 0
    is_pause = False
    button_pause.configure(text = 'Pause')
    load_music()
    pygame.mixer.music.play()
    
def music_check():
    if not pygame.mixer.music.get_busy() and is_pause == False:
        if is_repeat == False:
            load_music()
            pygame.mixer.music.play()
        else:
            next_music()
    app.after(1000, music_check)
def repeat_music():
    global is_repeat
    if is_repeat == False:
        button_repeat.configure(text = 'Change music')
    else:
        button_repeat.configure(text = 'Repeat')
    is_repeat = not is_repeat
def create_music_list():
    for i in files:
        index_music = files.index(i)
        button_music = ctk.CTkButton(frame_music, text = i.split('.')[0], height = 30, width = 150, command = lambda id = index_music: music_play(id))
        list_music_button.append(button_music)
        button_music.grid(row = index_music, column = 0, pady = 10, padx = 10)
button_repeat = ctk.CTkButton(app, text = 'Repeat', command = repeat_music)
button_repeat.place(y = 250, x = 375, anchor = 'center')
def mix_music():
    global index_music
    current_music = list_music[index_music]
    random.shuffle(files)
    list_music.clear()
    for i in files:
        list_music.append(os.path.abspath(__file__ + '/../music/' + i))
    index_music = list_music.index(current_music)
    list_music_button.clear()
    for button in frame_music.winfo_children():
        button.destroy()
    create_music_list()
button_mix = ctk.CTkButton(app, text = 'Mix', width = 70, command = mix_music)
button_mix.place(y = 250, x = 250, anchor = 'center')

button_prev = ctk.CTkButton(button_frame, text = '<<', width = 20, command = prev_music)
button_prev.grid(row = 0, column = 0, padx = 10)
button_pause = ctk.CTkButton(button_frame, text = 'Pause', command= pause_music)
button_pause.grid(row = 0, column = 1, padx = 10)
button_next = ctk.CTkButton(button_frame, text = '>>', width = 20, command = next_music)
button_next.grid(row = 0, column = 2, padx = 10)
list_music_button = []
frame_music = ctk.CTkFrame(app, width = 200, height = 400)
frame_music.place(x = 0, y = 0)

def set_volume(volume):
    pygame.mixer.music.set_volume(volume)
volume_slider = ctk.CTkSlider(app, width = 15, height = 200, command = set_volume, orientation = 'vertical')
volume_slider.place(x = 540, y = 100)

def music_play(music_id):
    global index_music, is_pause
    index_music = music_id
    is_pause = False
    button_pause.configure(text = 'Pause')
    load_music()
    pygame.mixer.music.play()
# class Music_button:
#     def __init__(self, name, music_id):
#         self.button_music = ctk.CTkButton(frame_music, text = name.split('.')[0], height = 30, width = 150, command = self.music_play)
#         self.music_id = music_id
#     def music_play(self):
#         global index_music, is_pause
#         index_music = self.music_id
#         is_pause = False
#         button_pause.configure(text = 'Pause')
#         load_music()
#         pygame.mixer.music.play()
create_music_list()
load_music()
pygame.mixer.music.play()
app.after(1000, music_check)
app.mainloop()