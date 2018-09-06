/** Copyright 2017 Mish7913 <Mish7913@gmail.com> **/

/*
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 *
 *
 */

#include <iostream>
#include <stdlib.h>
#include <str.h>

std::string tmp_str;
std::map <int, std::string> tmp_map;

int main(int argc, char **argv){
    tmp_str = std::string(argv[0]); tmp_map = str::split_to_map(tmp_str, "/"); tmp_str = "python " + tmp_map[0];
    for(int i = 1;  i < int(tmp_map.size()) - 1; i++){ tmp_str += "/" + tmp_map[i]; }
    tmp_str += "/zp_db.pyc"; system(tmp_str.c_str());
    return 0;
}

