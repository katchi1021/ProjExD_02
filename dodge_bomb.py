import sys
import pygame as pg
from random import randint

WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    fps = 50
    vx = vy = 5
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect()
    bomb_sfc = pg.Surface((40, 40))
    bomb_sfc.set_colorkey((0,0,0))
    bomb = pg.draw.circle(bomb_sfc, (255,0,0), (20,20), 10)
    bomb.center = (randint(0,1600), randint(0,800))
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        kk_move = [0, 0]
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]: kk_move[1] -= 5
        if key_lst[pg.K_DOWN]: kk_move[1] += 5
        if key_lst[pg.K_RIGHT]: kk_move[0] += 5
        if key_lst[pg.K_LEFT]: kk_move[0] -= 5

        if kk_rect.colliderect(bomb):
            return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rect)
        screen.blit(bomb_sfc, bomb)
        pg.display.update()
        bomb.move_ip((vx,vy))
        kk_rect.move_ip(kk_move)
        if out_display(bomb)[0] or out_display(bomb)[1]:
            pass
        else:
            if out_display(bomb)[0] == False:
                vx *= -1
            if out_display(bomb)[1] == False:
                vy *= -1
            bomb.move_ip(vx, vy)
            

        tmr += 1
        clock.tick(fps)

def out_display(obj_rect):
    """
    画面内判定をする関数
    引数:こうかとんRect or 爆弾Rect
    戻り値：横方向・縦方向の真理値タプル
    """
    out_x = out_y = True
    if obj_rect.top < 0 or obj_rect.bottom > 900:
        print(obj_rect.bottom)
        out_x = False
    if obj_rect.left < 0 or obj_rect.right > 1600:
        print(obj_rect.left)
        out_y = False
    return (out_x, out_y)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()