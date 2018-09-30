#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright: 2017 Mish7913 <mish7913@gmail.com>
#  License:   GNU General Public License v2 or later

import os, sys, codecs;

path = os.path.dirname(os.path.abspath(__file__));
sys.path.insert(0, path + '/dp');
about = 'Bible: Original Text.';
from orig_index import index
list_books = "בראשית,שמות,ויקרא,במדבר,דברים,יהושע,שופטים,רות,שמואל א,שמואל ב,מלכים א,מלכים ב,דברי הימים א,דברי הימים ב,עזרא,נחמיה,אסתר,איוב,תהלים,משלי,קהלת,שיר השירים,ישעיהו,ירמיהו,איכה,יחזקאל,דניאל,הושע,יואל,עמוס,עבדיה,יונה,מיכה,נחום,חבקוק,צפניה,חגי,זכריה,מלאכי,Κατά Ματθαίον,Κατά Μάρκον,Κατά Λουκάν,Κατά Ιωάννην,Πράξεις,Ιακώβου,Πέτρου Α΄,Πέτρου Β΄,Ιωάννου Α΄,Ιωάννου Β΄,Ιωάννου Γ΄,Ιούδα,Προς Ρωμαίους,Προς Κορινθίους Α',Προς Κορινθίους Β',Προς Γαλάτας,Προς Εφεσίους,Προς Φιλιππησίους,Προς Κολοσσαείς,Προς Θεσσαλονικείς Α΄,Προς Θεσσαλονικείς Β΄,Προς Τιμόθεον Α΄,Προς Τιμόθεον Β΄,Προς Τίτον,Προς Φιλήμονα,Προς Εβραίους,Αποκάλυψις Ιωάννου";
from orig_book import get_book

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
	result.sort();
	for i in result: list_items += i + "|";
	return list_items;
