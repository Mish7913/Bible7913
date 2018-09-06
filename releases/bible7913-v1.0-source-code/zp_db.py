#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Copyright 2017 Mish7913 <Mish7913@gmail.com> ##

#*
#* This program is free software; you can redistribute it and/or modify
#* it under the terms of the GNU General Public License as published by
#* the Free Software Foundation; either version 2 of the License, or
#* (at your option) any later version.
#*
#* This program is distributed in the hope that it will be useful,
#* but WITHOUT ANY WARRANTY; without even the implied warranty of
#* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#* GNU General Public License for more details.
#*
#* You should have received a copy of the GNU General Public License
#* along with this program; if not, write to the Free Software
#* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#* MA 02110-1301, USA.
#*

import os, sys, ast, gi, re;

from ast import literal_eval as ltr;
from os.path import expanduser as exusr;

gi.require_version('Gtk', '3.0'); gi.require_version('WebKit', '3.0');
from gi.repository import Gtk as gtk, Gdk as gdk, WebKit;

dirname = os.path.dirname(os.path.abspath(__file__));
sys.path.insert(0, dirname); sys.path.insert(0, dirname + '/modules');

import ui, modules, style;

pst = exusr("~") + "/.config" if (os.name == "posix") else os.getenv('APPDATA') if (os.name == "nt") else dirname;
settings = {}; file_settings = pst + "/Mish7913/bible7913.settings"; lng = {}; no_active_scroll = True;
list_lng = []; list_lng_data = {}; list_lng_num = {}; menu_lng = {};

menu_settings = gtk.Menu(); lng_uk_UA = gtk.RadioMenuItem();

lng_ua = {'code':   'uk_UA',       'lng':      'Українська',    'EXIT':    'Вийти',       'ABOUT':     'Про програму', 
          'S_BOOK': 'Вибір книги', 'S_CHAP':   'Вибір розділу', 'S_VERSE': 'Вибір вірша', 'LNG_BOOKS': 'Мова книг', 
          'SEARCH': 'Пошук',       'SETTINGS': 'Налаштування'};

cID = gtk.Builder(); main_view = WebKit.WebView(); strong_view = WebKit.WebView(); search_view = WebKit.WebView();

