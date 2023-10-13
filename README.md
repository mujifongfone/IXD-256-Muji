
![intro](https://github.com/mujifongfone/IXD-256-Muji/assets/146476309/0c9eb6fb-66f5-4781-a6bd-be4458b978ba)

![IMG_8762](https://github.com/mujifongfone/IXD-256-Muji/assets/146476309/1a272bdc-402d-400a-9249-bcbe40a847de)
![IMG_8765](https://github.com/mujifongfone/IXD-256-Muji/assets/146476309/6db67c2b-87b8-4ebf-90d1-ff9d751be3df)
![IMG_8764](https://github.com/mujifongfone/IXD-256-Muji/assets/146476309/4511a239-3c90-4d40-ab2b-84b157d2ea17)

import os, sys, io
import M5
from M5 import *
from hardware import *
import time


pin1 = None
rgb = None


def setup():
  global pin1, rgb

  M5.begin()
  pin1 = Pin(1, mode=Pin.OUT)
  # default rbg setting
  rbg=RGB()
  #custom setting using pin G35
  rgb = RGB(io=2, n=10, type="SK6812")


def loop():
  global pin1, rgb, rgb_color
  M5.update()
  # fade in RGB green
  for i in range(100):
      rgb.fill_color(get_color(0,i,0))
      time.sleep_ms(20)
  # cgase RGB blue light
  for i in range(10):
    rgb.set_color(i, 0x0000ff)
    time.sleep_ms(100)
  rgb.fill_color(0xff0129)
  time.sleep_ms(1000)
  
def get_color(r,g,b):
  rgb_color = (r << 16) | (g << 8) | b
  return rgb_color

print(get_color(255,0,0))
print('color ='), hex(get_color(255,0,0))

if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
