import os
import pygame

BASE_IMG_PATH = "data/images/"

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + "/" + img_name))
    return images

class Animation:
    def __init__(self, images, frame_duration = 5, loop = True):
        self.images = images
        self.frame_duration = frame_duration
        self.loop = loop
        self.done = False
        self.frame = 0
    
    def copy(self):
        return Animation(self.images, self.frame_duration, self.loop)
    
    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.frame_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.frame_duration * len(self.images) - 1)
            if self.frame >= self.frame_duration * len(self.images) - 1:
                self.done = True

    def img(self):
        return self.images[int(self.frame / self.frame_duration)]