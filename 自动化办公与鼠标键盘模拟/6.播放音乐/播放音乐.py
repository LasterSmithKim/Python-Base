import time
import pygame

#pip install pygame

#播放音乐的路径
filePath = "/Users/jinpeihua/PycharmProjects/Python语言基础视频课程/入门教程一/自动化办公与鼠标键盘模拟/6.播放音乐/res/Home.mp3"
#初始化
pygame.mixer.init()
#加载音乐
track = pygame.mixer.music.load(filePath)
#播放音乐
pygame.mixer.music.play()
#播放时间长度
time.sleep(5)

#pygame.mixer.music.pause()


#停止
pygame.mixer.music.stop()


