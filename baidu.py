#!/usr/bin/python
# -*- coding: UTF-8 -*-

from aip import AipSpeech
import util


class Baidu:
    APP_ID = '16434481'
    API_KEY = 'GVZbup1aU4r18bGDfV3yTldX'
    SECRET_KEY = 'EfamQgGUhtEQdUPVAzWLswVk3Cee4PFO'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    # 语音识别
    def asr(self, audio_file):
        with open(audio_file, 'rb') as fp:
            result = self.client.asr(fp.read(), 'wav', 16000, {
                'dev_pid': 1536,
            })
            return result

    # 语音合成
    def synthesis(self, content, audio_file):
        result = self.client.synthesis(content, 'zh', 1, {
            'vol': 5,
        })
        # 识别正确返回语音二进制 错误则返回dict
        if not isinstance(result, dict):
            with open(audio_file, 'wb') as f:
                f.write(result)


#################### 语音识别 ####################
if __name__ == '__main__':
    baidu = Baidu()
    util.audio_record('audio/audio.wav')
    response = baidu.asr('audio/audio.wav')

    if response['err_no'] == 0:
        print(response['result'][0])
    else:
        print('%d: %s' % (response['err_no'], response['err_msg']))

#################### 语音合成 ####################
if __name__ == '__main__':
    baidu = Baidu()
    baidu.synthesis('世界上最漂亮的人是谁', 'audio/audio.mp3')
    util.audio_play('audio/audio.mp3')
