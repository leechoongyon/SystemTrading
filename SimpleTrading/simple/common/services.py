# -*- coding: utf-8 -*-
from __future__ import division
import os,sys

# 설명
# 모델을 학습시키고 종목을 선택하는 데 필요한 환경 설정을
# 저장하고 관리하는 일종의 레지스트리로, 전역변수로 선언되어 모든 클래스에서
# 사용할 수 있다.


class BaseService():
	def __init__(self):
		self.items = {}

	def clear(self):
		self.items.clear()

	def register(self,name,value):
		self.items[name] = value

	def get(self,name):
		return self.items[name]


class Configurator(BaseService):
	def __init__(self):
		self.items = {}

	def update(self,name,value):
		self.items[name] = value


class Services(BaseService):
	def register(self,name,ref):
		self.items[name] = ref

	def getInstance(self):
		return self.services

services = Services()
