import gpiozero

buzzer_button = gpiozero.Button(12)


def main():
    while(True):
        if(buzzer_button.is_active):
            print("Reputo")

main()