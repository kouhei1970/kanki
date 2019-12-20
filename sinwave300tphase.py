# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:01:42 2019

@author: k2510120
"""

import numpy as np
import wave
import struct
 
fname = 'sinwave300t528phase.wav'
wf = wave.open(fname, 'w')
ch = 1
width = 2
samplerate = 44100
wf.setnchannels(ch)
wf.setsampwidth(width)
wf.setframerate(samplerate)

time = 300
numsamples = time * samplerate

# python 2.x では ( ) を取る
#print( u"チャンネル数 = ", ch)
#print( u"サンプル幅 (バイト数) = ", width)
#print( u"サンプリングレート(Hz) =", samplerate)
#print( u"サンプル数 =", numsamples)
#print( u"録音時間 =", time)

# 信号データを作る (numpy の ndarray で)
freq = 528                           # 周波数 freq を 440 Hz にする
x=np.linspace(0, time, numsamples+1) # 0≦t≦time をnumsamples等分
y=np.sin(2 * np.pi * freq * x+np.pi) # 周波数 freq (Hz) の正弦波
y=np.rint(32767*y/max(abs(y)))       # [-32767,32767] の範囲に収める
y=y.astype(np.int16)                 # 16ビット整数に型変換する
y=y[0:numsamples]                    # numsamples 個のデータに打ち切る

# ndarray から bytes オブジェクトに変換
data=struct.pack("h" * numsamples , *y)

# データを書き出す
wf.writeframes(data)
wf.close()