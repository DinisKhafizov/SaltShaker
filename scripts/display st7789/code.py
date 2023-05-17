import microcontroller
import board
# import time
import terminalio
import displayio
import busio
from adafruit_display_text import label
import adafruit_st7789

displayio.release_displays()
tft_cs = board.GP11
tft_dc = board.GP12
tft_res = board.GP13
spi_mosi = board.GP15
spi_clk = board.GP14

width = 240
height = 280

spi = busio.SPI(spi_clk, MOSI=spi_mosi)

display_bus = displayio.FourWire(
    spi, baudrate=48000000, command=tft_dc, chip_select=tft_cs, reset=tft_res
)

display = adafruit_st7789.ST7789(
    display_bus, width=width, height=height, rowstart=19, colstart=0
)

while True:
    # text = "CPU TEMP\n" + str(microcontroller.cpu.temperature)
    with open("myfile.txt") as f:
        line = f.readline()
    text = line
    # text = "poyamn za ruku \n kak deshevka"
    font = terminalio.FONT
    if microcontroller.cpu.temperature < 28:
        color = 0x00FF00
    else:
        color = 0xFFFF00

    if microcontroller.cpu.temperature > 30:
        color = 0xFF0000

    text_area = label.Label(font, text=text, color=color, scale=3)
    text_area.x = int(width/4)
    text_area.y = int(height/2)
    display.show(text_area)
