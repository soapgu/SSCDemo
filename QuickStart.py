import pyssc as ssc

found_setup = ssc.scan()
print(len(found_setup.ssc_devices))

for device in found_setup.ssc_devices:
    print(device)
    print(device.ip)
