FROM local-run-harbor-base


# Install GitHub CLI
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg && \
    chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null && \
    apt-get update && \
    apt-get install -y gh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --break-system-packages python-dotenv composio composio-openai-agents openai-agents

RUN mkdir -p /home/user && chmod 0755 /home/user

# Create trial_id file for initial state tests (it will be overwritten in the actual environment)
RUN mkdir -p /logs && echo "000" > /logs/trial_id

LABEL Author="any-task-builder"
LABEL Description="Composio Python environment for GitHub star automation."

# Container contents:
#   - composio, composio-openai-agents, openai-agents installed via pip
#   - gh CLI installed
#   - /home/user base directory

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
