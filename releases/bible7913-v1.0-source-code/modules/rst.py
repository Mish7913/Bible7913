#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright: 2017 Mish7913 <mish7913@gmail.com>
#  License:   GNU General Public License v2 or later

import os, sys, codecs;

path = os.path.dirname(os.path.abspath(__file__));
sys.path.insert(0, path + '/dp');
about = 'Библия: Синодальный перевод.';
from rst_index import index
list_books = "Бытие,Исход,Левит,Числа,Второзаконие,Книга Иисуса Навина,Книга Судей,Руфь,1-е Царств,2-е Царств,3-е Царств,4-е Царств,1-е Паралипоменон,2-е Паралипоменон,Ездра,Неемия,Есфирь,Иов,Псалтирь,Притчи,Екклесиаст,Песня Песней,Исаия,Иеремия,Плач Иеремии,Иезекииль,Даниил,Осия,Иоиль,Амос,Авдий,Иона,Михей,Наум,Аввакум,Софония,Аггей,Захария,Малахия,от Матфея,от Марка,от Луки,от Иоанна,Деяния Апостолов,Послание Иакова,1-е Петра,2-е Петра,1-е Иоанна,2-е Иоанна,3-е Иоанна,Послание Иуды,Послание к Римлянам,1-е послание к Коринфянам,2-е послание к Коринфянам,Послание к Галатам,Послание к Ефесянам,Послание к Филиппийцам,Послание к Колоссянам,1-е послание к Фессалоникийцам,2-е послание к Фессалоникийцам,1-е послание к Тимофею,2-е послание к Тимофею,Послание к Титу,Послание к Филимону,Послание к Евреям,Откровение";
from rst_book import get_book

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
