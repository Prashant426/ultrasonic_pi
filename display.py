from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, textsize
from luma.core.legacy.font import proportional, LCD_FONT, CP437_FONT
from luma.led_matrix.device import max7219
import time
from PIL import ImageFont

def demo(x, height=16, width=24, block_orientation=-90):

    new_font = ImageFont.truetype("pixelmix_micro.ttf", 8)
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=width, height=height, block_orientation=block_orientation)
    
   
    with canvas(device) as draw:

        draw.rectangle(device.bounding_box, outline="white")
        text(draw, (1,1), "Dist", fill="white", font=proportional(LCD_FONT))
        text(draw, (8,1),str(x) , fill="white", font = propertional(CP437_FONT))
      # text(draw,(0,0), x, font=  new_font)
      # text(draw, (2, 10), "World", fill="white", font=proportional(LCD_FONT))
