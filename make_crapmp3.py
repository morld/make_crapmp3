#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 今のところ当コードはpython3専用
# ==================================================
import sys
import six
if not six.PY3:
	print("ERROR: this code is only python3...")
	sys.exit()

# import
# ==================================================
import os
import linecache
import struct
import random

# class
# ==================================================
class ArgParser:
	'''オプション解析 クラス'''
	
	def __init__(self, argv):
		'''初期化'''
		
		self.output_path	= "."
		self.dic_name		= ""
		self.filecnt		= 1
		
		index  = 0
		maxarg = len(argv)
		while True:
			if maxarg <= index: break
			opt = argv[index]
			# 出力先
			if opt == "-o":
				index += 1
				if maxarg <= index: break
				self.output_path = argv[index]
			# ファイル名辞書
			elif opt == "-dic":
				index += 1
				if maxarg <= index: break
				self.dic_name = argv[index]
			# ファイル数
			elif opt == "-c":
				index += 1
				if maxarg <= index: break
				self.filecnt = int(argv[index])
				if self.filecnt < 1:
					print("WARN: invalid file cnt: " + argv[index])
					self.filecnt = 1
			index += 1

# function
# ==================================================
def bits2int(bits):
	'''bit列を整数値に変換'''
	
	result = 0
	for bit in bits:
		result = result << 1 | bit
	return result

def pickword(dic_filename):
	'''辞書から適当な単語を選ぶ'''
	dummy_title = ""
	
	try:
		f = open(dic_filename, "r")
	except FileNotFoundError:
		print("MESSAGE: not found dictionary.")
	else:
		dic_linecnt = sum(1 for line in f)		# ファイル行数カウント
		
		# 適当なタイトルを作る
		if 0 < dic_linecnt:
			dummy_title = linecache.getline(dic_filename, random.randrange(1, dic_linecnt + 1)).rstrip()
			for i in range(random.randrange(0, 2)):
				dummy_title += " "
				dummy_title += linecache.getline(dic_filename, random.randrange(1, dic_linecnt + 1)).rstrip()
			f.close()
	return dummy_title

def main():
	'''メイン処理'''
	
	arg = ArgParser(sys.argv)
	
	# dicをチェック
	dummy_title = pickword(arg.dic_name)
	if dummy_title is "":
		dummy_title = "crap"
	
	# フォルダ生成
	if arg.filecnt is 1:
		output_path = arg.output_path
	else:
		output_path = arg.output_path + "\\" + dummy_title
	output_path = os.path.abspath(output_path) + "\\"
	
	if not os.path.exists(output_path):
		try:
			os.mkdir(output_path)
		except FileNotFoundError:
			print("ERROR! can not create directory: " + output_path)
			sys.exit()
	print("output: " + output_path)
	
	# ダミーデータソースを作成
	buf_len = 32768
	dummy_buf = bytearray()
	
	lower = random.randrange(0, 128)
	upper = lower + random.randrange(1, 64)
	for i in range(buf_len):
		dummy_buf.append(random.randrange(lower, upper))
	
	# それっぽいヘッダを生成
	header = bytearray()
							#frame sync (常に固定値)
	header.append(bits2int([1, 1, 1, 1, 1, 1, 1, 1]))
							#frame sync	#version MPEG1	#layer III	#protection CRC無
	header.append(bits2int([1, 1, 1,	1, 1,			0, 1,		1]))
							# bit rate 128kbps	#sampling rate 44100	# pad 	#extension
	header.append(bits2int([1, 0, 0, 1,			0, 0,					0,		0]))
							# channel mode js		#mode extension(dummy)	#copyright 著作権なし	#original	#emphasis
	header.append(bits2int([0, 1,					0, 0,					0,				 		0,			0, 0]))
	
	for filecnt in range(arg.filecnt):
		filename = ""
		if arg.filecnt is 1:
			filename += dummy_title
		else:
			filename += "%02d" %(filecnt + 1) + "." + dummy_title
		filename += ".mp3"
		print(" " + filename)
		f = open(output_path + filename, "wb")
		
		# ゴミ生成
		max_frame = random.randrange(2048, 20480)
		for i in range(max_frame):
			left  = random.randrange(0, buf_len - 414)
			right = left + 413			# フレームサイズ (1152サンプル*128bps*1000/8/44100 = 417.959.. ?)
			f.write(header)				# TODO: 正確なフレームサイズを確認する
			f.write(dummy_buf[left:right])
		f.write(header)
		f.close
	print("finish.")


# invoke mainline
# ==================================================
if __name__ == "__main__":
	main()

