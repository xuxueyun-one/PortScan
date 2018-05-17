#!/usr/bin/env python
#! -*- coding:utf-8 -*-

from ctypes import *

lib = cdll.LoadLibrary(u'./scan.so')

lib.Scan("14.215.177.38","1-1024","eth0")

