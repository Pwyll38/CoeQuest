import pygame
import sys
import random
import noise
import math
import numpy

pygame.init()

clock = pygame.time.Clock()

#Window----------------------------------------------------------------------------------------------------

WINDOW_SIZE = (800,600)
DISPLAY_SIZE = (300,200)

pygame.display.set_caption("The Coelacanths mediocre quest for survival")
win = pygame.display.set_mode(WINDOW_SIZE, 0, 0)
display = pygame.Surface(DISPLAY_SIZE)

#Sound Effects----------------------------------------------------------------------------------------------

boss_music = pygame.mixer.music.load("Assets\Hayloft 8-BIT.mp3") #by NoseRice
#pygame.mixer.music.set_volume(0.2)
#pygame.mixer.music.play(-1)


#Images and fonts-------------------------------------------------------------------------------------------

time_cave_image = pygame.image.load("Assets\Time_cave.png").convert_alpha()
time_cave_empty_image = pygame.image.load("Assets\Time_cave_empty.png").convert_alpha()
cave_clock_image = pygame.image.load("Assets\cave_clock.png").convert_alpha()

coe_image_1 = pygame.image.load("Assets\Coelacanth_1.png").convert_alpha()
coe_image_2 = pygame.image.load("Assets\Coelacanth_2.png").convert_alpha()
coe_image_3 = pygame.image.load("Assets\Coelacanth_3.png").convert_alpha()

coe_img_list = [coe_image_1,coe_image_2,coe_image_1,coe_image_3]

dirt_image = pygame.image.load("Assets\dirt.png").convert_alpha()
grass_image = pygame.image.load("Assets\grass.png").convert_alpha()
plant_image = pygame.image.load("Assets\plant.png").convert_alpha()

bg_1 = pygame.image.load("Assets\Bg_1.png").convert_alpha()
bg_2 = pygame.image.load("Assets\Bg_2.png").convert_alpha()
bg_3 = pygame.image.load("Assets\Bg_3.png").convert_alpha()

bg_bubble = pygame.image.load("Assets\Bg_bubble.png").convert_alpha()

scientist_img_1 = pygame.image.load("Assets\Scientist_1.png").convert_alpha()
scientist_img_0 = pygame.image.load("Assets\Scientist_0.png").convert_alpha()
scientist_img_2 = pygame.image.load("Assets\Scientist_2.png").convert_alpha()

scientist_imgs = [scientist_img_0, scientist_img_1, scientist_img_2]

vision_meter_image = pygame.image.load("Assets\Vision_meter.png").convert_alpha()

radar_img_1 = pygame.image.load("Assets\Radar_1.png").convert_alpha()
radar_img_2 = pygame.image.load("Assets\Radar_2.png").convert_alpha()
radar_img_3 = pygame.image.load("Assets\Radar_3.png").convert_alpha()
radar_img_4 = pygame.image.load("Assets\Radar_4.png").convert_alpha()
radar_img_5 = pygame.image.load("Assets\Radar_5.png").convert_alpha()
radar_img_6 = pygame.image.load("Assets\Radar_6.png").convert_alpha()

radar_imgs = [radar_img_1,radar_img_2,radar_img_3,radar_img_4,radar_img_5,radar_img_6]

chat_img_1 = pygame.image.load("Assets\Chat_ui_bg_1.png").convert_alpha()
chat_img_2 = pygame.image.load("Assets\Chat_ui_bg_2.png").convert_alpha()
shop_bg_img_1 = pygame.image.load("Assets\Shop_ui_bg_1.png").convert_alpha()

phish_img_1 = pygame.image.load("Assets\Sphish_1.png").convert_alpha()
phish_img_2 = pygame.image.load("Assets\Sphish_2.png").convert_alpha()
phish_img_1_flipped = pygame.transform.flip(phish_img_1,1,0)
phish_img_2_flipped = pygame.transform.flip(phish_img_2,1,0)
phish_face_img_1 = pygame.image.load("Assets\Sphish_face_1.png").convert_alpha()

phish_imgs = [phish_img_1, phish_img_1_flipped, phish_img_2, phish_img_2_flipped]

satchel_img_1 = pygame.image.load("Assets\Satchel_1.png").convert_alpha()
satchel_img_2 = pygame.image.load("Assets\Satchel_2.png").convert_alpha()
satchel_img_2_flipped = pygame.transform.flip(satchel_img_2,1,0)

coin_icon_img = pygame.image.load("Assets\coin1_icon.png").convert_alpha()
coin_img_1 = pygame.image.load("Assets\coin_item1.png").convert_alpha()
coin_img_2 = pygame.image.load("Assets\coin_item2.png").convert_alpha()
coin_img_3 = pygame.image.load("Assets\coin_item3.png").convert_alpha()
coin_img_4 = pygame.image.load("Assets\coin_item4.png").convert_alpha()
coin_img_5 = pygame.image.load("Assets\coin_item5.png").convert_alpha()
coin_img_6 = pygame.image.load("Assets\coin_item6.png").convert_alpha()
coin_img_7 = pygame.image.load("Assets\coin_item7.png").convert_alpha()

coin_img_list = [coin_img_1, coin_img_2, coin_img_3, coin_img_4, coin_img_5, coin_img_6, coin_img_7]

shop_fish_img = pygame.image.load("Assets\Shop_Fush.png").convert_alpha()
shop_fish_face = pygame.image.load("Assets\Shop_Fush_Face.png").convert_alpha()
shop_fish_img_flip = pygame.transform.flip(shop_fish_img,1,0)
shop_backpack_img = pygame.image.load("Assets\Backpack_1.png").convert_alpha()
shop_backpack_img_flip = pygame.transform.flip(shop_backpack_img,1,0)
shop_fish_imgs = [shop_fish_img, shop_fish_img_flip, shop_backpack_img, shop_backpack_img_flip]

select_arrow = pygame.image.load("Assets\select_arrow.png").convert_alpha()

life_icon_img = pygame.image.load("Assets\life_icon.png").convert_alpha()
life_icon_shop_img = pygame.image.load("Assets\life_icon_big.png").convert_alpha()

double_jump_icon = pygame.image.load("Assets\Shop Animations\Double_Jump_Icon.png").convert_alpha()
dash_icon = pygame.image.load("Assets\Shop Animations\Dash_Icon.png").convert_alpha()
headstand_icon = pygame.image.load("Assets\Shop Animations\Headstand_Icon.png").convert_alpha()

