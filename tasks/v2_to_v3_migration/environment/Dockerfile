FROM local-run-harbor-base

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        curl ca-certificates git python3 python3-pip python3-pytest bash unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --break-system-packages composio

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Composio environment for v2 to v3 migration."

RUN cat >/home/user/old_script.py <<'EOF'
from composio import Composio
composio = Composio()
session = composio.create(user_id="zealt-user01")
# v2 syntax: session.actions()
actions = session.actions()
print(f"Actions: {len(actions)}")
# v2 syntax: update_toolkits()
session.update_toolkits(["github"])
EOF

# Container contents:
#   - composio installed
#   - /home/user directory created
#   - /home/user/old_script.py created with v2 syntax

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
