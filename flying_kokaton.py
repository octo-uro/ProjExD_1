import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_revarse = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr % 1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_revarse, [1600-x, 0])
        screen.blit(kk_img, kk_rct)
        key_lst = pg.key.get_pressed()
        key = lambda k: int(key_lst[k])
        afk = int(not any(key(k) for k in [pg.K_LEFT, pg.K_RIGHT]))
        kk_rct.move_ip(key(pg.K_RIGHT) - key(pg.K_LEFT) - afk, key(pg.K_DOWN) - key(pg.K_UP))
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()