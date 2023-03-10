import machine
import utime


def main():
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    i = 0
    temperature = 0
    print('Loading....')
    while i < 17:
        if(i%4==0):
            print('(', i, ')','analyzing..')
        temperature += round(27 - (sensor_temp.read_u16() * conversion_factor - 0.706)/0.0017212,2)
        utime.sleep(0.4)
        i = i+1
    print('Current Temperature :', temperature/10)

main()
