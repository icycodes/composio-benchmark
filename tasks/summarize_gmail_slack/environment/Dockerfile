FROM local-run-harbor-base


# Install Node.js v24
RUN curl -fsSL https://deb.nodesource.com/setup_24.x | bash - && \
    apt-get install -y --no-install-recommends nodejs

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Node.js environment for Composio TypeScript SDK tasks."

RUN mkdir -p /home/user/summarize-task && \
    chmod 0755 /home/user/summarize-task

# Container contents:
#   - always required libs: curl ca-certificates git python3 python3-pip python3-pytest bash
#   - Node.js v24
#   - /home/user/summarize-task: base directory for the project

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
