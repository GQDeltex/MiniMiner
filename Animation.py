import pygame

class Animation(object):
    def __init__(self, duration):
        self.duration = duration
        self.time = 0
        self.current = 0
        
    def update(self, animation_list, time = 1):
        self.time += time
        self.animation_list = animation_list
        if self.time > self.duration:
            self.time = 0
            self.current += 1
            if self.current >= len(self.animation_list):
                self.current = 0
        self.image = self.animation_list[self.current] 
        return self.image