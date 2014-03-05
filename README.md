VKeyboard
=========

Virtual Keyboard for Adafruit PiTFT

 (C) Copyright 2007 Anthony Maro<br>
 (C) Copyright 2014 William B Phelps

   Version 2.1 - February 2014 - for PiTFT 320x240 touchscreen

   Now has 2 line input area (code specific for 2 lines, not generalized)

   This program is free software; you can redistribute it and/or
   modify it under the terms of the GNU General Public License as
   published by the Free Software Foundation; either version 3 of the
   License, or (at your option) any later version.

   This program is distributed in the hope that it will be useful, but
   WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
   General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
   02111-1307, USA.

   Usage:

   from virtualKeyboard import VirtualKeyboard

   default_text = 'Hello world'
   vkeybd = VirtualKeyboard(screen)         <<< Changed in version 2.1 !
   userinput = vkeybd.run(default_text)     <<< Changed in version 2.1 !

