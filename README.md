
[89.pdf](https://github.com/mujifongfone/IXD-256-Muji/files/12900671/89.pdf)



![IMG_8765](https://github.com/mujifongfone/IXD-256-Muji/assets/146476309/6db67c2b-87b8-4ebf-90d1-ff9d751be3df)
![IMG_8764](https://github.com/mujifongfone/IXD-256-Muji/assets/146476309/4511a239-3c90-4d40-ab2b-84b157d2ea17)

import os, sys, io
import M5
from M5 import *
from hardware import *
import time


pin1 = None
looprun = None


def setup():
  global pin1, looprun

  M5.begin()
  pin1 = Pin(1, mode=Pin.OUT)
  looprun = 0



def loop():
  global pin1,looprun
  
  M5.update()
  if looprun <= 5 :
    pin1.on()
    time.sleep(1)
    pin1.off()
    time.sleep(1)
    looprun +=1
    print(looprun)


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
