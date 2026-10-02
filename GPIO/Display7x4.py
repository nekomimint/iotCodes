import time 
import board
import smbus2 as bus
from adafruit_ht16k33.segments import BigSeg7x4
i2c = board.I2C()
a = 0
CHARS = [
    {"seg_up": 0x01},
    {"seg_up_left": 0x02},
    {"seg_down_left": 0x04},
    {"seg_down": 0x08},
    {"seg_up": 0x01},
    {"seg_up": 0x01}
]
#def put_raw_digit(disp,index_number: int, char: String):
#    disp.set_digit_raw()
letras = ['P','e','r','l','a',' ','s','e',' ', 'l', 'a', ' ','v','a',' ','a',' ','r','i','f','a','r']
frase = "Sofia grita mucho alvaberja"
disp = BigSeg7x4(i2c, 0x70, auto_write=False)
def main():
        while True:
            global a
            if(a == len(letras)):
                a = 0
                disp._push(' ')
            time.sleep(0.5)
            
            disp._push(frase[a])
            a= a+1
            disp.show()
main()


