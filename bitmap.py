import uos
import machine
import st7789
import time
from fonts import vga2_8x8 as font1
from fonts import vga1_16x32 as font2




#SPI(1) default pins
spi1_sck=10
spi1_mosi=11
spi1_miso=8     #not use
st7789_res = 12
st7789_dc  = 13
disp_width = 240
disp_height = 240
CENTER_Y = int(disp_width/2)
CENTER_X = int(disp_height/2)

print(uos.uname())
spi1 = machine.SPI(1, baudrate=40000000, polarity=1)
print(spi1)
st7789_display = st7789.ST7789(spi1, disp_width, disp_width,
                          reset=machine.Pin(st7789_res, machine.Pin.OUT),
                          dc=machine.Pin(st7789_dc, machine.Pin.OUT),
                          xstart=0, ystart=0, rotation=0)

def display_bitmap(file_name, display):
    """读取位图并显示在ST7789上"""
    with open(file_name, 'rb') as bmp:
        # 验证位图文件头
        if bmp.read(2) != b'BM':
            raise ValueError("Not a valid BMP file")
        bmp.seek(10)
        start_pos = int.from_bytes(bmp.read(4), 'little')  # 图像数据起始地址
        bmp.seek(18)
        width = int.from_bytes(bmp.read(4), 'little')
        height = int.from_bytes(bmp.read(4), 'little')
        
        if width != 240 or height != 120:
            raise ValueError("Image size must be 240x240")

        bmp.seek(start_pos)
        for y in range(height):
            for x in range(width):
                # 读取每个像素（BGR格式）
                b = bmp.read(1)
                g = bmp.read(1)
                r = bmp.read(1)
                # 将RGB值写入显示器
                display.pixel(x, height - y - 1, st7789.color565(int.from_bytes(r, 'little'),
                                                                 int.from_bytes(g, 'little'),
                                                                 int.from_bytes(b, 'little')))


def read_cpu_temperature():
    # 讀取內建溫度感應器
    sensor_temp = machine.ADC(4)
    voltage = sensor_temp.read_u16() * (3.3 / 65535)  # 計算電壓
    temperature = 27 - (voltage - 0.706) / 0.001721   # 根據公式計算溫度
    return temperature


# 调用函数显示图像
display_bitmap("tello_120.bmp", st7789_display)
st7789_display.text(font2, "Hello! Tello", 10, 130)


while True:
    # 獲取 CPU 溫度
    temp = read_cpu_temperature()
    st7789_display.text(font1,'CPU Temperature:', 10, 165)
    st7789_display.text(font1,f'{temp:.2f} °C', 10, 175, st7789.RED)
    
    # 每隔一段時間更新
    time.sleep(2)
    
    

