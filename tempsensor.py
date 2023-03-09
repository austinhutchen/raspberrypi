import machine
import utime



sensor_temp = machine.ADC(4)
conversion_factor= 3.3/ (65535)
i=0
temperature=0
while i<10:
    print('(',i+1,')','assessing data from your environment....')
    temperature += round(27 -(sensor_temp.read_u16() * conversion_factor - 0.706)/0.0017212)
    utime.sleep(0.4)
    i=i+1
    
print('Current Temperature :' ,temperature/10)