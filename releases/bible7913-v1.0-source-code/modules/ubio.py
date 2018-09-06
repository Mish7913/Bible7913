#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright: 2017 Mish7913 <mish7913@gmail.com>
#  License:   GNU General Public License v2 or later

import os, sys, codecs;

path = os.path.dirname(os.path.abspath(__file__));
sys.path.insert(0, path + '/dp');
about = 'Біблія: Переклад. Івана Огієнка, 1988';
from ubio_index import index
list_books = "Буття,Вихід,Левит,Числа,Повторення Закону,Iсус Навин,Книга Суддiв,Рут,1-а Самуїлова,2-а Самуїлова,1-а Царiв,2-а Царiв,1-а Хронiки,2-а Хронiки,Ездра,Неемія,Естер,Йов,Псалми,Приповiстi,Екклезiяст,Пiсня над пiснями,Iсая,Єремiя,Плач Єремiї,Єзекiїль,Даниїл,Осiя,Йоїл,Амос,Овдiй,Йона,Михей,Наум,Авакум,Софонiя,Огiй,Захарiя,Малахiї,Вiд Матвiя,Вiд Марка,Вiд Луки,Вiд Iвана,Дiї,Якова,1-е Петра,2-е Петра,1-е Iвана,2-е Iвана,3-е Iвана,Юда,До Римлян,1-е до Коринтян,2-е до Коринтян,До Галатiв,До Ефесян,До Филип'ян,До Колоссян,1-е до Солунян,2-е до Солунян,1-е Тимофiю,2-е Тимофiю,До Тита,До Филимона,До Євреїв,Об'явлення";
from ubio_book import get_book

def prv_text(dic, num = 0):
	global index; list_items = []; num = 0;
	
	for word in dic:
		try:
			if (num == 0): list_items = set(index[word]); num = 1;
			else: list_items = list_items.intersection(set(index[word]));
		except KeyError: [];
		
	return list(list_items);
	
def module_search(idx, string, mode = 0):
	global index; keys = []; list_items = "";
	if (mode == 1):
		for key in index:
			if (key.decode('utf-8')[0:len(string.decode('utf-8'))] == string.decode('utf-8')):
				for in_key in index[key]: keys.append(in_key);
	elif (mode == 2):
		for key in index:
			if (key.decode('utf-8')[-len(string.decode('utf-8')):] == string.decode('utf-8')):
				for in_key in index[key]: keys.append(in_key);
	else: keys = prv_text(string);
	
	result = list(set(keys));
	for i in result: list_items += i + "|";
	return list_items;
