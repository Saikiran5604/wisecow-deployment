FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install prerequisites AND the actual fortune data packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fortune-mod \
    cowsay \
    netcat-openbsd \
    fortunes && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add cowsay and fortune binaries to PATH
ENV PATH="/usr/games:$PATH"

WORKDIR /app

COPY wisecow.sh /app/wisecow.sh
RUN chmod +x /app/wisecow.sh

EXPOSE 4499

CMD ["./wisecow.sh"]