font = pygame.font.Font("Assets\Grand9K Pixel.ttf", 16)
font_small = pygame.font.Font("Assets\Grand9K Pixel.ttf", 8)
font_medium = pygame.font.Font("Assets\Grand9K Pixel.ttf", 10)

chat_bubble_1 = pygame.image.load("Assets\Chat_boxes\chat_1.png").convert_alpha()
chat_bubble_2 = pygame.image.load("Assets\Chat_boxes\chat_2.png").convert_alpha()
chat_bubble_3 = pygame.image.load("Assets\Chat_boxes\chat_3.png").convert_alpha()

chat_bubble_1_flip = pygame.transform.flip(chat_bubble_1,1,0)
chat_bubble_2_flip = pygame.transform.flip(chat_bubble_2,1,0)
chat_bubble_3_flip = pygame.image.load("Assets\Chat_boxes\chat_3_flipped.png").convert_alpha()

headstand_1 = pygame.image.load("Assets\headstands_1.png").convert_alpha()
headstand_2 = pygame.image.load("Assets\headstands_2.png").convert_alpha()
headstand_3 = pygame.image.load("Assets\headstands_3.png").convert_alpha()
headstand_4 = pygame.image.load("Assets\headstands_4.png").convert_alpha()
headstands = [headstand_1, headstand_2, headstand_3, headstand_4]

sub1_img= pygame.image.load("Assets\sub1.png").convert_alpha()
sub2_img = pygame.transform.flip(sub1_img,1,0)

oxy_img = pygame.image.load("Assets\sub_oxy.png").convert_alpha()

sub_imgs = [sub1_img, sub2_img, oxy_img]

#Constants--------------------------------------------------------------------------------------------------

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (165,48,48)
BG_BLUE = (79,143,186)
SIGHT_YELLOW = (252,209,112)
DISCOVERY_PURPLE = (122,52,123)
UI_GRAY = (235,237,234)
TILE_SIZE = grass_image.get_height()
CHUNK_SIZE = 8
SCIENTIST_SIZE = [scientist_img_1.get_width(),scientist_img_1.get_height()]
PHISH_SIZE = [phish_img_1.get_width(),phish_img_1.get_height()]
SATCHEL_SIZE = [satchel_img_1.get_width(),satchel_img_1.get_height()]
COIN_SIZE = [coin_img_1.get_width(),coin_img_1.get_height()]
SHOP_FISH_SIZE = [shop_fish_img.get_width(),shop_fish_img.get_height()]
SUB_SIZE = [sub1_img.get_width(),sub1_img.get_height()]

#Variables------------------------------------------------------------------------------------------------

moving_left = False
moving_right = False
interacting = False
y_momentum = 0
game_map = {}
scroll = [0,0]
air_timer = 0
facing_right = True
animation_frame = 0 
fade_timing = 0
is_fading = False
fade_multiplyer = 2 #change this value to change speed of fade
year = "80M BC"
possible_years = [1700,1800,1900,1938,2000]
year_leap = 0
scientists_pos = []
scientists = []
time_caves_pos = []
time_caves = []
background_objects = [[0.10,bg_3,0,0],[0.10,bg_2,0,0],[0.10,bg_1,0,0]]
tile_index = {1:grass_image, 2:dirt_image, 3:plant_image, 4:scientist_img_1, 5:time_cave_image, 6:phish_img_1, 7:satchel_img_1, 8:coin_img_1, 9:shop_fish_img}
discovery_level = 1
radar_size = radar_img_1.get_size()
bubble_list = [[50,200]]
phishes_pos = []
phishes = []
is_chatting_global = []
satchels = []
satches_pos = []
has_satchel = []
coin_counter = 0
coins = []
coins_pos = []
shop_fishes = []
shop_fish_pos = []
lives = 3
can_double_jump = []
can_dash = []
coe_speed = 2
hud_on = True
has_turned_on_hud = False
can_headstand = []
headstanding = False
headstand_frame = 0


#Miscelaneous functions-----------------------------------------------------------------------------------

def palette_swap(surf, old_c, new_c, img):
    img_copy = pygame.Surface(img.get_size())
    img_copy.fill(new_c)
    surf.set_colorkey(old_c)
    img_copy.blit(surf, (0, 0))
    return img_copy

def grayscale(img):
    arr = pygame.surfarray.array3d(img)
    #luminosity filter
    avgs = [[(r*0.298 + g*0.587 + b*0.114) for (r,g,b) in col] for col in arr]
    arr = numpy.array([[[avg,avg,avg] for avg in col] for col in avgs])
    return pygame.surfarray.make_surface(arr)

def blit_text(surface, text, pos, font, color=pygame.Color('black')):   #taken from stackoverflow
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width = 250
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def generate_chunk(chunk_x,chunk_y):
    chunk_data = []
    chunk_seed = random.randint(0,5)

    for y_pos in range(CHUNK_SIZE):
        for x_pos in range(CHUNK_SIZE):

            real_x = chunk_x * CHUNK_SIZE + x_pos
            real_y = chunk_y * CHUNK_SIZE + y_pos
            tile_type = 0
            height = int(noise.pnoise1(real_x * 0.1, repeat = 99999999) * 5)


            if real_y > 8 - height:
                tile_type = 2
            elif real_y == 8 - height:  #ground is y8
                tile_type = 1
            elif real_y == 7 - height and random.randint(0,6) == 6:
                tile_type = 3
            elif real_y > 3 - height and real_y < 7 - height and random.randint(0,50) == 0:
                tile_type = 8
            
            if chunk_seed == 0: #standard empty chunk with plat 
                if real_y == 6 - height and random.randint(0,4) == 4:
                    tile_type = 4

            
            if chunk_seed == 1:   #scientist chunk
                if real_y == 6 - height and random.randint(0,4) == 4:
                    tile_type = 4

            if chunk_seed == 2:   #Time cave chunk 
                if real_y == 4 and x_pos == 2:
                    tile_type = 5 

            if chunk_seed == 3:  #Quest fish chunk 
                if real_y == 7 - height and x_pos == 4:
                    tile_type = 6

            if chunk_seed == 4:   #Satchel chunk
                if real_y == 6 - height and x_pos == 5:
                    tile_type = 7
            
            if chunk_seed == 5:  #shop chunk
                if real_y == 7 - height and x_pos == 5:
                    tile_type = 9

            if tile_type != 0:
                chunk_data.append([[real_x, real_y], tile_type])

    return chunk_data
   
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


