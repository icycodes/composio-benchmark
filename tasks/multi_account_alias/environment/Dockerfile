FROM local-run-harbor-base


# Install Composio SDK
RUN pip3 install --break-system-packages composio

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Composio Python SDK environment for multi-account alias management."

RUN mkdir -p /home/user/alias-task && \
    chmod 0755 /home/user/alias-task

# Container contents:
#   - always required libs: curl ca-certificates git python3 python3-pip python3-pytest bash
#   - composio SDK for Python
#   - /home/user/alias-task: base directory for the project

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
