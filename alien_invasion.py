import sys
import pygame
from pygame.sprite import Group
from settings import Settings 
from ship import Ship
from game_stats import GameStats
from button import Button
import game_functions as gf

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height),
        #pygame.FULLSCREEN
    )
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button =  Button(ai_settings, screen, 'Play')
    
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:        
            # 飞船移动
            ship.update()

            # 更新子弹位置并删除已经消失的子弹
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

            # 外星人移动
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # 更改屏幕上的图像并切换到新的屏幕
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()