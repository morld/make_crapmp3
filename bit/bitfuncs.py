#!/usr/bin/env python
# -*- coding: utf-8 -*-

# function
# ==================================================
def bits2int(bits):
	'''bit列を整数値に変換'''
	
	result = 0
	for bit in bits:
		result = result << 1 | bit
	return result