#Classes--------------------------------------------------------------------------------------------------

class Coe_Class:
    def __init__(self):
        self.rect = pygame.Rect(1, 40,coe_image_1.get_width(),coe_image_1.get_height())

    def movement(self,rect,movement,tiles):
        collisions = {"Top":False, "Left":False, "Right":False, "Bottom":False}

        rect.x += movement[0]

        hit_list = collision_test(rect, tiles)

        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collisions["Right"] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collisions["Left"] = True

        rect.y += movement[1]
        hit_list = collision_test(rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collisions["Bottom"] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collisions["Top"] = True

        return collisions, rect

Coe = Coe_Class()

class Scientist_Class:
    def __init__(self, pos):
        self.pos = pos 
        self.radar_animation_frame = 0
        self.facing_number = random.randint(0,1)
        if self.facing_number ==0:
            self.facing_right = True
        else:
            self.facing_right = False


    def get_rect(self):
        return pygame.Rect(int(self.pos[0]), int(self.pos[1]), SCIENTIST_SIZE[0], SCIENTIST_SIZE[1])

    def render(self, surface, scroll):
        bobbing = math.sin(pygame.time.get_ticks()/300) * 3 
    
        
        if [self.pos[0], self.pos[1]] not in scientists_pos:
            scientists_pos.append([self.pos[0], self.pos[1]])
        
        if year_leap == 2:
            point_1 = (self.pos[0] - scroll[0] + SCIENTIST_SIZE[0]/2 - 4, self.pos[1] - scroll[1] - bobbing + SCIENTIST_SIZE[1]/2 - 5)
            if self.facing_right:
                point_2 = (self.pos[0] - scroll[0] + 50, self.pos[1] - scroll[1] - bobbing + 21)
                point_3 = (self.pos[0] - scroll[0] + 50 , self.pos[1] - scroll[1] - bobbing - 10)
                self.triangle_rect = pygame.Rect(self.pos[0] + SCIENTIST_SIZE[0]/2,  self.pos[1] - bobbing + SCIENTIST_SIZE[1]/2 - 10, 40,15)
            else:
                point_2 = (self.pos[0] - scroll[0] - 50, self.pos[1] - scroll[1] - bobbing + 21)
                point_3 = (self.pos[0] - scroll[0] - 50 , self.pos[1] - scroll[1] - bobbing - 10)
                self.triangle_rect = pygame.Rect(self.pos[0] + SCIENTIST_SIZE[0]/2 - 50,  self.pos[1] - bobbing + SCIENTIST_SIZE[1]/2 - 10, 40,15)

            pygame.draw.polygon(display,(SIGHT_YELLOW), (point_1, point_2, point_3))

        if year_leap == 3:
            self.radar_rect = pygame.Rect((int(self.pos[0] - scroll[0] - 22), int(self.pos[1] - scroll[1] - bobbing - 24)), radar_size)
            surface.blit(radar_imgs[int(self.radar_animation_frame/10)], (int(self.pos[0] - scroll[0] - 22), int(self.pos[1] - scroll[1] - bobbing - 24)))
            if self.radar_animation_frame == 50:
                self.radar_animation_frame = 0
            self.radar_animation_frame += 1
        
        if self.facing_right:
            surface.blit(scientist_imgs[year_leap - 1],(int(self.pos[0] - scroll[0]), int(self.pos[1] - scroll[1] - bobbing))) 
        else:
            surface.blit(pygame.transform.flip(scientist_imgs[year_leap - 1],1,0),(int(self.pos[0] - scroll[0]), int(self.pos[1] - scroll[1] - bobbing)))


    def collision_test_with_player(self,rect):
        return self.get_rect().colliderect(rect)
    def collision_test_with_player_sight(self,rect):
        try:
            return self.triangle_rect.colliderect(rect)
        except:
            pass
    def collision_test_with_player_radar(self,rect):
        try:
            return self.radar_rect.colliderect(rect)
        except:
            pass

class Time_Cave_Class:
    def __init__(self,pos):
        self.pos = pos
        self.WIDTH = time_cave_image.get_width()
        self.HEIGHT = time_cave_image.get_height()
        self.rect = pygame.Rect(self.pos[0],self.pos[1], self.WIDTH,self.HEIGHT)
        self.full = True

    def render(self, surface, scroll):
        bobbing = math.sin(pygame.time.get_ticks()/300) * 5
        if self.full:
            surface.blit(time_cave_image,(int(self.pos[0] - scroll[0]), int(self.pos[1] - scroll[1])))
            surface.blit(cave_clock_image,(int(self.pos[0] - scroll[0] + self.WIDTH/2 - 12), int(self.pos[1] - scroll[1]+ bobbing)))
        else:
            surface.blit(time_cave_empty_image,(int(self.pos[0] - scroll[0]), int(self.pos[1] - scroll[1])))

        if [self.pos[0], self.pos[1]] not in time_caves_pos:
            time_caves_pos.append([self.pos[0], self.pos[1]])        

    def collision_test_with_player(self,rect):
        return self.rect.colliderect(rect)

class NPC_Class:
    def __init__(self, pos):
        self.pos = pos 
        self.facing_number = random.randint(0,1)
        if self.facing_number == 0:
            self.facing_right = True
        else:
            self.facing_right = False

        self.rect = pygame.Rect(int(self.pos[0]), int(self.pos[1]), self.SIZE[0], self.SIZE[1])

        if [self.pos[0], self.pos[1]] not in self.list:
            self.list.append([self.pos[0], self.pos[1]])

    def render(self, surface, scroll):
        bobbing = math.sin(pygame.time.get_ticks()/300) * 3 

        if self.facing_right:
            surface.blit(self.images[0],(int(self.pos[0] - scroll[0]), int(self.pos[1] - scroll[1] - bobbing - 10))) 
        else:
            surface.blit(self.images[1],(int(self.pos[0] - scroll[0]), int(self.pos[1] - scroll[1] - bobbing - 10)))

    def collision_test_with_player(self,rect):
        return self.rect.colliderect(rect)  

class Boss_class():
    def __init__(self):
        self.pos = [10,10]
        self.health = 3
        self.SIZE = SUB_SIZE
        self.images = sub_imgs

        self.rect = pygame.Rect(int(self.pos[0]), int(self.pos[1]), self.SIZE[0], self.SIZE[1])

        self.oxy_rect = pygame.Rect(70,10, self.health, 20)
        
        self.facing_right = True

    def render(self):
        bobbing = math.sin(pygame.time.get_ticks()/300) * 3 

        if self.facing_right:
            display.blit(self.images[0],(int(self.pos[0]), int(self.pos[1]- bobbing))) 
        else:
            display.blit(self.images[1],(int(self.pos[0]), int(self.pos[1]- bobbing)))

        display.blit(self.images[2], (70,10))
        pygame.draw.rect(display, (WHITE), self.oxy_rect)
    
    def collision_test_with_player(self,rect):
        return self.rect.colliderect(rect)  





class Phish_Class(NPC_Class):
    def __init__(self, pos):
        self.SIZE = PHISH_SIZE
        self.images = phish_imgs
        self.list = phishes_pos

        self.is_chatting = False
        self.current_dialogue = 0
        self.quest_complete = False

        self.dialogue_text = ["Hey! \nI've lost my satchel, can you help me find it?"]

        super().__init__(pos)

    def render(self, surface, scroll):
        bobbing = math.sin(pygame.time.get_ticks()/300) * 3 

        if self.quest_complete == False:
            if self.facing_right:
                surface.blit(chat_bubble_1, (self.pos[0] - scroll[0] + 20, self.pos[1] - scroll[1] - bobbing - 25))
            else:
                surface.blit(chat_bubble_1_flip, (self.pos[0] - scroll[0] - 10, self.pos[1] - scroll[1] - bobbing - 25))

        if has_satchel:
            if self.facing_right:
                surface.blit(chat_bubble_2, (self.pos[0] - scroll[0] + 20, self.pos[1] - scroll[1] - bobbing - 25))
            else:
                surface.blit(chat_bubble_2_flip, (self.pos[0] - scroll[0] - 10, self.pos[1] - scroll[1] - bobbing - 25))

        if self.quest_complete == False:
            if self.facing_right:
                surface.blit(self.images[0],(int(self.pos[0] - scroll[0]), int(self.pos[1] - scroll[1] - bobbing - 10))) 
            else:
                surface.blit(self.images[1],(int(self.pos[0] - scroll[0]), int(self.pos[1] - scroll[1] - bobbing - 10)))
        else:
            if self.facing_right:
                surface.blit(self.images[2],(int(self.pos[0] - scroll[0]), int(self.pos[1] - scroll[1] - bobbing - 10))) 
                surface.blit(satchel_img_2, (int(self.pos[0] - scroll[0]) + PHISH_SIZE[0] + 5, int(self.pos[1] - scroll[1] - bobbing)))
            else:
                surface.blit(self.images[3],(int(self.pos[0] - scroll[0]), int(self.pos[1] - scroll[1] - bobbing - 10)))
                surface.blit(satchel_img_2_flipped, (int(self.pos[0] - scroll[0]) - 20, int(self.pos[1] - scroll[1] - bobbing)))  

    def functionality(self):
        if 1073742049 in keys: #left shift
            try:
                self.is_chatting = False
                is_chatting_global.pop(0)
                self.current_dialogue = 0
            except:
                pass

        if self.is_chatting:
            display.blit(chat_img_1, (30, 150))
            display.blit(phish_face_img_1, (50, 163))
            blit_text(display, self.dialogue_text[self.current_dialogue], (85,158), font_small, BLACK)


    def interact(self):
        if len(has_satchel) == 1 and self.quest_complete == False:
            self.dialogue_text = ["Hey! \nI've lost my satchel, can you help me find it?", "Oh wow thank you!", "Here are some coins as a little reward!"]
            
        if self.is_chatting and len(self.dialogue_text) - 1 == self.current_dialogue:  #if you are done chatting 
            self.is_chatting = False
            is_chatting_global.pop(0)
            self.current_dialogue = 0
            if len(has_satchel) == 1 and self.quest_complete == False:
                has_satchel.clear()
                self.quest_complete = True
                global coin_counter
                coin_counter += 10
                self.dialogue_text = ["Thank you very much!"]

        elif self.is_chatting and len(self.dialogue_text) - 1 != self.current_dialogue:  #if theres still text left
            self.current_dialogue += 1

        elif self.is_chatting == False:  #if you want to start the convo
            self.is_chatting = True
            is_chatting_global.append(1)
            
class Colectable_Class:
    def __init__(self, pos):
        self.pos = pos
        self.rect = pygame.Rect(int(self.pos[0]), int(self.pos[1]), self.SIZE[0], self.SIZE[1])

        if [self.pos[0], self.pos[1]] not in self.list:
            self.list.append([self.pos[0], self.pos[1]])
    
    def render(self, surface,scroll):
        bobbing = math.sin(pygame.time.get_ticks()/300) * 3 

        surface.blit(self.images,(int(self.pos[0] - scroll[0]), int(self.pos[1] - scroll[1] - bobbing - 10))) 
    
    def collision_test_with_player(self,rect):
        return self.rect.colliderect(rect)

class Satchel_Class(Colectable_Class):
    def __init__(self,pos):
        self.images = satchel_img_1
        self.SIZE = SATCHEL_SIZE
        self.list = satches_pos
        super().__init__(pos)

class Coin_Class(Colectable_Class):
    def __init__(self, pos):
        self.images = coin_img_list
        self.SIZE = COIN_SIZE
        self.list = coins_pos
        self.animation_frame = 0
        self.animation_rotation = 1
        super().__init__(pos)

    def render(self, surface,scroll):
        bobbing = math.sin(pygame.time.get_ticks()/300) * 3 

        if [self.pos[0], self.pos[1]] not in self.list:
            self.list.append([self.pos[0], self.pos[1]])

        surface.blit(self.images[int(self.animation_frame/10)],(int(self.pos[0] - scroll[0]), int(self.pos[1] - scroll[1] - bobbing - 10))) 
        self.animation_frame += self.animation_rotation

        if self.animation_frame == 60:
            self.animation_rotation *= -1
        if self.animation_frame == 0:
            self.animation_rotation *= -1

class Shop_Fish_Class(NPC_Class):
    def __init__(self,pos):
        self.SIZE = SHOP_FISH_SIZE
        self.images = shop_fish_imgs
        self.list = shop_fish_pos

        self.dialogue_text = ["Hi, looking for anything?", "DEBUG"]
        self.is_chatting = False
        self.current_dialogue = 0

        self.items = [["Double Jump", "For the right price, I'll teach you how \nto double swim!", double_jump_icon , 10, 1,(0,0,0)], #size of image = 16x16 or close
         ["Dash", "Dashing is a great way to move out of danger (LSHIFT)" , dash_icon , 20, 1,(0,0,0)],
         ["Headstand", "The classic coelacanth headstand!\n I don't know what it does (R)" , headstand_icon , 30, 1,(0,0,0)],
         ["item_4", "Ah, ITEM4, wonderful choice!" , life_icon_shop_img , 400, 1,(0,0,0)],
         ["Extra life", "One extra life!\n Don't ask me where I got it" , life_icon_shop_img , 5, 1,(32,32,32)],
         ["item_6", "Ah, ITEM6, wonderful choice!" , life_icon_shop_img , 600, 1,(0,0,0)]]

        self.selected_item = 0

        self.arrow_pos = [(30, 45), (110,45), (190,45), (30,105), (110,105), (190,105)]
        self.coin_ico_pos = [(68, 70), (148,70), (228,70), (68,130), (148,130), (228,130)]
        self.cost_pos = [(50,67), (130,67), (210,67), (50,127), (130,127), (210,127)]
        self.icons_pos = [(55,50), (135,50), (215,50), (55,110), (135,110), (215,110)]

        super().__init__(pos)

    def render(self, surface, scroll):
        bobbing = math.sin(pygame.time.get_ticks()/300) * 3 

        if self.facing_right:
            surface.blit(chat_bubble_3, (self.pos[0] - scroll[0] + 10, self.pos[1] - scroll[1] - bobbing - 25))
        else:
            surface.blit(chat_bubble_3_flip, (self.pos[0] - scroll[0] - 10, self.pos[1] - scroll[1] - bobbing - 25))

        if self.facing_right:
            surface.blit(self.images[3],(int(self.pos[0] - scroll[0] - 3), int(self.pos[1] - scroll[1]))) 
            surface.blit(self.images[0],(int(self.pos[0] - scroll[0]), int(self.pos[1] - scroll[1] - bobbing - 5))) 
        else:
            surface.blit(self.images[2],(int(self.pos[0] - scroll[0] + 3), int(self.pos[1] - scroll[1]))) 
            surface.blit(self.images[1],(int(self.pos[0] - scroll[0]), int(self.pos[1] - scroll[1] - bobbing - 5)))

        if len(can_double_jump) == 1:
            self.items[0][4] = 0
        if len(can_dash) == 1:
            self.items[1][4] = 0
        if len(can_headstand) == 1:
            self.items[2][4] = 0

    def functionality(self):
        global coin_counter
        #Closing the chat
        if 1073742049 in keys: #left shift
            try:
                self.is_chatting = False
                is_chatting_global.pop(0)
                self.current_dialogue = 0
            except:
                pass

        if self.is_chatting:
            #shop ui
            display.blit(shop_bg_img_1, (30, 30))
            display.blit(shop_bg_img_1, (30, 90))

            display.blit(shop_bg_img_1, (110, 30))
            display.blit(shop_bg_img_1, (110, 90))

            display.blit(shop_bg_img_1, (190, 30))
            display.blit(shop_bg_img_1, (190, 90))

            display.blit(chat_img_1, (30, 150))
            display.blit(shop_fish_face, (50, 163))

            #non-shop lines of dialogue
            if self.current_dialogue == 0:
                blit_text(display, self.dialogue_text[self.current_dialogue], (85,160), font_small, BLACK)

            else:

                #controls   
                if 97 in keys:
                    self.selected_item -= 1
                    if self.selected_item == -1:
                        self.selected_item = 5
                if 100 in keys:
                    self.selected_item += 1
                    if self.selected_item == 6:
                        self.selected_item = 0
                if 115 in keys:
                        if self.selected_item == 0:
                            self.selected_item = 3
                        elif self.selected_item == 1:
                            self.selected_item = 4
                        elif self.selected_item == 2:
                            self.selected_item = 5
                        elif self.selected_item == 3:
                            self.selected_item = 0
                        elif self.selected_item == 4:
                            self.selected_item = 1
                        elif self.selected_item == 5:
                            self.selected_item = 2
                if 119 in keys:
                        if self.selected_item == 0:
                            self.selected_item = 3
                        elif self.selected_item == 1:
                            self.selected_item = 4
                        elif self.selected_item == 2:
                            self.selected_item = 5
                        elif self.selected_item == 3:
                            self.selected_item = 0
                        elif self.selected_item == 4:
                            self.selected_item = 1
                        elif self.selected_item == 5:
                            self.selected_item = 2
                #dialogue
                blit_text(display, self.items[self.selected_item][1], (85,160), font_small, BLACK)

                #rendering assets
                for i in range(6):
                    display.blit(coin_icon_img, self.coin_ico_pos[i])

                    if coin_counter < self.items[i][3]:
                        blit_text(display, str(self.items[i][3]), self.cost_pos[i], font_small, RED)
                    else:
                        blit_text(display, str(self.items[i][3]), self.cost_pos[i], font_small, BLACK)

                    if self.items[i][4] == 1:
                        display.blit(self.items[i][2], self.icons_pos[i])
                    if self.items[i][4] == 0:
                        self.items[i][2] = grayscale(self.items[i][2]).convert_alpha()
                        self.items[i][2].set_colorkey(self.items[i][5])

                        
                        display.blit(self.items[i][2] , self.icons_pos[i])

                    if self.selected_item == i:
                        display.blit(select_arrow, self.arrow_pos[i])

                #try to buy
                if 32 in keys:
                    if self.selected_item == 0:
                        if coin_counter >= self.items[0][3] and self.items[0][4] == 1:
                            coin_counter -= self.items[0][3]
                            self.items[0][4] = 0
                            can_double_jump.append(0)
                        pass
                    if self.selected_item == 1:
                        if coin_counter >= self.items[1][3] and self.items[1][4] == 1:
                            coin_counter -= self.items[1][3]
                            self.items[1][4] = 0
                            can_dash.append(0)
                        pass
                    if self.selected_item == 2:
                        if coin_counter >= self.items[2][3] and self.items[2][4] == 1:
                            coin_counter -= self.items[2][3]
                            self.items[2][4] = 0
                            can_headstand.append(0)
                        pass
                    if self.selected_item == 3:
                        if coin_counter >= self.items[3][3] and self.items[3][4] == 1:
                            coin_counter -= self.items[3][3]
                            self.items[3][4] = 0
                        pass
                    if self.selected_item == 4:
                        if coin_counter >= self.items[4][3] and self.items[4][4] == 1:
                            coin_counter -= self.items[4][3]
                            self.items[4][4] = 0
                            global lives 
                            lives += 1
                    if self.selected_item == 5:
                        if coin_counter >= self.items[5][3] and self.items[5][4] == 1:
                            coin_counter -= self.items[5][3]
                            self.items[5][4] = 0
                        pass




    def interact(self):
        if self.current_dialogue == 0 or self.is_chatting == False:
            if self.is_chatting and len(self.dialogue_text) - 1 == self.current_dialogue:  #if you are done chatting 
                self.is_chatting = False
                is_chatting_global.pop(0)
                self.current_dialogue = 0

            elif self.is_chatting and len(self.dialogue_text) - 1 != self.current_dialogue:  #if theres still text left
                self.current_dialogue += 1

            elif self.is_chatting == False:  #if you want to start the convo
                self.is_chatting = True
                is_chatting_global.append(1)
 



#Bosses---------------------------------------------------------------------------------------------------

def submarine_boss_gamestate():
    global facing_right, year_leap, moving_right, moving_left, y_momentum, air_timer, headstanding, keys, year, coin_counter, lives, hud_on, has_turned_on_hud, is_fading, discovery_level, coe_speed, interacting, fade_timing, fade_multiplyer, animation_frame
    Recorded_pos = [Coe.rect.x, Coe.rect.y]
    Coe.rect.x = 0
    Coe.rect.y = 50
    while True:
        display.fill(BG_BLUE)

        #backgrond objects ----------------------------------------------------------

        for obj in background_objects:
            obj_x = obj[2] - scroll[0] * obj[0]

            for i in range(-50, 50):
                display.blit(obj[1],(obj_x + (i * 300), obj[3]))

        if random.randint(0,30) == 0:
            bubble_list.append([random.randint(0,DISPLAY_SIZE[0] - 4),200])

        for bubble in bubble_list:
            if bubble[1] <= -10:
                bubble_list.pop(bubble_list.index(bubble))
            bubble[1] -= 0.5
            display.blit(bg_bubble, (bubble[0], bubble[1]))

        #world generation-----------------------------------------------------------

        game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]
        
        tile_rects = []

        y = 0
        for row in game_map:
            x = 0  
            for tile in row: 
                if tile == "1":
                    display.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE)) 
                if tile == "2":
                    display.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))

                if tile != "0":
                    tile_rects.append(pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)) 

                x += 1 

            y += 1

        #boss------------------------------------------------------------------

        Sub = Boss_class()

        Sub.render()

        #movement---------------------------------------------------------------

        coe_movement = [0,0]

        if moving_right:
            coe_movement[0] += coe_speed
            facing_right = True
        if moving_left:
            coe_movement[0] -= coe_speed
            facing_right = False

        coe_movement[1] += y_momentum
        y_momentum += 0.2
        if y_momentum > 3:
            y_momentum = 3
        
        Collisions, Coe.rect = Coe.movement(Coe.rect, coe_movement, tile_rects)


        if Collisions["Bottom"]:
            y_momentum = 0
            air_timer = 0
        else:
            air_timer += 1


        if Collisions["Top"]:
            y_momentum = 0

        #Keypresses------------------------------------------------------------

        keys = [] 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.KEYDOWN:
                keys.append(event.key)
                keys_pressed = pygame.key.get_pressed()
                #print(keys)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                #movement
                if len(is_chatting_global) == False:
                    if event.key == pygame.K_w:
                        if len(can_double_jump) == 1:
                            if air_timer < 33:
                                y_momentum = -5
                        else:
                            if air_timer < 11:
                                y_momentum = -5
                    if event.key == pygame.K_a:
                        moving_left = True
                    if event.key == pygame.K_d:
                        moving_right = True    
                if event.key == pygame.K_SPACE:
                    interacting = True

                if keys_pressed[pygame.K_LSHIFT] and len(can_dash) == 1:
                    coe_speed = 4
                
                if event.key == pygame.K_i:
                    has_turned_on_hud = True
                    if hud_on:
                        hud_on = False
                    else:
                        hud_on = True         

                if event.key == pygame.K_r and len(can_headstand) == 1:
                    if headstanding:
                        headstanding = False
                    else:
                        headstanding = True
                #DEBUG----------------
                if event.key == pygame.K_g:
                    Coe.rect.x = Recorded_pos[0]
                    Coe.rect.y = Recorded_pos[1]
                    mainloop()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    moving_right = False
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_SPACE:
                    interacting = False
                if event.key == pygame.K_LSHIFT:
                    coe_speed = 2


        #animation----------------------------------------------------------------

        bobbing = math.sin(pygame.time.get_ticks()/300) * 2

        if headstanding == False:
            if facing_right and moving_right == False:
                display.blit(coe_image_1, (Coe.rect.x, Coe.rect.y + bobbing))
                animation_frame = 0
            elif facing_right == False and moving_left == False:
                display.blit(pygame.transform.flip(coe_image_1, 1, 0), (Coe.rect.x, Coe.rect.y + bobbing))
                animation_frame = 0
            elif facing_right and moving_right:
                if round(animation_frame/10) == 4:
                    animation_frame = 0
                display.blit(coe_img_list[round(animation_frame/10)], (Coe.rect.x, Coe.rect.y + bobbing))
                animation_frame += 1
            elif facing_right == False and moving_left:
                if round(animation_frame/10) == 4:
                    animation_frame = 0
                display.blit(pygame.transform.flip(coe_img_list[round(animation_frame/10)], 1, 0), (Coe.rect.x, Coe.rect.y + bobbing))
                animation_frame += 1

        else:
            if round(headstand_frame/10) == 4:
                headstand_frame = 0
            display.blit(headstands[round(headstand_frame/10)],(Coe.rect.x, Coe.rect.y+ bobbing - 20))
            headstand_frame += 1

        #UI and fading----------------------------------------------------------

        upgrades_label = font_small.render("Upgrades:", True, UI_GRAY)
        lives_label = font_small.render("x " + str(lives), True, UI_GRAY)
        if hud_on:
            display.blit(life_icon_img,(10, 168))
            display.blit(lives_label,(20,165))
            display.blit(upgrades_label,(250,5))

            if len(can_double_jump) == 1:
                display.blit(double_jump_icon,(280,20))
            if len(can_dash) == 1:
                display.blit(dash_icon,(280,40))
            if len(can_headstand) == 1:
                display.blit(headstand_icon,(280,60))

        discovery_bar = pygame.Rect(12, 180, discovery_level, 13)
        if len(is_chatting_global) == 0:
            pygame.draw.rect(display, DISCOVERY_PURPLE, discovery_bar)
            display.blit(vision_meter_image, (10, 180))

        if discovery_level >= 75:
            lives -= 1
            discovery_level = 1

        if lives == 0:
            print("lose")
                
        if is_fading:
            fade = pygame.Surface(WINDOW_SIZE)
            fade.fill((0,0,0))

            if fade_timing >= 300:  
                fade_multiplyer *= -1
            fade_timing += fade_multiplyer
            
            if fade_timing < 0:
                fade_timing = 0
                fade_multiplyer *= -1
                is_fading = False

            fade.set_alpha(fade_timing)
            display.blit(fade,(0,0))


        #display and FPS---------------------------------------------------------

        win.blit(pygame.transform.scale(display, WINDOW_SIZE), (0,0))
        pygame.display.update()

        clock.tick(60)



