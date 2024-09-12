from jira_api import JiraAPI
from chatgpt_api import ChatGPTAPI

def main():
    # Set up Jira API credentials
    jira_url = "https://your-jira-instance.atlassian.net"
    jira_username = "your-jira-username"
    jira_password = "your-jira-password"

    # Set up ChatGPT API credentials
    chatgpt_api_key = "your-chatgpt-api-key"

    # Create Jira API instance
    jira_api = JiraAPI(jira_url, jira_username, jira_password)

    # Create ChatGPT API instance
    chatgpt_api = ChatGPTAPI(chatgpt_api_key)

    # Example usage
    issue_key = "ABC-123"
    prompt = f"What is the velocity of the assignee for Jira issue {issue_key}?"
    response = chatgpt_api.ask(prompt)

    # Get the assignee velocity from Jira API
    velocity = jira_api.get_assignee_velocity(issue_key)

    print("ChatGPT Response:", response)
    print("Assignee Velocity:", velocity)

if __name__ == "__main__":
    main()