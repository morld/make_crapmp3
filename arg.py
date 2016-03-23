#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
