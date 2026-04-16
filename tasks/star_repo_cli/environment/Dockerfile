FROM local-run-harbor-base


# Install GitHub CLI
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg && \
    chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null && \
    apt-get update && \
    apt-get install gh -y

# Install unzip
RUN apt-get install unzip -y

# Install Composio CLI
RUN curl -fsSL https://composio.dev/install | bash && ln -sf ~/.composio/composio /usr/local/bin/composio

RUN mkdir -p /home/user && chmod 0755 /home/user

LABEL Author="any-task-builder"
LABEL Description="Composio CLI and GitHub CLI environment for starring repositories."

RUN mkdir -p /home/user/star-task && \
    chmod 0755 /home/user/star-task

# Container contents:
#   - always required libs: curl ca-certificates git python3 python3-pip python3-pytest bash
#   - gh CLI for GitHub operations
#   - composio CLI for tool execution
#   - /home/user/star-task: base directory for the project

CMD ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
