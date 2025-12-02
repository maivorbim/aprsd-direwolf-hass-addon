FROM python:3.11-slim

ENV LANG=C.UTF-8

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential git alsa-utils libasound2-dev cmake && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /opt

# Install Direwolf
RUN git clone https://github.com/wb2osz/direwolf.git && \
    cd direwolf && \
    git checkout 1.7 && \
    mkdir build && cd build && \
    cmake .. && \
    make && make install && make install-conf

# Install APRSd
RUN pip install --no-cache-dir aprsd==3.0.0

WORKDIR /data
VOLUME ["/data"]

COPY run.sh /run.sh
COPY start-aprsd.sh /start-aprsd.sh
COPY start-direwolf.sh /start-direwolf.sh
COPY mqtt_bridge.py /mqtt_bridge.py

RUN chmod +x /run.sh /start-aprsd.sh /start-direwolf.sh

CMD ["/run.sh"]
