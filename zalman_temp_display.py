#!/usr/bin/env python
import hid, asyncio, sys

ZALMAN_VID = 0x1C57
ZALMAN_PID = 0x3ED1

# Time between USB reports sent to the display
# ---
# Interpolation between values is done on the device,
# so changing this delay affects the responsivness of
# the displayed number
UPDATE_DELAY = 0.2

temperature = 0

async def writeUsb():
    device = hid.device()
    device.open(ZALMAN_VID, ZALMAN_PID)

    while True:
        data = bytearray([0] * 64)
        data[0] = 2           # Report ID (?)
        data[1] = temperature # CPU Dynamic Info 1 - Temperature
        device.write(data)
        await asyncio.sleep(UPDATE_DELAY)


async def readInput():
    global temperature
    while True:
        temperature_str = (await asyncio.to_thread(sys.stdin.readline)).strip()
        try:
            temperature = int(temperature_str) & 0xFF
        except:
            pass

async def main():
    await asyncio.gather(writeUsb(), readInput())

asyncio.run(main())
