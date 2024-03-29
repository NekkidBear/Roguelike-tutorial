import tcod as libtcod

from entity import Entity
from input_handlers import handle_keys


def main():
    screen_width = 80
    screen_height = 50

    player = Entity(int(screen_width/2), int(screen_height/2), '@', libtcod.white)
    npc = Entity(int(screen_width/2 -5), int(screen_height /2), '@', libtcod.white)
    entities = [npc,player]

    libtcod.console_set_custom_font('arial10X10.png', libtcod.FONT_TYPE_GREYSCALE|libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width,screen_height, 'libtcod tutorial revised', False,libtcod.RENDERER_SDL2,vsync=True)

    con = libtcod.console_new(screen_width,screen_height)


    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed:
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        libtcod.console_set_default_foreground(con,libtcod.white)
        libtcod.console_put_char(con,player_x,player_y,'@',libtcod.BKGND_NONE)
        libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        libtcod.console_flush()

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player.move(dx,dy)


        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())



if __name__ == '__main__':
    main()
