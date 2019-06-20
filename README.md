# chatbot-pi
聊天机器人、智能音箱......(Ubuntu16.04、Raspberry Pi 3 测试成功)

## 启动
$ python main.py (确保有输入输出设备......)
```
Q: 世界上最漂亮的人是谁
A: 大概是如花吧，因为貌美如花啊！
Q: 播放光年之外
A: xxxxxx 此时应有背景音乐......
......

Q保存到audio/audio.wav
A保存到audio/audio.mp3
歌曲保存到audio/song.mp3
```

## snowboy唤醒词
### [安装](https://github.com/Kitt-AI/snowboy)
```
# 安装 pyaudio sox
$ sudo apt-get install python-pyaudio python3-pyaudio sox ffmpeg mplayer
$ pip install pyaudio

# 安装 swig
$ wget http://downloads.sourceforge.net/swig/swig-3.0.10.tar.gz
$ tar xvf swig-3.0.10.tar.gz
$ cd swig-3.0.10
$ sudo apt-get install -y libpcre3 libpcre3-dev
$ ./configure --prefix=/usr --without-clisp --without-maximum-compile-warnings
$ make
$ sudo make install
$ sudo install -v -m755 -d /usr/share/doc/swig-3.0.10
$ sudo cp -v -R Doc/* /usr/share/doc/swig-3.0.10

# 安装 atlas
$ sudo apt-get install -y libatlas-base-dev

# 安装 snowboy
$ wget https://github.com/Kitt-AI/snowboy/archive/v1.3.0.tar.gz
$ tar -xvjf snowboy-1.3.0.tar.gz
$ cd snowboy/swig/Python3
$ sudo make
```

### 使用
复制以下文件到项目目录:
`resources/common.res`
`resources/ding.wav`
`resources/dong.wav`
`example/Python3/_snowboydetect.so`
`example/Python3/snowboydetect.py`
`example/Python3/snowdecoder.py`

snowboydetect.py 是一个由 SWIG 生成的 Python 封装文件。
因为它很难阅读，我们创建了另一个高级封装：snowboydecoder.py。

```
import snowboydecoder

......

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)

# main loop
detector.start(detected_callback=snowboydecoder.play_audio_file,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
```

### 语料
我的唤醒词: 小七小七(resources/xiaoqi.pmdl)

可以创建自己的唤醒词: https://snowboy.kitt.ai/dashboard

## 百度API
```
pip install baidu-aip
```

语音识别文档
http://ai.baidu.com/docs#/ASR-Online-Python-SDK/top

语音合成文档
http://ai.baidu.com/docs#/TTS-Online-Python-SDK/top

## 图灵API
```
pip install requests
pip install bs4
sudo apt-get install python3-lxml
```

智能问答文档
http://www.tuling123.com/help/h_cent_webapi.jhtml

## 网易云音乐
根据歌名搜索歌曲，获取歌曲的id，然后根据外链下载歌曲：
>* `来自天堂的魔鬼` http://music.163.com/song/media/outer/url?id=36270426.mp3
>* `光年之外` http://music.163.com/song/media/outer/url?id=449818741.mp3
>* `泡沫` http://music.163.com/song/media/outer/url?id=26113988.mp3

代码参考: https://blog.csdn.net/qq_38282706/article/details/80300475
