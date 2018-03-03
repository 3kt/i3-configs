#!/usr/bin/env python3
from i3pystatus import Status
from collections import defaultdict
from string import Formatter
from i3pystatus.weather import weathercom
from i3pystatus import IntervalModule

status = Status()

status.register("clock",
    format="%a %-d/%m/%y %r")

status.register("disk",
    path="/data",
    round_size=1,
    format="{used}/{total}G")

status.register("disk",
    path="/",
    round_size=1,
    format="{used}/{total}G")

status.register("mem",
    format="{used_mem}/{total_mem}G",
    color="#FFFFFF",
    divisor=1073741824,
    round_size=3)

status.register("load", format="{avg1}")

status.register("cpu_usage",
    format="{usage}%")

status.register("temp",
    format="{Core_0}°C {Core_1}°C {Core_2}°C {Core_3}°C",
    hints={"markup": "pango"},
    lm_sensors_enabled=True,
    dynamic_color=True)

status.register("network", interface="wlo1", format_up="↓{bytes_recv}KB/s ↑{bytes_sent}KB/s")

status.register("battery")

status.register("pulseaudio")

status.register(
    'weather',
    format='{condition} {current_temp}{temp_unit}',
    colorize=True,
    hints={'markup': 'pango'},
    backend=weathercom.Weathercom(
        location_code='ASXX0117:1:AS',
        units="metric",
    ))

status.register("uptime",
    format="{hours}:{mins}:{secs}")

status.register("shell",
    command="/usr/local/bin/vscoden",
    color="#0FC0FF",
    interval=300)

status.register("shell",
    command="/usr/local/bin/vimn",
    color="#99AAFF",
    interval=300)

status.register("shell",
    command="/usr/local/bin/torn",
    color="#CA30B2",
    interval=300)

status.register("shell",
    command="/usr/local/bin/swayn",
    color="#FF00BB",
    interval=300)

#status.register("shell",
#    command="/usr/local/bin/nixn",
#    interval=300)

#status.register("shell",
#    command="/usr/local/bin/marvinn",
#    interval=300)

# Not really useful now as I've ditched IceCat
#status.register("shell",
#    command="/usr/local/bin/icecatn",
#    interval=300)

# Too many updates for this to be worthwhile
#status.register("shell",
#    command="/usr/local/bin/guixn",
#    interval=300)

status.register("shell",
    command="/usr/local/bin/obss",
    color="#00AF0F",
    interval=300)

status.register("shell",
    command="/usr/local/bin/obsf",
    color="#909C09",
    interval=300)

status.register("shell",
    command="/usr/local/bin/obsd",
    color="#CA3355",
    interval=300)

status.register("shell",
    command="/usr/local/bin/openran",
    color="#FF5F11",
    interval=300)

status.register("shell",
    command="/usr/local/bin/oscn",
    color="#AA5F6A",
    interval=300)

status.register("shell",
    command="/usr/local/bin/jucippn",
    color="#F03000",
    interval=300)

status.register("shell",
    command="/usr/local/bin/atomn",
    color="#FFAA00",
    interval=300)

status.run()
