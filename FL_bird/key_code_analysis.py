tunnel_list = [x-speed if x-speed>-200 else 2100 for x in tunnel_list ]

def draw_tunnel():
for x in tunnel_list:
    pygame.draw.rect(screen,COLORS['darkgreen'],(x,0,100,350),0)
    pygame.draw.rect(screen,COLORS['darkgreen'],(x+100,550,100,350),0)