#Mainloop-------------------------------------------------------------------------------------------------

def mainloop():
    global facing_right, year_leap, moving_right, moving_left, y_momentum, air_timer, headstanding, keys, year, coin_counter, lives, hud_on, has_turned_on_hud, is_fading, discovery_level, coe_speed, interacting, fade_timing, fade_multiplyer, animation_frame
    while True:
        #print(clock.get_fps())
        display.fill(BG_BLUE)

        #camera scroll----------------------------------------------------------------

        scroll[0] += (Coe.rect.x - scroll[0] - DISPLAY_SIZE[0]/2 + Coe.rect.width/2)/20
        scroll[1] += (Coe.rect.y - scroll[1] - DISPLAY_SIZE[1]/2 - Coe.rect.height/2)/20

        int_scroll = scroll.copy()
        int_scroll[0] = int(int_scroll[0])
        int_scroll[1] = int(int_scroll[1])

        #backgrond objects ----------------------------------------------------------

        for obj in background_objects:
            obj_x = obj[2] - scroll[0] * obj[0]

            for i in range(-50, 50):
                display.blit(obj[1],(obj_x + (i * 300), obj[3]))

        if random.randint(0,30) == 0:
            bubble_list.append([random.randint(0,DISPLAY_SIZE[0] - 4),200])

        for bubble in bubble_list:
            if bubble[1] <= -10:
                bubble_list.pop(bubble_list.index(bubble))
            bubble[1] -= 0.5
            display.blit(bg_bubble, (bubble[0], bubble[1]))

        #world generation-----------------------------------------------------------

        tile_rects = []

        for y in range(4):
            for x in range(4):
                target_x = x - 1 + int(round(scroll[0]/(CHUNK_SIZE*TILE_SIZE)))
                target_y = y - 1 + int(round(scroll[1]/(CHUNK_SIZE*TILE_SIZE)))

                target_chunk = str(target_x) + ";" + str(target_y)
                if target_chunk not in game_map:
                    game_map[target_chunk] = generate_chunk(target_x, target_y)

                for tile in game_map[target_chunk]:
                    if tile[1] in [1,2,3]:
                        display.blit(tile_index[tile[1]], (tile[0][0]*TILE_SIZE - scroll[0], tile[0][1]*TILE_SIZE - scroll[1]))

                    if tile[1] in [1,2]:#if tile_type is 1 or 2 make a rect for colision 
                        tile_rects.append(pygame.Rect(tile[0][0]*TILE_SIZE, tile[0][1]*TILE_SIZE, 16, 16))                    

                    if tile[1] in [4]:
                        if year_leap > 0:
                            if [tile[0][0]*TILE_SIZE, tile[0][1]* TILE_SIZE] not in scientists_pos:
                                scientists.append(Scientist_Class([tile[0][0]*TILE_SIZE, tile[0][1]* TILE_SIZE]))

                    if tile[1] in [5]:
                        if [tile[0][0]*TILE_SIZE, tile[0][1]* TILE_SIZE] not in time_caves_pos:
                            time_caves.append(Time_Cave_Class([tile[0][0]*TILE_SIZE, tile[0][1]* TILE_SIZE]))

                    if tile[1] in [6]:
                        if [tile[0][0]*TILE_SIZE, tile[0][1]* TILE_SIZE] not in phishes_pos:
                            phishes.append(Phish_Class([tile[0][0]*TILE_SIZE, tile[0][1]* TILE_SIZE]))
                        
                    if tile[1] in [7]:
                        if [tile[0][0]*TILE_SIZE, tile[0][1]* TILE_SIZE] not in satches_pos:
                            satchels.append(Satchel_Class([tile[0][0]*TILE_SIZE, tile[0][1]* TILE_SIZE]))

                    if tile[1] in [8]:
                        if [tile[0][0]*TILE_SIZE, tile[0][1]* TILE_SIZE] not in coins_pos:
                            coins.append(Coin_Class([tile[0][0]*TILE_SIZE, tile[0][1]* TILE_SIZE]))

                    if tile[1] in [9]:
                        if [tile[0][0]*TILE_SIZE, tile[0][1]* TILE_SIZE] not in shop_fish_pos:
                            shop_fishes.append(Shop_Fish_Class([tile[0][0]*TILE_SIZE, tile[0][1]* TILE_SIZE]))



        #movement---------------------------------------------------------------

        coe_movement = [0,0]

        if moving_right:
            coe_movement[0] += coe_speed
            facing_right = True
        if moving_left:
            coe_movement[0] -= coe_speed
            facing_right = False

        coe_movement[1] += y_momentum
        y_momentum += 0.2
        if y_momentum > 3:
            y_momentum = 3
        
        Collisions, Coe.rect = Coe.movement(Coe.rect, coe_movement, tile_rects)


        if Collisions["Bottom"]:
            y_momentum = 0
            air_timer = 0
        else:
            air_timer += 1


        if Collisions["Top"]:
            y_momentum = 0

        #Keypresses------------------------------------------------------------

        keys = [] 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.KEYDOWN:
                keys.append(event.key)
                keys_pressed = pygame.key.get_pressed()
                #print(keys)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                #movement
                if len(is_chatting_global) == False:
                    if event.key == pygame.K_w:
                        if len(can_double_jump) == 1:
                            if air_timer < 33:
                                y_momentum = -5
                        else:
                            if air_timer < 11:
                                y_momentum = -5
                    if event.key == pygame.K_a:
                        moving_left = True
                    if event.key == pygame.K_d:
                        moving_right = True    
                if event.key == pygame.K_SPACE:
                    interacting = True

                #DEBUG-----------g
                if event.key == pygame.K_g:
                    submarine_boss_gamestate()

                if keys_pressed[pygame.K_LSHIFT] and len(can_dash) == 1:
                    coe_speed = 4
                
                if event.key == pygame.K_i:
                    has_turned_on_hud = True
                    if hud_on:
                        hud_on = False
                    else:
                        hud_on = True         

                if event.key == pygame.K_r and len(can_headstand) == 1:
                    if headstanding:
                        headstanding = False
                    else:
                        headstanding = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    moving_right = False
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_SPACE:
                    interacting = False
                if event.key == pygame.K_LSHIFT:
                    coe_speed = 2


        #Objects behind the player-----------------------------------------------

        for cave in time_caves:
            cave.render(display, scroll)
            if cave.collision_test_with_player(Coe.rect):
                if interacting:
                    cave.full = False
                    is_fading = True

        for satchel in satchels:
            satchel.render(display, scroll)
            if satchel.collision_test_with_player(Coe.rect):
                if len(has_satchel) == 0:
                    has_satchel.append(1)
                    satchels.pop(satchels.index(satchel))

        for coin in coins:
            coin.render(display, scroll)
            if coin.collision_test_with_player(Coe.rect):
                coin_counter += 5
                coins.pop(coins.index(coin))

        for phish in phishes:
            phish.render(display, scroll)
            phish.functionality()
            if phish.collision_test_with_player(Coe.rect):
                if interacting and 32 in keys:
                    phish.interact()



        #animation----------------------------------------------------------------

        bobbing = math.sin(pygame.time.get_ticks()/300) * 2

        if headstanding == False:
            if facing_right and moving_right == False:
                display.blit(coe_image_1, (Coe.rect.x - int_scroll[0], Coe.rect.y - int_scroll[1] + bobbing))
                animation_frame = 0
            elif facing_right == False and moving_left == False:
                display.blit(pygame.transform.flip(coe_image_1, 1, 0), (Coe.rect.x - int_scroll[0], Coe.rect.y - int_scroll[1] + bobbing))
                animation_frame = 0
            elif facing_right and moving_right:
                if round(animation_frame/10) == 4:
                    animation_frame = 0
                display.blit(coe_img_list[round(animation_frame/10)], (Coe.rect.x - int_scroll[0], Coe.rect.y - int_scroll[1] + bobbing))
                animation_frame += 1
            elif facing_right == False and moving_left:
                if round(animation_frame/10) == 4:
                    animation_frame = 0
                display.blit(pygame.transform.flip(coe_img_list[round(animation_frame/10)], 1, 0), (Coe.rect.x - int_scroll[0], Coe.rect.y - int_scroll[1] + bobbing))
                animation_frame += 1

        else:
            if round(headstand_frame/10) == 4:
                headstand_frame = 0
            display.blit(headstands[round(headstand_frame/10)],(Coe.rect.x - int_scroll[0], Coe.rect.y - int_scroll[1] + bobbing - 20))
            headstand_frame += 1


        #Objects in front of the player-------------------------------------------

        for scientist in scientists:
                    scientist.render(display, scroll)
                    if scientist.collision_test_with_player(Coe.rect) or scientist.collision_test_with_player_sight(Coe.rect) or scientist.collision_test_with_player_radar(Coe.rect):
                        discovery_level += 0.5

        for shop in shop_fishes:
            shop.render(display, scroll)
            shop.functionality()
            if shop.collision_test_with_player(Coe.rect):
                if interacting and 32 in keys:
                    shop.interact()
            

        #UI and fading----------------------------------------------------------

        years_label = font.render("Year: " + str(year), True, UI_GRAY)
        coins_label = font_small.render(str(coin_counter), True, UI_GRAY)
        upgrades_label = font_small.render("Upgrades:", True, UI_GRAY)
        lives_label = font_small.render("x " + str(lives), True, UI_GRAY)
        inventory_tutorial = font_small.render("Press I to turn off HUD", True, UI_GRAY)
        if hud_on:
            display.blit(coins_label,(20,21))
            display.blit(coin_icon_img,(10,23))
            display.blit(life_icon_img,(10, 168))
            display.blit(lives_label,(20,165))
            display.blit(upgrades_label,(250,5))
            if has_turned_on_hud == False:
                display.blit(inventory_tutorial,(185,185))
            if len(has_satchel):
                display.blit(satchel_img_1,(10, 35))
            if is_fading == False:
                display.blit(years_label,(10,0))

            if len(can_double_jump) == 1:
                display.blit(double_jump_icon,(280,20))
            if len(can_dash) == 1:
                display.blit(dash_icon,(280,40))
            if len(can_headstand) == 1:
                display.blit(headstand_icon,(280,60))
            


        discovery_bar = pygame.Rect(12, 180, discovery_level, 13)
        if len(is_chatting_global) == 0:
            pygame.draw.rect(display, DISCOVERY_PURPLE, discovery_bar)
            display.blit(vision_meter_image, (10, 180))

        if discovery_level >= 75:
            lives -= 1
            discovery_level = 1

        if lives == 0:
            print("lose")
                
        if is_fading:
            fade = pygame.Surface(WINDOW_SIZE)
            fade.fill((0,0,0))
            year = possible_years[year_leap]

            if fade_timing >= 300:  
                fade_multiplyer *= -1
            fade_timing += fade_multiplyer
            
            if fade_timing < 0:
                fade_timing = 0
                fade_multiplyer *= -1
                is_fading = False
                year_leap += 1
                discovery_level = 1

            fade.set_alpha(fade_timing)
            years_label.set_alpha(fade_timing)
            display.blit(fade,(0,0))
            year = possible_years[year_leap]
            display.blit(years_label,(105,90))


        #display and FPS---------------------------------------------------------

        win.blit(pygame.transform.scale(display, WINDOW_SIZE), (0,0))
        pygame.display.update()

        clock.tick(60)

if __name__ == "__main__":
    mainloop()