def main(args):
	global file_settings, path, cID, settings; cID.add_from_string(ui.gtk3);
	
	list_modules = file_ltr(dirname + '/modules/list_modules');
	
	if os.path.isfile(file_settings) == False: save_settings(file_settings);
	settings = file_ltr(file_settings);
	
	main_window = obj("main_window"); main_window.connect("destroy", quit);
	main_window.set_icon_from_file('icon.svg');
	try:
		if settings['close_btn'] == "right": main_window.set_titlebar(obj("main_header_bar_right"));
		else: main_window.set_titlebar(obj("main_header_bar_left"));
	except KeyError: main_window.set_titlebar(obj("main_header_bar_left"));
	
	lng_uk_UA.set_label("Українська"); lng_uk_UA.connect("toggled", change_lng); menu_settings.append(lng_uk_UA);
	load_list_lng(); obj("lng_menu_label").set_submenu(menu_settings); menu_settings.show_all();
		
	try:
		if settings['lng'] != "uk_UA": lng = list_lng_data[settings['lng']]; menu_lng[list_lng_num[settings['lng']]].set_active(True);
		else: lng_uk_UA.set_active(True);
	except KeyError: lng_uk_UA.set_active(True);
	
	obj("btn_exit").connect("clicked", quit);          obj("btn_minimize").connect("clicked", minimize);
	obj("btn_maximize").connect("clicked", maximize);  obj("btn_about").connect("clicked", about_open);
	obj("btn_exit1").connect("clicked", quit);         obj("btn_minimize1").connect("clicked", minimize);
	obj("btn_maximize1").connect("clicked", maximize); obj("btn_about1").connect("clicked", about_open);
	
	obj("about").connect("destroy", about_hide); obj("about").connect("delete-event", about_hide);
	obj("about").connect("remove", about_hide);  obj("about").connect("close", about_hide);
	obj("about").connect("response", about_hide);
	
	obj("btn_search").connect("clicked", search_show);
	
	for translate in list_modules["translations"]:
		id = list_modules["translations"][translate][0]; obj("list_left_select").prepend(id, translate);	
		obj("list_right_select").prepend(id, translate); obj("search_list_books").prepend(id, translate);
		
	try: obj("list_left_select").set_active(settings["left_select"]); obj("list_right_select").set_active(settings["right_select"]);
	except KeyError: obj("list_left_select").set_active(0); obj("list_right_select").set_active(1);
	obj("search_list_books").set_active(0);
	
	obj("list_left_select").connect("changed", reload_page);
	obj("list_right_select").connect("changed", reload_page);
	
	try: obj("get_books_right").set_active(True) if (settings["get_translate"] == "right") else obj("get_books_left").set_active(True);
	except KeyError: obj("get_books_right").set_active(True); settings["get_translate"] = "right";
	obj("get_books_right").connect("toggled", load_books);
	
	obj("books_viewer").add(main_view); obj("dict_box").add(strong_view); obj("search_container").add(search_view);
	
	style_gtk3 = gtk.CssProvider(); style_gtk3.load_from_data(style.css);
	gtk.StyleContext.add_provider_for_screen( gdk.Screen.get_default(), style_gtk3, gtk.STYLE_PROVIDER_PRIORITY_APPLICATION );
	
	try: run_book = settings["sel_book"]; run_chap = settings["sel_chap"]; run_vrse = settings["sel_verse"];
	except KeyError: run_book = 0; run_chap = 0; run_vrse = 0;
	use_lng(); load_books(); load_chapters(); load_verses(); load_two_translations();
	
	obj("list_books_select").connect("changed", load_chapters);
	obj("list_chapters_select").connect("changed", load_verses);
	obj("list_verse_select").connect("changed", open_verse);
	
	obj("list_books_select").set_active(run_book);
	obj("list_chapters_select").set_active(run_chap);
	obj("list_verse_select").set_active(run_vrse);
	
	main_view.connect('title-changed', load_word_indict);
	strong_view.connect('title-changed', load_word_indict, True);
	search_view.connect('title-changed', search_view_loab_book);
	
	obj("search_entry").connect("icon-press", search_func);
	obj("search_entry").connect("activate", search_func);
	
	if (os.path.isfile('/tmp/bible7913.strong')): strong_view.open('file:///tmp/bible7913.strong');
	main_window.show_all(); main_window.maximize(); obj("search_dict").hide(); main_window.set_title("Bible7913");
	
	gtk.main();
	
	return 0
	
def search_view_loab_book(webView = None, frame = None, title = None):
	title = title.split('.'); obj("list_books_select").set_active(int(title[0])-1);
	obj("list_chapters_select").set_active(int(title[1])-1); obj("list_verse_select").set_active(int(title[2])-1);
	obj("search_window").hide(); open_verse();
	
def search_show(widget = None, data = None):
	about_hide();
	try: obj("dialog_header_bar").set_title(lng["SEARCH"]);
	except KeyError: obj("dialog_header_bar").set_title("Пошук");
	obj("btn_exit_dialog").connect("clicked", search_hide); obj("dialog_header_bar").unparent();
	obj("search_window").set_titlebar(obj("dialog_header_bar")); obj("search_window").show_all();
def search_hide(widget = None, data = None): obj("search_window").hide();
	
def search_text(text, module_search):
	if (text[-1:] == '*'):
		return (module_search(0, text.replace('*', ''), 1));
	else:
		if (text[0:1] == '*'):
			return (module_search(0, text.replace('*', ''), 2));
		else:
			search = text.split(' ');
	return module_search(0, search);
		
