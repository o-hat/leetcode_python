#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by sundazhong on 2019/10/10 18:35.
"""


def echo(value=None):
	print("Begin ... ...")
	try:
		value = yield value
	except Exception as e:
		value = e
	finally:
		print("clear Up 。。。 。。。")


generator = echo(1)
print(generator)
