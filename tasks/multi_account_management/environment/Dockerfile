FROM local-run-harbor-base


RUN pip3 install --break-system-packages python-dotenv composio composio-openai openai

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Composio Python environment for multi-account Slack management."

# Container contents:
#   - composio, composio-openai, openai installed via pip
#   - /home/user base directory

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