def search_func(entry, icon_pos = None, event = None, user_data = None):
	global modules;
	nmb = obj("search_list_books").get_active();
	nmb_2 = obj("list_right_select").get_active();
	md_src = modules.module[nmb]; md2_src = modules.module[nmb_2]; text = "";
	for i in search_text(obj("search_entry").get_text(), md_src.module_search).split("|"):
		if (i):
			map_word = i.split(".");
			rtl = 'dir="rtl" style="text-align: right;"' if (int(map_word[0]) < 40) and (nmb == 0) else 'dir="ltr"';
			find_test = obj("search_entry").get_text(); prb = "'";
			search_text_mode = md_src.get_book[int(map_word[0])][int(map_word[1])][int(map_word[2])];
			search_text_rep = re.sub('<S>.*?</S>', '', search_text_mode);
			text += '<tr><td valign="top" width="60%"><ul><li '+rtl+'><font class="word" onclick="get_word('+prb+i+prb+')">' + "<font class='label'>◉ (" + \
			md_src.list_books.split(",")[int(map_word[0])-1] + "." + map_word[1] + "." + map_word[2] + ")</font> " + \
			search_text_rep.replace(find_test.replace("*", ""), "<b>" + find_test.replace("*", "") + "</b>") + '</font></li></ul></td>';
				
			if (nmb != nmb_2):
				rtl_2 = 'dir="rtl" style="text-align: right;"' if (int(map_word[0]) < 40) and (nmb_2 == 0) else 'dir="ltr"';
				search_text_mode_2 = md2_src.get_book[int(map_word[0])][int(map_word[1])][int(map_word[2])];
				search_text_rep_2 = re.sub('<S>.*?</S>', '', search_text_mode_2);
				text += '<td valign="top" width="40%"><ul><li '+rtl_2+ '>' + "<font class='label'>◉ (" + \
				md2_src.list_books.split(",")[int(map_word[0])-1] + "." + map_word[1] + "." + map_word[2] + ")</font> <font>" + \
				search_text_rep_2 + '</font></li></ul></td></tr>';
			else: text += "</tr>";
			
	file_search = open('/tmp/bible7913.search', 'w+');
	file_search.write("""<!DOCTYPE html><head><meta content='text/html; charset=UTF-8' http-equiv='Content-Type'/>
		<style>.word{ cursor:pointer;color:#000; }.word:hover{ color:#0000FF; } body{ width:100%; overflow-y:scroll;
		margin: 5px auto; padding: 0; min-width: 50px; max-width: 100%; } ul{list-style-type:none; margin: 0 auto; padding: 0; } 
		li{padding-bottom: 5px} .label{border-bottom:1px solid #ccc; font-style:italic;} td{border-bottom:1px solid #aaa;}</style>
		<script type='text/javascript'> function get_word(word){ document.title = word; }</script><body><table width="100%">""" + 
	text + "</table></body></html>"); file_search.close();
	search_view.open('file:///tmp/bible7913.search');
	
def load_list_lng():
	global list_lng, list_lng_data, menu_lng;
	obj("lng_menu_label").set_label("Languages"); path_lng = dirname + "/lng";
	list_lng = [f for f in os.listdir(path_lng) if os.path.isfile(os.path.join(path_lng, f))];
	for i in range(0, len(list_lng)):
		file_lng = open(dirname + "/lng/" + list_lng[i], "r");
		list_lng_data[list_lng[i]] = ltr(file_lng.read());
		list_lng_num[list_lng[i]] = i; file_lng.close();
			
		menu_lng[i] = gtk.RadioMenuItem(group = lng_uk_UA);
		menu_lng[i].set_label(list_lng_data[list_lng[i]]["lng"]);
		menu_lng[i].connect("toggled", change_lng);
		menu_settings.append(menu_lng[i]);

