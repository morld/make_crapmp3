#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 今のところ当コードはpython3専用
# ==================================================
import sys
if sys.version_info < (3,0,0):
	sys.exit()

# import
# ==================================================
import os
import linecache
import random
import arg
import mp3

# function
# ==================================================
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

def maketrash():
	'''メイン処理'''
	args = arg.ArgParser(sys.argv)
	
	# dicをチェック
	dummy_title = pickword(args.dic_name)
	if dummy_title is "":
		dummy_title = "crap"
	
	# フォルダ生成
	if args.filecnt is 1:
		output_path = args.output_path
	else:
		output_path = args.output_path + "\\" + dummy_title
	output_path = os.path.abspath(output_path) + "\\"
	
	if not os.path.exists(output_path):
		try:
			os.mkdir(output_path)
		except FileNotFoundError:
			print("ERROR! can not create directory: " + output_path)
			sys.exit()
	print("output: " + output_path)
	
	mp3maker = mp3.DummyMp3Maker()
	mp3maker.create_dummybuf()
	header = mp3.DummyMp3Maker.make_header()	# それっぽいヘッダを生成
	
	for filecnt in range(args.filecnt):
		filename = ""
		if args.filecnt is 1:
			filename += dummy_title
		else:
			filename += "%02d" %(filecnt + 1) + "." + dummy_title
		filename += ".mp3"
		print(" " + filename)
		with open(output_path + filename, "wb") as f:
			max_frame = random.randrange(2048, 20480)
			for i in range(max_frame):
				f.write(header)
				f.write(mp3maker.make_dummyframe())
			f.write(header)
	print("finish.")


# invoke mainline
# ==================================================
if __name__ == "__main__":
	maketrash()

