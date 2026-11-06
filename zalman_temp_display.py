#!/usr/bin/env python3
import hid, asyncio, sys, os

ZALMAN_VID = 0x1C57
ZALMAN_PID = 0x3ED1

# Time between USB reports sent to the display
# ---
# Interpolation between values is done on the device,
# so changing this delay affects the responsiveness of
# the displayed number
UPDATE_DELAY = 0.2

temperature = 0

async def writeUsb():
    while True:
        device = hid.device()
        try:
            device.open(ZALMAN_VID, ZALMAN_PID)
        except Exception as e:
            print(f"Failed to open the device: {e}")
            sys.exit(1)
        data = bytearray(64)
        data[0] = 2  # Report ID (?)
        while True:
            data[1] = temperature  # CPU Dynamic Info 1 - Temperature
            try:
                device.write(data)
            except Exception as e:
                print(f"Lost communication with the device: {e}")
                device.close() # Should not raise exceptions
                sys.exit(1)
            await asyncio.sleep(UPDATE_DELAY)

async def readInput():
    global temperature
    while True:
        try:
            temperature_str = (await asyncio.to_thread(sys.stdin.readline)).strip()
        except asyncio.CancelledError:
            os._exit(1) # Force thread to terminate
        # EOF condition check, sleep so that we don't consume CPU cycles
        if not temperature_str:
            await asyncio.sleep(0.5)
            continue
        try:
            temperature = int(temperature_str) & 0xFF
        except ValueError:
            pass

async def main():
    await asyncio.gather(writeUsb(), readInput(), return_exceptions=True)

asyncio.run(main())