def change_lng(widget, data = None):
	global menu_lng, lng, list_lng, list_lng_data, settings;
	if (lng_uk_UA.get_active()):
		lng = lng_ua; settings["lng"] = "uk_UA";
	for i in menu_lng:
		if (menu_lng[i].get_active()):
			settings["lng"] = list_lng[i];
			lng = list_lng_data[list_lng[i]];
	use_lng();
		
def load_word_indict(webView, frame, title, data = None):
	global no_active_scroll
	if (title[0:1] == "#"):
		is_active_scroll = False
		obj("list_verse_select").set_active(int(title.replace("#", ""))-1);
		is_active_scroll = True
	else:
		active_book = obj("list_books_select").get_active() + 1;
		if data == True: word = title.replace("S:", "");
		else: word = title.replace("''", "").replace(":", "");
		if is_int(word): code = "H" if (active_book < 40) else "G";
		else: code = '';
		nmb = obj("list_dict_select").get_active();
		try:
			text = modules.strong[nmb].get_strong[code + word];
			text = text.replace("<a href='", "<font class='word' onclick=get_word('");
			text = text.replace("'>", "')>"); text = text.replace("</a>", "</font>");
			file_left = open('/tmp/bible7913.strong', 'w+');
			file_left.write("""<!DOCTYPE html><head><meta content='text/html; charset=UTF-8' http-equiv='Content-Type'/>
				<style>.word{cursor:pointer;color:#0000FF;text-decoration: underline;}.word:hover{color:#8888FF;} body { background: #fff;
				text-decoration: none; overflow-y:scroll; margin: 0 auto; padding: 10px; min-width: 100px; max-width: 100%;} </style>
				<script type='text/javascript'> function get_word(word){ document.title = word; }</script><body>""" + \
			text + """</body></html>"""); file_left.close();
			strong_view.open('file:///tmp/bible7913.strong');
		except KeyError: None;
		
def is_int(var):
	try: int(var); return True
	except ValueError: return False
	
def open_verse(widget = None, data = None):
	global no_active_scroll, settings
	if (no_active_scroll == True):
		nmb = obj("list_verse_select").get_active();
		main_view.open('file:///tmp/bible7913.view#' + str(nmb + 1));
		settings["sel_verse"] = nmb;
	update_settings(widget, data);
	
def reload_page(widget = None, data = None): load_books(); load_two_translations();
	
def load_two_translations(widget = None, data = None):
	global settings, dirname;
	active_book = obj("list_books_select").get_active() + 1;
	active_chap = obj("list_chapters_select").get_active() + 1;
	
	result = """<!DOCTYPE html><head><meta content='text/html; charset=UTF-8' http-equiv='Content-Type'/>
		<style>.word{cursor:pointer;color:#000;}.word:hover{color:#0000FF;} body { background: #fff;
		text-decoration: none; overflow-y:scroll; margin: 0 auto; padding: 0; min-width: 480px; max-width: 100%;}
		.vrs{border-bottom: 1px solid #aaaaaa}; </style><script src="file://""" + dirname + """/jquery.min.js"></script></head>
		<script type='text/javascript'> function get_word(word){ document.title = word; }
		
		$(function () {
			var currentHash = "#1"
			$(document).scroll(function () {
				$('.vrs').each(function () {
					var top = window.pageYOffset;
					var distance = top - $(this).offset().top;
					var hash = $(this).attr('id');

					if (distance < 30 && distance > -30 && currentHash != hash) {
						if (hash) {
							document.title = "#" + hash;
							currentHash = hash;
						}
					}
				});
			});
		});
		</script>
		<body><table width='100%' cellpadding="5" cellspacing="5">""";
		
	nmb_l = obj("list_left_select").get_active(); nmb_r = obj("list_right_select").get_active();
	settings["left_select"] = nmb_l; settings["right_select"] = nmb_r;
	
	try:
		for i in range(1, len(modules.module[nmb_l].get_book[active_book][active_chap])):
			verse_l = ""; verse_r = "";
			rtl_l = 'dir="rtl"' if (active_book < 40) and (nmb_l == 0) else 'dir="ltr"';
			rtl_r = 'dir="rtl"' if (active_book < 40) and (nmb_r == 0) else 'dir="ltr"';
			for word in str(delete_html_tags(modules.module[nmb_l].get_book[active_book][active_chap][i])).split("</S>"):
				verse_l += str_verse(word, 'strong') + " ";
			for word in str(delete_html_tags(modules.module[nmb_r].get_book[active_book][active_chap][i])).split("</S>"):
				verse_r += str_verse(word, 'strong') + " ";
			result += '<tr><td id="' + str(i) + '" class="vrs" width="50%" valign="top" ' + rtl_l + \
					  '><b>' + str(i) + "</b>. " + verse_l+'</td><td width="50%" '+ rtl_r + \
					  ' valign="top" class="vrs"><b>' + str(i) + "</b>. " + verse_r + '</td></tr>';
	except KeyError: result += "Error #5423";
		
	result += """</table></body></html>""";
		
	file_view = file_create('/tmp/bible7913.view'); file_view.write(result); file_view.close();
	main_view.open('file:///tmp/bible7913.view');
		
	update_settings(widget, data);
	
