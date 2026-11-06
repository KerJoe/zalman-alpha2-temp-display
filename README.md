# Zalman Alpha2 A24/A36 Linux Temperature Display Driver

![Alpha2 White](alpha2wh.png)

Userspace Python USB HID Linux Driver and Systemd services for Zalman Alpha2 A24/A36 liquid coolers.

# Requirements

- Python 3.9+
- `python-hidapi` system package

Debian: `apt install python3 python-hidapi lm-sensors`

Arch: `pacman -S python python-hidapi lm_sensors`

# Usage

To do a quick test, run:
```
$ ./run.sh
```

To add the driver as a startup Systemd service, run:
```
# cp zalman_temp_display.py /usr/local/bin/zalman_temp_display
# cp zalman_temp_display.service zalman_temp_display.socket zalman_temp_display_writer.service /etc/systemd/system/
# systemctl daemon-reload
# systemctl enable --now zalman_temp_display.socket zalman_temp_display_writer.service
```

# Modifying displayed value

By default the `Tctl` value (used by AMD CPUs), which is reported by lm_sensors, is displayed.
You can replace it with another (e.g. `Tccd1`, `temp1`, `Package id 0`, etc.), by modifying `grep` capture in `run.sh` or `zalman_temp_display_writer.service`.

# License

The software is released under the GNU General Public License (GPL) which can be found in the file LICENSE.txt in the same directory as this file.
