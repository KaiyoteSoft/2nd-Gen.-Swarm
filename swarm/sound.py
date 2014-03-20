import pygame

try:
    import pygame.mixer as mixer
except ImportError:
    import android.mixer as mixer

class Sound():
    def __init__(self):
        self.reload = mixer.Sound("snd/reload_final.wav")
        self.bullet_sound = mixer.Sound("snd/shot_final.wav")
        self.roar = mixer.Sound("snd/monster.wav")

        
    