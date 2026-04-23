# 675.710 Small Satellite Development and Experimentation
# AMSAT Lab 4 Part A
# 2026-04-19

from mpu6050 import mpu6050
import time

i2c_address = 0x68

def loop():
    mpu = mpu6050(i2c_address)
    while True:
        print("Temp: "+str(mpu.get_temp()))
        print()
        
        accel_data = mpu.get_accel_data()
        print("Acc X: "+str(accel_data['x']))
        print("Acc Y: "+str(accel_data['y']))
        print("Acc Z: "+str(accel_data['z']))
        print()
        
        gyro_data = mpu.get_gyro_data()
        print("Gyro X: "+str(gyro_data['x']))
        print("Gyro Y: "+str(gyro_data['y']))
        print("Gyro Z: "+str(gyro_data['z']))
        print()
        print("-----------------------------")
        time.sleep(1)
    
if __name__ == "__main__":
    loop()