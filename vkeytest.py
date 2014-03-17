#!/usr/bin/python

from datetime import datetime, timedelta
import sys, signal
import pygame
from virtualKeyboard import VirtualKeyboard
from time import sleep

import os
# Init framebuffer/touchscreen environment variables

# for Adafruit PiTFT:
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV'      , '/dev/fb1')
os.putenv('SDL_MOUSEDRV'   , 'TSLIB')
os.putenv('SDL_MOUSEDEV'   , '/dev/input/touchscreen')

# for other TFT 
#os.putenv('FRAMEBUFFER', '/dev/fb1') # wbp
#os.putenv('SDL_VIDEODRIVER', 'fbcon')
#os.putenv('SDL_FBDEV'      , '/dev/fb1')
#os.putenv('SDL_MOUSEDEV'   , '/dev/input/event0')

# for X11 
#os.putenv('DISPLAY'   , '192.168.1.100:0.0')

# Init pygame and screen
pygame.display.init()
pygame.font.init()
pygame.mouse.set_visible(False)

size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
print "Framebuffer size: %d x %d" % (size[0], size[1])
#screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

#size = (320,240) # temp
size = (480,320) # temp
screen = pygame.display.set_mode(size)

image = pygame.Surface.convert(pygame.image.load('ISS_Close_up_3bwr.jpg'))
bg  = pygame.transform.scale(image, size)

bgRect = bg.get_rect()
txtColor = (255,255,0)
txtFont = pygame.font.SysFont("Arial", 30, bold=True)
txt = txtFont.render('Virtual Keyboard' , 1, txtColor)
bg.blit(txt, (15, 35))
txt = txtFont.render('by' , 1, txtColor)
bg.blit(txt, (15, 70))
txt = txtFont.render('William Phelps' , 1, txtColor)
bg.blit(txt, (15, 105))
screen.blit(bg, bgRect)
pygame.display.update()
sleep(2)

#  ----------------------------------------------------------------

def Exit():
    print 'Exit'
#    StopAll()
    sys.exit(0)

def signal_handler(signal, frame):
    print 'SIGNAL {}'.format(signal)
    Exit()

def pageDateTime():
  global page
  print 'DateTime'
  while page == pageDateTime:
#    if checkEvent(): return
    vkey = VirtualKeyboard(screen) # create a virtual keyboard
    if gps_on and gps.statusOK:
      tn = gps.datetime + timedelta(seconds=5) # set ahead a bit
    else:
      tn = datetime.now() + timedelta(seconds=5) # set ahead a bit
    txt = vkey.run(tn.strftime('%Y-%m-%d %H:%M:%S'))
    print 'datetime: {}'.format(txt)
    if len(txt)>0:
      try:
          dt = datetime.strptime(txt, '%Y-%m-%d %H:%M:%S') # check format
          print 'dt: {}'.format(dt)
          os.system('sudo date -s "{}"'.format(dt))
      except:
          pass
    else:
      Exit()

#    page = pageMenu
    return

#  ----------------------------------------------------------------
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGHUP, signal_handler)
signal.signal(signal.SIGQUIT, signal_handler)

page = pageDateTime
gps_on = False

while(True):

  try:
    page()

  except SystemExit:
#    print 'SystemExit'
    sys.exit(0)
  except:
    print '"Except:', sys.exc_info()[0]
#    print traceback.format_exc()
#    StopAll()
    raise