def str_verse(word, path = 'none'):
	mapi = word.split("<S>"); result = ''; dd = '"';
	if len(mapi) == 2:
		if path == 'strong':
			result += "<font class='word' onclick=" + dd + "get_word('" + mapi[1].replace(" ", "") + "', " + \
			mapi[1].replace("</S>", "") + ")" + dd + ">" + mapi[0] + "</font>";
		else:
			result += "<font class='word' onclick=" + dd + "get_word('" + mapi[0].replace(" ", "") + "', " + \
			mapi[1].replace("</S>", "") + ")" + dd + ">" + mapi[0] + "</font>";
	else:
		result += "<font class='word' onclick=" + dd + "get_word('" + mapi[0].replace(" ", "") + "', 0)" + \
		dd + ">" + mapi[0] + "</font>";
	return result;
	
def g_p(): return obj("list_left_select").get_active() if obj("get_books_left").get_active() else obj("list_right_select").get_active();
	
def load_books(widget = None, data = None):
	global settings;
	active_book = obj("list_books_select").get_active() if (obj("list_books_select").get_active() != -1) else 0;
	active_chap = obj("list_chapters_select").get_active(); active_vrse = obj("list_verse_select").get_active(); 
		
	nmb = g_p(); obj("list_books_select").get_model().clear();
	for text in modules.module[nmb].list_books.split(","): obj("list_books_select").append_text(text);
	
	obj("list_books_select").set_active(active_book); obj("list_chapters_select").set_active(active_chap);
	obj("list_verse_select").set_active(active_vrse); settings["sel_book"] = active_book; update_settings(widget, data);
	
def load_chapters(widget = None, data = None):
	global settings;
	active_book = obj("list_books_select").get_active() + 1;
	
	nmb = g_p(); obj("list_chapters_select").get_model().clear();
	for i in range(1, len(modules.module[nmb].get_book[active_book])): obj("list_chapters_select").append_text(str(i));
	
	obj("list_chapters_select").set_active(0); settings["sel_chap"] = 0; update_settings(widget, data);
	
def load_verses(widget = None, data = None):
	global settings;
	active_book = obj("list_books_select").get_active() + 1;
	active_chap = obj("list_chapters_select").get_active() + 1;
	
	nmb = g_p(); obj("list_verse_select").get_model().clear();
	for i in range(1, len(modules.module[nmb].get_book[active_book][active_chap])): obj("list_verse_select").append_text(str(i));
	
	obj("list_verse_select").set_active(0); update_settings(widget, data); load_two_translations();
	
