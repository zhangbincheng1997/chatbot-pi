#!/usr/bin/python
# -*- coding: UTF-8 -*-

from aip import AipSpeech
import pyaudio
import wave
import os

import deep

APP_ID = '16434481'
API_KEY = 'GVZbup1aU4r18bGDfV3yTldX'
SECRET_KEY = 'EfamQgGUhtEQdUPVAzWLswVk3Cee4PFO'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

"""
流程：
1. 录制音频
2. 语音识别
3. 智能问答
4. 语音合成
5. 播放音频
"""


# 录制音频
def audio_record(out_file):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16  # 16bit编码格式wav
    CHANNELS = 1  # 单声道
    RATE = 16000  # 16000采样频率
    RECORD_SECONDS = 5  # 记录时间
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
    wf = wave.open(out_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


# 语音识别
def asr(audio_file):
    with open(audio_file, 'rb') as fp:
        result = client.asr(fp.read(), 'wav', 16000, {
            'dev_pid': 1536,
        })
        return result


# 语音合成
def synthesis(content, audio_file):
    result = client.synthesis(content, 'zh', 1, {
        'vol': 5,
    })
    # 识别正确返回语音二进制 错误则返回dict
    if not isinstance(result, dict):
        with open(audio_file, 'wb') as f:
            f.write(result)


# 播放音频
def audio_play(audio_file):
    os.system('mplayer %s' % audio_file)


if __name__ == '__main__':
    # 录制音频
    audio_record('audio/audio.wav')
    # 语音识别
    response = asr('audio/audio.wav')

    if response['err_no'] == 0:
        question = response['result'][0]
        print('Q: ' + question)

        # 智能问答
        answer = deep.tuling(question)
        print('A: ' + answer)

        # 语音合成
        synthesis(answer, 'audio/audio.mp3')
        # 播放音频
        audio_play('audio/audio.mp3')
    else:
        print('%d: %s' % (response['err_no'], response['err_msg']))
