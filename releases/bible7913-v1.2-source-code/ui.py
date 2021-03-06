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

gtk3 = """<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.20.0 -->
<interface>
  <requires lib="gtk+" version="3.12"/>
  <object class="GtkHeaderBar" id="dialog_header_bar">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <child>
      <object class="GtkButton" id="btn_exit_dialog">
        <property name="label" translatable="yes">X</property>
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <style>
          <class name="panel_btn"/>
        </style>
      </object>
    </child>
    <style>
      <class name="back_panel"/>
    </style>
  </object>
  <object class="GtkImage" id="image_search">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="stock">gtk-find</property>
  </object>
  <object class="GtkHeaderBar" id="main_header_bar_left">
    <property name="height_request">20</property>
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="spacing">1</property>
    <child>
      <object class="GtkButton" id="btn_exit">
        <property name="label" translatable="yes">X</property>
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <style>
          <class name="panel_btn"/>
        </style>
      </object>
    </child>
    <child>
      <object class="GtkButton" id="btn_maximize">
        <property name="label" translatable="yes">◻</property>
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <style>
          <class name="panel_btn"/>
        </style>
      </object>
      <packing>
        <property name="position">1</property>
      </packing>
    </child>
    <child>
      <object class="GtkButton" id="btn_minimize">
        <property name="label" translatable="yes">_</property>
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <style>
          <class name="panel_btn"/>
        </style>
      </object>
      <packing>
        <property name="position">2</property>
      </packing>
    </child>
    <child type="title">
      <object class="GtkLabel">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="label" translatable="yes">Bible7913</property>
        <attributes>
          <attribute name="foreground" value="#ffffffffffff"/>
        </attributes>
      </object>
    </child>
    <child>
      <object class="GtkButton" id="btn_about">
        <property name="label" translatable="yes">?</property>
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <style>
          <class name="panel_btn"/>
        </style>
      </object>
      <packing>
        <property name="pack_type">end</property>
        <property name="position">3</property>
      </packing>
    </child>
    <style>
      <class name="back_panel"/>
    </style>
  </object>
  <object class="GtkHeaderBar" id="main_header_bar_right">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="spacing">1</property>
    <child>
      <object class="GtkButton" id="btn_about1">
        <property name="label" translatable="yes">?</property>
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <style>
          <class name="panel_btn"/>
        </style>
      </object>
      <packing>
        <property name="position">3</property>
      </packing>
    </child>
    <child type="title">
      <object class="GtkLabel">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="label" translatable="yes">Bible7913</property>
        <attributes>
          <attribute name="foreground" value="#ffffffffffff"/>
        </attributes>
      </object>
    </child>
    <child>
      <object class="GtkButton" id="btn_exit1">
        <property name="label" translatable="yes">X</property>
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <style>
          <class name="panel_btn"/>
        </style>
      </object>
      <packing>
        <property name="pack_type">end</property>
        <property name="position">1</property>
      </packing>
    </child>
    <child>
      <object class="GtkButton" id="btn_maximize1">
        <property name="label" translatable="yes">◻</property>
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <style>
          <class name="panel_btn"/>
        </style>
      </object>
      <packing>
        <property name="pack_type">end</property>
        <property name="position">2</property>
      </packing>
    </child>
    <child>
      <object class="GtkButton" id="btn_minimize1">
        <property name="label" translatable="yes">_</property>
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <style>
          <class name="panel_btn"/>
        </style>
      </object>
      <packing>
        <property name="pack_type">end</property>
        <property name="position">1</property>
      </packing>
    </child>
    <style>
      <class name="back_panel"/>
    </style>
  </object>
  <object class="GtkMenu" id="menu_book">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <child>
      <object class="GtkMenuItem" id="lng_menu_label">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="label" translatable="yes">lng</property>
        <property name="use_underline">True</property>
      </object>
    </child>
    <child>
      <object class="GtkMenuItem" id="get_book_label">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="label" translatable="yes">book_lng</property>
        <property name="use_underline">True</property>
        <child type="submenu">
          <object class="GtkMenu">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <child>
              <object class="GtkRadioMenuItem" id="get_books_left">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">left</property>
                <property name="use_underline">True</property>
                <property name="draw_as_radio">True</property>
              </object>
            </child>
            <child>
              <object class="GtkRadioMenuItem" id="get_books_right">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">right</property>
                <property name="use_underline">True</property>
                <property name="draw_as_radio">True</property>
                <property name="group">get_books_left</property>
              </object>
            </child>
          </object>
        </child>
      </object>
    </child>
  </object>
  <object class="GtkWindow" id="main_window">
    <property name="width_request">600</property>
    <property name="height_request">400</property>
    <property name="can_focus">False</property>
    <property name="window_position">center</property>
    <child>
      <object class="GtkBox">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="orientation">vertical</property>
        <child>
          <object class="GtkBox">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <child>
              <object class="GtkComboBoxText" id="list_books_select">
                <property name="width_request">250</property>
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <style>
                  <class name="panel_combobox"/>
                </style>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkComboBoxText" id="list_chapters_select">
                <property name="width_request">70</property>
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <style>
                  <class name="panel_combobox"/>
                </style>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkComboBoxText" id="list_verse_select">
                <property name="width_request">70</property>
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <style>
                  <class name="panel_combobox"/>
                </style>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">2</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">3</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="btn_search">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="image">image_search</property>
                <accelerator key="f" signal="clicked" modifiers="GDK_CONTROL_MASK"/>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">4</property>
              </packing>
            </child>
            <child>
              <object class="GtkMenuButton" id="menu_settings">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="popup">menu_book</property>
                <child>
                  <object class="GtkImage">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="stock">gtk-preferences</property>
                  </object>
                </child>
                <style>
                  <class name="menubar_btn"/>
                </style>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">5</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkPaned">
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <child>
              <object class="GtkBox">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="orientation">vertical</property>
                <child>
                  <object class="GtkBox">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkComboBoxText" id="list_left_select">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="popup_fixed_width">False</property>
                        <style>
                          <class name="panel_combobox"/>
                        </style>
                      </object>
                      <packing>
                        <property name="expand">True</property>
                        <property name="fill">True</property>
                        <property name="position">0</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkComboBoxText" id="list_right_select">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="popup_fixed_width">False</property>
                        <style>
                          <class name="combobox"/>
                        </style>
                      </object>
                      <packing>
                        <property name="expand">True</property>
                        <property name="fill">True</property>
                        <property name="position">1</property>
                      </packing>
                    </child>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkScrolledWindow" id="books_viewer">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="shadow_type">in</property>
                    <child>
                      <placeholder/>
                    </child>
                  </object>
                  <packing>
                    <property name="expand">True</property>
                    <property name="fill">True</property>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="resize">True</property>
                <property name="shrink">True</property>
              </packing>
            </child>
            <child>
              <object class="GtkPaned">
                <property name="width_request">250</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="orientation">vertical</property>
                <child>
                  <object class="GtkBox">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="orientation">vertical</property>
                    <child>
                      <object class="GtkComboBoxText" id="list_dict_select">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                      </object>
                      <packing>
                        <property name="expand">False</property>
                        <property name="fill">True</property>
                        <property name="position">0</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkEntry" id="search_dict">
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="secondary_icon_stock">gtk-find</property>
                      </object>
                      <packing>
                        <property name="expand">False</property>
                        <property name="fill">True</property>
                        <property name="position">1</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkScrolledWindow" id="dict_box">
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="shadow_type">in</property>
                        <child>
                          <placeholder/>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">True</property>
                        <property name="fill">True</property>
                        <property name="position">2</property>
                      </packing>
                    </child>
                  </object>
                  <packing>
                    <property name="resize">True</property>
                    <property name="shrink">True</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkBox">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="orientation">vertical</property>
                    <child>
                      <placeholder/>
                    </child>
                    <child>
                      <placeholder/>
                    </child>
                    <child>
                      <placeholder/>
                    </child>
                  </object>
                  <packing>
                    <property name="resize">False</property>
                    <property name="shrink">True</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="resize">False</property>
                <property name="shrink">True</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">True</property>
            <property name="fill">True</property>
            <property name="position">1</property>
          </packing>
        </child>
        <child>
          <object class="GtkStatusbar">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="margin_left">10</property>
            <property name="margin_right">10</property>
            <property name="margin_start">10</property>
            <property name="margin_end">10</property>
            <property name="margin_top">6</property>
            <property name="margin_bottom">6</property>
            <property name="orientation">vertical</property>
            <property name="spacing">2</property>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">3</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
  <object class="GtkAboutDialog" id="about">
    <property name="can_focus">False</property>
    <property name="resizable">False</property>
    <property name="window_position">center</property>
    <property name="destroy_with_parent">True</property>
    <property name="type_hint">dialog</property>
    <property name="transient_for">main_window</property>
    <property name="attached_to">main_window</property>
    <property name="program_name">Bible7913</property>
    <property name="version">Версія 0.10</property>
    <property name="copyright" translatable="yes">© Mish7913. All Rights Reserved.</property>
    <property name="website">https://mish7913.blogspot.com/p/home.html</property>
    <property name="website_label" translatable="yes">Web-site</property>
    <property name="authors">Mish7913</property>
    <property name="logo">icon.svg</property>
    <property name="license_type">gpl-3-0</property>
    <child internal-child="vbox">
      <object class="GtkBox">
        <property name="can_focus">False</property>
        <property name="orientation">vertical</property>
        <property name="spacing">2</property>
        <child internal-child="action_area">
          <object class="GtkButtonBox">
            <property name="can_focus">False</property>
            <property name="layout_style">end</property>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">False</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkSeparator">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">2</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
  <object class="GtkWindow" id="search_window">
    <property name="width_request">600</property>
    <property name="height_request">350</property>
    <property name="can_focus">False</property>
    <property name="window_position">center</property>
    <property name="default_width">750</property>
    <property name="default_height">400</property>
    <child>
      <object class="GtkPaned">
        <property name="width_request">600</property>
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <child>
          <object class="GtkBox">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="orientation">vertical</property>
            <child>
              <object class="GtkEntry" id="search_entry">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="has_focus">True</property>
                <property name="is_focus">True</property>
                <property name="can_default">True</property>
                <property name="has_default">True</property>
                <property name="margin_left">5</property>
                <property name="margin_right">5</property>
                <property name="margin_top">5</property>
                <property name="margin_bottom">5</property>
                <property name="secondary_icon_stock">gtk-find</property>
                <property name="placeholder_text" translatable="yes">Пошук</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkComboBoxText" id="search_list_books">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="margin_left">5</property>
                <property name="margin_right">5</property>
                <property name="margin_top">5</property>
                <property name="margin_bottom">5</property>
                <property name="has_entry">True</property>
                <child internal-child="entry">
                  <object class="GtkEntry">
                    <property name="can_focus">False</property>
                  </object>
                </child>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="margin_left">5</property>
                <property name="margin_right">5</property>
                <property name="label" translatable="yes">*а - зірочка на початку слова означає що кожне слово повинно починатись з (а).

а* - зірочка у кінці слова означає що кожне слово повинно закінчуватись на "а".
</property>
                <property name="wrap">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="pack_type">end</property>
                <property name="position">2</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="resize">False</property>
            <property name="shrink">True</property>
          </packing>
        </child>
        <child>
          <object class="GtkBox">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="margin_right">5</property>
            <property name="margin_bottom">5</property>
            <property name="orientation">vertical</property>
            <child>
              <object class="GtkLabel">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="halign">start</property>
                <property name="margin_left">5</property>
                <property name="margin_right">5</property>
                <property name="margin_top">5</property>
                <property name="margin_bottom">5</property>
                <property name="label" translatable="yes">Результати пошуку: </property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkScrolledWindow" id="search_container">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="shadow_type">in</property>
                <child>
                  <placeholder/>
                </child>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="resize">True</property>
            <property name="shrink">True</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>""";
