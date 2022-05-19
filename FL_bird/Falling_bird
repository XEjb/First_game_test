G = 9.8*30 # g
JUMP_V = -300
bird_x,bird_y = 700,450
bird_v = 0

if not jump:
    bird_v += G*frame
else:
bird_v = JUMP_V
jump = False
bird_y += frame*bird_v

def draw_bird():
screen.blit(birdImg,[bird_x,bird_y])
