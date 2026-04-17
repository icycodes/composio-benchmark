FROM local-run-harbor-base

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --break-system-packages composio
RUN curl -fsSL https://composio.dev/install | bash && ln -sf ~/.composio/composio /usr/local/bin/composio

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Composio CLI environment for tool exploration."

# Container contents:
#   - composio CLI installed
#   - /home/user directory created

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
