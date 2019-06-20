#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pyaudio
import wave
import os


# 录制音频
def audio_record(audio_file):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16  # 16bit编码格式wav
    CHANNELS = 1  # 单声道
    RATE = 16000  # 16000采样频率
    RECORD_SECONDS = 2.5  # 记录时间
    p = pyaudio.PyAudio()
    # 创建音频流
    stream = p.open(format=FORMAT,  # 16bit编码格式wav
                    channels=CHANNELS,  # 单声道
                    rate=RATE,  # 采样率16000
                    input=True,
                    frames_per_buffer=CHUNK)
    print("Start Recording...")
    frames = []  # 录制的音频流
    # 录制音频数据
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    # 录制完成
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("Recording Done...")
    # 保存音频文件
    wf = wave.open(audio_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


# 播放音频
def audio_play(audio_file):
    os.system('mplayer %s > /dev/null 2>&1' % audio_file)
