import js as p5
from js import document

data_string = None
data_list = None
sensor_val = None
button_val = None
button_state = 0

# load font data and assign it to variable:
jellee_font = p5.loadFont('Jellee.otf') 

swirl_img = p5.loadImage('swirl.png')
icecream_1 = p5.loadImage('images/icecream_1.png')
icecream_2 = p5.loadImage('images/icecream_2.png')
icecream_3 = p5.loadImage('images/icecream_3.png')
topping_1 = p5.loadImage('images/topping_1.png')
topping_2 = p5.loadImage('images/topping_2.png')
topping_3 = p5.loadImage('images/topping_3.png')

# load font:
# font = p5.loadFont('fontfile.ttf')

icecream_selected = 0
icecream_flavors = ['Omelette', 'Pig Blood', 'Blue Cheese']
icecream_toppings = ['Rotten Egg', 'Dead Fish', 'Poopoo']

select_mode = 'icecream'

icecream_number = 0
topping_number = 0

def setup():
  p5.createCanvas(400, 400)
  # change mode to draw rectangles from center:
  p5.rectMode(p5.CENTER)
  # change mode to draw images from center:
  p5.imageMode(p5.CENTER)
  # change stroke cap to square:
  p5.strokeCap(p5.SQUARE)
  # change font to Courier:
  p5.textFont('Courier', 14)
  # change to font from font file:
  #p5.textFont(font)


def draw():
  p5.background(255)
  global data_string, data_list
  global sensor_val, button_val
  global icecream_selected
  global select_mode
  global icecream_number
  global topping_number
  global button_state

  # assign content of "data" div on index.html page to variable:
  data_string = document.getElementById("data").innerText
  # split data_string by comma, making a list:
  data_list = data_string.split(',')

  # assign 1st item of data_list to sensor_val:
  sensor_val = int(data_list[0])
  # assign 2nd item of data_list to sensor_val:
  button_val = int(data_list[1])

# print "digital ice cream maker"
  p5.textFont(jellee_font, 28)
  # print ice cream number
  p5.fill(65,105,225)
  p5.text('Digital Ice Cream Maker', 10, 40)

  ##CHOOSE FLAVOR
  if(select_mode == 'icecream'):
    # map sensor_val (0 - 255) to icecream_number (0 - 2)
    icecream_number = int(p5.map(sensor_val, 0, 255, 0, 2))
    # print "Choose Ice Cream Flavor and Topping"
    p5.textFont(jellee_font, 18)
    # print ice cream number
    p5.fill(0)
    p5.text('Select Ice Cream Flavor', 10, 350)
    # print "flavor/ topping being selected"
    p5.textFont('Courier', 16)
    p5.fill(0)  # black fill
    p5.text('Icecream Flavor:' + ' ' + '<' + ' ' + icecream_flavors[icecream_number] + ' ' + '>', 10, 370)
  ##CHOOSE TOPPING
    # map sensor_val (0 - 255) to topping_number (0 - 2)
  elif(select_mode == 'topping'):
    topping_number = int(p5.map(sensor_val, 0, 255, 0, 2))
    # print "Choose Ice Cream Flavor and Topping"
    p5.textFont(jellee_font, 18)
    # print ice cream number
    p5.fill(0)
    p5.text('Select Ice Cream Flavor', 10, 350)
    # print "flavor/ topping being selected"
    p5.textFont('Courier', 16)
    p5.fill(0)  # black fill
    p5.text('Icecream Flavor:' + ' ' + '<' + ' ' + icecream_toppings[topping_number] + ' ' + '>', 10, 370)

  elif(select_mode == 'final'):
    p5.textFont(jellee_font, 28)
    # print final text
    p5.fill(0)
    p5.text('Ice Cream Made :) Enjoy!', 10, 340)

  
  
  
  
#when its cold or not too cold
#in the summer i did  a lot but havent done in a while
#why do u think i hike

  # draw rectangle
  p5.rect(0, 200, 10, 800)
  p5.rect(400, 0, 10, 800)
  p5.rect(0, 400, 800, 10)
  p5.rect(400, 0, 800, 10)

# select ice cream flavor
  if(icecream_number == 0):
    p5.image(icecream_1, 200, 200)
  elif(icecream_number == 1):
    p5.image(icecream_2, 200, 200)
  elif(icecream_number == 2):
    p5.image(icecream_3, 200, 200)

# select topping flavor
  if(topping_number == 0):
    p5.image(topping_1, 220, 140)
  elif(topping_number == 1):
    p5.image(topping_2, 220, 140)
  elif(topping_number == 2):
    p5.image(topping_3, 220, 140)
  

  # when button is pressed, select icecream
  if(button_val == 1) and (button_state == 0):
    if(select_mode == 'icecream'):
        select_mode = 'topping'
    elif(select_mode == 'topping'):
        select_mode = 'final'
    button_state = 1
  elif(button_val == 0):
    button_state = 0

  
  

  '''
  # draw circle changing size with sensor data:
  # ellipse function takes (x, y, width, height)
  p5.ellipse(75, 75, sensor_val, sensor_val)
  
  # draw square changing color with sensor data:
  # fill function can take (red, green, blue)
  p5.fill(sensor_val, 0, 255 - sensor_val)  
  # rectangle function takes (x, y, width, height)
  p5.rect(225, 75, 100, 100)

  # draw lines responding to button data:
  if(button_val == 0):
    for i in range(8):
      p5.strokeWeight(i+1)
      p5.stroke(0)
      # line function takes (x1, y1, x2, y2)
      x1 = x2 = 25 + i*12
      y1 = 175
      y2 = 275
      p5.line(x1, y1, x2, y2)

  # draw image rotating with sensor data:
  p5.push()  # save transformation coordinates
  p5.translate(225, 225)  # move coordinates by (x, y)
  # use sensor_val as degrees converted to radians:
  angle = p5.radians(sensor_val)  
  p5.rotate(angle)  # rotate coordinates
  # image function takes (image, x, y, width, height)
  p5.image(swirl_img, 0, 0, 100, 100)
  p5.pop()  # restore transformation coordinates
  '''