#!/bin/bash
set -e

if [ ! -f /data/aprsd.yml ]; then
    echo "Missing /data/aprsd.yml"
    sleep infinity
fi

if [ ! -f /data/direwolf.conf ]; then
    echo "Missing /data/direwolf.conf"
    sleep infinity
fi

/start-direwolf.sh &

sleep 3

/start-aprsd.sh &

python3 /mqtt_bridge.py &

wait -n
