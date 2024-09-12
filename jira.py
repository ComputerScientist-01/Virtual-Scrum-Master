import requests
import json

class JiraAPI:
    def __init__(self, jira_url, username, password):
        self.jira_url = jira_url
        self.username = username
        self.password = password

    def get_issue(self, issue_key):
        auth = (self.username, self.password)
        url = f"{self.jira_url}/rest/api/2/issue/{issue_key}"
        response = requests.get(url, auth=auth)
        return response.json()

    def get_assignee_velocity(self, issue_key):
        issue_data = self.get_issue(issue_key)
        assignee_id = issue_data["fields"]["assignee"]["accountId"]
        # Assuming you have a custom field for velocity
        velocity_field = "customfield_12345"
        velocity = issue_data["fields"][velocity_field]
        return velocity