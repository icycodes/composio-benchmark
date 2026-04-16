FROM local-run-harbor-base


RUN pip3 install --break-system-packages python-dotenv composio

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Composio Python environment for manual authentication flow."

# Container contents:
#   - composio installed via pip
#   - /home/user base directory

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
