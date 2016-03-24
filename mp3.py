#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from bit import bitfuncs

# class
# ==================================================
class DummyMp3Maker:
	'''ダミーmp3作成クラス'''
	@staticmethod
	def make_header():
		'''ダミーのヘッダを生成する'''
		header_bytes = [
			#*frame sync (常に固定値)
			[1, 1, 1, 1, 1, 1, 1, 1],
			#*frame sync *version MPEG1  *layer III  *protection CRC無
			[1, 1, 1,    1, 1,           0, 1,       1],
			#*bit rate 128kbps  *sampling rate 44100  *pad  *extension
			[1, 0, 0, 1,        0, 0,                 0,    0],
			#*channel mode js   *mode extension(dummy) *copyright 著作権なし  *original  *emphasis
			[0, 1,              0, 0,                  0,                     0,         0, 0]
		]
	
		header = bytearray()
		for bytes in header_bytes:
			header.append(bitfuncs.bits2int(bytes))
		return header
	
	def __init__(self):
		self.dummy_buf = bytearray()
		self.buf_len = 32768
	
	def createbuf(self):
		'''ダミーデータソースを作成する'''
		self.dummy_buf.clear()
		lower = random.randrange(0, 128)
		upper = lower + random.randrange(1, 64)
		for i in range(self.buf_len):
			self.dummy_buf.append(random.randrange(lower, upper))
	
	def make_dummyframe(self):
		'''ダミーのフレームを作成する'''
		left  = random.randrange(0, self.buf_len - 414)
		right = left + 413	# フレームサイズ (1152サンプル*128bps*1000/8/44100 = 417.959 → 417-4byte(header)=413 ?)
		return self.dummy_buf[left:right]
	
	def writefile(self, filename):
		'''ダミーのmp3ファイルを作成する'''
		header = DummyMp3Maker.make_header()
		with open(filename, "wb") as f:
			max_frame = random.randrange(2048, 20480)
			for i in range(max_frame):
				f.write(header)
				f.write(self.make_dummyframe())
			f.write(header)
