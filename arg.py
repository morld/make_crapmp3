#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

# class
# ==================================================
class ArgParser:
	'''オプション解析 クラス'''
	
	def __init__(self):
		'''初期化'''
		parser = argparse.ArgumentParser(description="Make crap MP3.")
		parser.add_argument("--o", 	default="",	help="output filename")
		parser.add_argument("--c", 	default=1,	help="num of output file", type=int)
		parser.add_argument("--dic",default="",	help="script choose words randomly in dictionary to make filename")
		args = parser.parse_args()
		
		self.output_path = args.o
		self.dic_name = args.dic
		self.filecnt = args.c