def update_settings(widget, data = None):
	global settings;
	if   (widget == obj("list_left_select")):     settings["left_select"]   = obj("list_left_select").get_active();
	elif (widget == obj("list_right_select")):    settings["right_select"]  = obj("list_right_select").get_active();
	elif (widget == obj("list_books_select")):    settings["sel_book"]      = obj("list_books_select").get_active();
	elif (widget == obj("list_chapters_select")): settings["sel_chap"]      = obj("list_chapters_select").get_active();
	elif (widget == obj("list_verse_select")):    settings["sel_verse"]     = obj("list_verse_select").get_active();
	elif (widget == obj("get_books_right")): settings["get_translate"] = "right" if obj("get_books_right").get_active() else "left";
	
def save_settings(file_settings, settings = None):
	file_settings = file_create(file_settings);
	if settings: file_settings.write(str(settings));
	else: file_settings.write("""{'lng': 'uk_UA', 'close_btn': 'left', 'get_translate': 'right', 'left_select': 0, 'right_select': 0}""");
	file_settings.close();
	
def file_ltr(file): return ltr(file_read(file));
	
def file_create(file_path):
	try: os.makedirs(os.path.dirname(file_path));
	except OSError: None;
	try: return open(file_path, "w+");
	except: error_msg("Error: #512 --> I can't create file settings.");
def file_read(file): file = open(file, "r"); result = file.read(); file.close(); return result;

def use_lng():
	global lng;
	try: obj("btn_about").set_tooltip_text(lng["ABOUT"]);
	except KeyError: obj("btn_about").set_tooltip_text(lng_ua["ABOUT"]);
	try: obj("btn_about1").set_tooltip_text(lng["ABOUT"]);
	except KeyError: obj("btn_about1").set_tooltip_text(lng_ua["ABOUT"]);
	try: obj("list_books_select").set_tooltip_text(lng["S_BOOK"]);
	except KeyError: obj("list_books_select").set_tooltip_text(lng_ua["S_BOOK"]);
	try: obj("list_chapters_select").set_tooltip_text(lng["S_CHAP"]);
	except KeyError: obj("list_chapters_select").set_tooltip_text(lng_ua["S_CHAP"]);
	try: obj("list_verse_select").set_tooltip_text(lng["S_VERSE"]);
	except KeyError: obj("list_verse_select").set_tooltip_text(lng_ua["S_VERSE"]);
	try: obj("get_book_label").set_label(lng["LNG_BOOKS"]);
	except KeyError: obj("get_book_label").set_label(lng_ua["LNG_BOOKS"]);
	try: obj("btn_search").set_tooltip_text(lng["SEARCH"]);
	except KeyError: obj("btn_search").set_tooltip_text(lng_ua["SEARCH"]);
	try: obj("menu_settings").set_tooltip_text(lng["SETTINGS"]);
	except KeyError: obj("menu_settings").set_tooltip_text(lng_ua["SETTINGS"]);
	
def about_open(widget = None, data = None):
	search_hide();
	try: obj("dialog_header_bar").set_title(lng["ABOUT"]);
	except KeyError: obj("dialog_header_bar").set_title(lng_ua["ABOUT"]);
	obj("btn_exit_dialog").connect("clicked", about_hide); obj("dialog_header_bar").unparent();
	obj("about").set_titlebar(obj("dialog_header_bar")); obj("about").run();
def about_hide(widget = None, data = None): obj("about").hide();

def delete_html_tags(raw_html): return delete_f_tags(raw_html);
def delete_i_tags(raw_html): return re.sub('<i>.*?</i>', '', raw_html.replace("<pb/>", ""));
def delete_f_tags(raw_html): return re.sub('<f>.*?</f>', '', raw_html.replace("<pb/>", ""));

def maximize(widget = None): obj("main_window").unmaximize() if obj("main_window").props.is_maximized else obj("main_window").maximize();
def minimize(widget = None): obj("main_window").iconify();
def obj(data): return cID.get_object(data);
def quit(widget): global file_settings, settings; save_settings(file_settings, settings); gtk.main_quit();

if __name__ == '__main__': sys.exit(main(sys.argv))
