
from frontend import pygame, red_team, blue_team
from dataclasses import dataclass
@dataclass
class SoundManager:
    def __init__(self):
        self.eat_sound: pygame.mixer.Sound = pygame.mixer.Sound(r"C:\Users\lusan\OneDrive\Desktop\Machine learning\Lộc\cờ tướng\sound\wav\đớp-mồi.wav")
        self.nervous_sound: pygame.mixer.Sound = pygame.mixer.Sound(r"C:\Users\lusan\OneDrive\Desktop\Machine learning\Lộc\cờ tướng\sound\wav\gây cấn (mp3cut (mp3cut.net).mp3")
        self.intro_sound :  pygame.mixer.Sound = pygame.mixer.Sound(r"C:\Users\lusan\OneDrive\Desktop\Machine learning\Lộc\cờ tướng\sound\wav\intro.wav")
        self.move_trong : pygame.mixer.Sound = pygame.mixer.Sound(r"C:\Users\lusan\OneDrive\Desktop\Machine learning\Lộc\cờ tướng\sound\wav\move-trống.wav")
        self.danh_kiem_sound : pygame.mixer.Sound = pygame.mixer.Sound(r"C:\Users\lusan\OneDrive\Desktop\Machine learning\Lộc\cờ tướng\sound\wav\ăn-đánh-kiếm.wav")
        self.current_channel = None
        
    def eat(self):
        self.eat_sound.play()
        
    def play_nervous(self):
        if self.current_channel is None:
            # self.current_channel.stop()
            self.current_channel = pygame.mixer.find_channel()
            self.current_channel.play(self.nervous_sound, loops=-1)

    def stop_nervous(self):
        if self.current_channel is not None:
            self.current_channel.stop()
            self.current_channel = None
        
    def intro(self):
        self.intro_sound.play()
        
    def move(self):
        self.move_trong.play()
        
    def danh_kiem(self):
        self.danh_kiem_sound.play()
sound_manager = SoundManager()



def gay_can(team, board):
    if team == 'red': # thủ
        count = 0
        for a in range(10):
            for b in range(9):
                if board[a][b] is not None:
                    if a >= 6 and board[a][b] in red_team:
                        count += 1
                        if count >= 4:
                            return True
    if team == 'blue': # thủ
        count = 0
        for a in range(10):
            for b in range(9):
                if board[a][b] is not None:
                    if a <= 3 and board[a][b] in blue_team:
                        count += 1
                        if count >= 4:
                            return True
    return False
# tạo danh sách red team > 