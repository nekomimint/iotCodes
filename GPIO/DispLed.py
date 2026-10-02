from RPLCD.i2c import CharLCD
display = 0x21
import time

display_lcd = CharLCD(
    i2c_expander="MCP23008",
    address=0x21,
    port=1,
    cols=16,
    rows=2
)
frase = "Texto para testear el test whut, mas longitud para intentar forzar al ciclado"
timer = 0
letter_count = 0
display_lcd.clear()
splits = frase.split(' ')
print(splits)

display_lcd.write_string("Un texto quizas algo largo")