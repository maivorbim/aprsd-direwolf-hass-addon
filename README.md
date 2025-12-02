APRSd + Direwolf — Home Assistant Add-on

A combined APRS-IS client (APRSd) and AX.25/KISS modem (Direwolf) packaged as a Home Assistant add-on.
Supports radio TNCs, soundcard modems, MQTT integration, and Home Assistant Ingress.

Features

Runs Direwolf and APRSd in one supervised add-on

Supports serial TNCs (/dev/ttyUSB*) and soundcard /dev/snd devices

Optional MQTT bridging:

aprs/raw

aprs/position/<callsign>

aprs/message/<callsign>

Home Assistant Ingress web dashboard

Multi-arch Docker images via GitHub Actions

Uses /data for persistent configuration
