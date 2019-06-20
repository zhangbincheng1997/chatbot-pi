#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
1. 唤醒 √
2. 响应 √
3. 输入 √
4. 理解 √
5. 反馈 √
"""

from baidu import Baidu
from tuling import TuLing
from netease import NetEase
from snowboy import snowboydecoder
import util
import signal
import os


class ChatBot:

    def __init__(self):
        self.interrupted = False

        # capture SIGINT signal, e.g., Ctrl+C
        signal.signal(signal.SIGINT, self.signal_handler)
        print('Listening... Press Ctrl+C to exit')

        self.baidu = Baidu()
        self.tuling = TuLing()
        self.netease = NetEase()

    def signal_handler(self, signal, frame):
        self.interrupted = True

    def interrupt_callback(self):
        return self.interrupted

    def chat(self):
        # ding
        util.audio_play('snowboy/resources/ding.wav')

        # 录制音频
        util.audio_record('audio/audio.wav')
        # 语音识别
        response = self.baidu.asr('audio/audio.wav')

        # dong
        util.audio_play('snowboy/resources/dong.wav')

        if response['err_no'] == 0:
            question = response['result'][0]
            print('Q: ' + question)

            # 比较粗糙的实现......
            if question.find('播放') == -1:
                # 智能问答
                answer = self.tuling.tuling(question)
                print('A: ' + answer)

                # 语音合成
                self.baidu.synthesis(answer, 'audio/audio.mp3')
                # 播放音频
                util.audio_play('audio/audio.mp3')
            else:
                # 下载歌曲
                song_name = question[2:]
                self.netease.download_song(song_name, 'audio/song.mp3')
                # 播放音频
                util.audio_play('audio/song.mp3')
        else:
            print('%d: %s' % (response['err_no'], response['err_msg']))


if __name__ == '__main__':
    model = 'snowboy/resources/xiaoqi.pmdl'
    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)

    chatbot = ChatBot()

    # main loop
    detector.start(detected_callback=chatbot.chat,
                   interrupt_check=chatbot.interrupt_callback,
                   sleep_time=0.03)

    detector.terminate()
