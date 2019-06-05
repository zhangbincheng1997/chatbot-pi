#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 安装: https://wukong.hahack.com/#/install?id=方式二：手动安装
# 代码: https://s3-us-west-2.amazonaws.com/snowboy/snowboy-releases/ubuntu1404-x86_64-1.1.1.tar.bz2
# 语料: https://snowboy.kitt.ai/dashboard

"""
1. 唤醒 √
2. 响应
3. 输入
4. 理解
5. 反馈
"""

import snowboydecoder
import signal

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


model = 'xiaoqi.pmdl'

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=snowboydecoder.play_audio_file,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
