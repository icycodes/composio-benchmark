# GitHub Trigger and Sentiment Analysis with Composio

## Background
Composio Triggers allow agents to react to external events in real-time. In this task, you will set up a workflow that listens for new GitHub issues and posts a sentiment analysis to Slack.

## Requirements
1. Create a Python script `trigger_agent.py` in `/home/user/trigger-task`.
2. The script must use the Composio Python SDK and the OpenAI SDK.
3. The script must create a new public repository named `harbor-trigger-${trial_id}` under `zealt-user01`.
4. The script must set up a **Composio Trigger** to listen for `github_issue_created` events on this repository.
5. When a new issue is created, the script must use an AI agent to analyze the issue's sentiment (Positive, Neutral, or Negative).
6. The agent must post the sentiment analysis to a Slack channel named `sentiment-${trial_id}`.
7. To test the workflow, the script must programmatically create a new issue in the repository with the title "Great work on the new feature!" and body "I really love how this works.".

## Implementation Guide
1. Read the `trial_id` from `/logs/trial_id`.
2. Create the GitHub repository and Slack channel.
3. Initialize Composio and create a session for `zealt-user01`.
4. Subscribe to the `github_issue_created` trigger for the new repository.
5. Implement a listener that receives the trigger payload.
6. Pass the issue content to an OpenAI agent for sentiment analysis.
7. Use the agent to post the result to the Slack channel.
8. Create the test issue to fire the trigger.

## Constraints
- Project path: /home/user/trigger-task
- Use the test user `zealt-user01`.
- Read `trial_id` from `/logs/trial_id` for repo and channel names.

## Integrations
- Composio
- GitHub
- Slack
- OpenAI
