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

css = b"""
* {
	transition: none;
	border-radius: 0;
}

.back_panel {
	background: #232323;
	border: 1px solid #1A1A1A;
	border-radius: 0;
	padding: 0 0;
}

.panel_btn{
	background: rgba(35, 35, 35, 0.0);
	border: 1px solid rgba(35, 35, 35, 0.0); 
	padding: 8px 11px;
	color: #EEEEEE;
}.panel_btn:hover{
	background: rgba(86, 128, 194, 1.0);
	border: 0; padding: 9px 12px;
	color: #000000;
}.panel_btn:active, .panel_btn:checked{
	background: rgba(86, 128, 194, 0.5);
	border: 1px solid #5680C2;
	box-shadow: none;
	color: #FFFFFF;
}.panel_btn:focus{
	background: rgba(35, 35, 35, 0.5);
	border: 1px dotted #5680C2;
	box-shadow: none;
	color: #EEEEEE;
}.panel_btn:focus:hover{
	background: rgba(86, 128, 194, 1.0);
	padding: 8px 11px;
	color: #000000;
}


""";
