import json
import streamlit as st
import requests

# Load JSON data
with open('dummy_data.json', 'r') as file:
    jira_dashboard_data = json.load(file)

def get_llm_response(prompt):
    api_endpoint = 'http://hkl20164337.hc.cloud.hk.hsbc:12234/v1/chat/completions'
    access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0X2lkIjoiZmFkZTk2ODg2ODJhYjRiMjY1OTZmZTUyNWRlYzY1MTIiLCJ1c2VyX25hbWUiOiIyYWNmNTI4YTY2YTAxOGUxZjMyZmY2MmUxZjk5OTVmNCIsInNjb3BlIjpbImFsbCJdLCJ1cmxMaXN0IjoiL3Rlc3QvcGVybWlzc2lvbiIsImV4cCI6MTczNjM1NzAxMSwiYXV0aG9yaXRpZXMiOlsiMmFjZjUyOGE2NmEwMThlMWYzMmZmNjJlMWY5OTk1ZjQiXSwianRpIjoiOThhMDUyMjktZmY0Ni00MjRlLTlkYjMtMmNlOTdkMTAzNWZjIiwia2V5IjoiMmFjZjUyOGE2NmEwMThlMWYzMmZmNjJlMWY5OTk1ZjQiLCJjbGllbnRfaWQiOiJjbGllbnQtYXBwIn0.Tz745gy37qqNEwatBQCl9j5ZkmM8sc055CrMmSjofQFa8RkWoKlFzg_d9MgxMbi4wHKRzYVDWVVDYjGk5ktrxrkPK46h8LYlEd5k16kKD13_WL4aZuk_eCbPWhkMIlsd0s7yvwLcnvWAfdRn4pcntdOXVZp-cyrdsbCTl8f2LeK2SFZXlJtVc8ROIWOjLjnoocfWjVadLzd3TEbLW7JPv_QaLL-qCHkq09AB2wuxKeIDjdVEuX7esCzbU7A5nnH2_NX9ZA6wYUpwHPmURZL1ZccMB_krrFOhf6kW9JMgtw5LJiYE8oft9F8AMSz_Vv0eBljVxJaZqMDcqpX6Diojzw'
    model = 'gpt-4-turbo-2024-04-09'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    
    data = {
        'model': model,
        'messages': [{'role': 'user', 'content': f"{jira_dashboard_data}\n\n{prompt}"}]
    }
    
    response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        response_data = response.json()
        # Extract the content from the response
        if 'choices' in response_data and len(response_data['choices']) > 0:
            message = response_data['choices'][0].get('message', {})
            content = message.get('content', '')
            return content
        else:
            return 'No content found in response.'
    else:
        return f'Error: {response.status_code} - {response.text}'

#Create new task
def create_jira_task(prompt):
    jira_task = {
      "assignee": "",
      "reporter": "",
      "title": "",
      "description": "",
      "issue type": "",
      "sprint details": [
          {
              "sprint_name": "",
              "start_date": "",
              "end_date": "",
              "state": ""
          }
      ],
      "priority": "",
      "story points": "",
      "fix version": "",
      "labels": "",
      "status": "To do"
    }

    fields = prompt.split(',')
    for field in fields:
        key_value = field.split(':')  # Split each field into key and value
        if len(key_value) == 2:
            key = key_value[0].strip().lower()
            value = key_value[1].strip()
            if key in jira_task:
                jira_task[key] = value
    return jira_task

#Clone a task
def clone_jira_task(task,prompt):
    for issue in jira_dashboard_data["issues"]:
        if task in issue["title"]:
            jira_task = issue

    fields = prompt.split(',')
    for field in fields:
        key_value = field.split(':')  # Split each field into key and value
        if len(key_value) == 2:
            key = key_value[0].strip().lower()
            value = key_value[1].strip()
            if key in jira_task:
                jira_task[key] = value
    jira_task["status"] = "To do"
    jira_task["start_date"] = ""
    jira_task["closing_date"] = ""
    jira_task["branch_details"] = {}
    jira_task["comments"] = []
    return jira_task

#Update existing task
def update_existing_task(task,prompt):
    for issue in jira_dashboard_data["issues"]:
        if task in issue["title"]:
            jira_task = issue

    fields = prompt.split(',')
    for field in fields:
        key_value = field.split(':')  # Split each field into key and value
        if len(key_value) == 2:
            key = key_value[0].strip().lower()
            value = key_value[1].strip()
            if key in jira_task:
                jira_task[key] = value
    return jira_task

#Find a task



def main():
    #create task
    # user_input = input("Enter details: ")
    # jira = create_jira_task(user_input)
    # print(jira)

    #clone a task
    # existing_task = input("Enter task: ")
    # print(type(existing_task))
    # user_input = input("Enter details: ")
    # jira = clone_jira_task(existing_task,user_input)
    # print(jira)

    #update existing task
    # existing_task = input("Enter task: ")
    # print(type(existing_task))
    # user_input = input("Enter details: ")
    # jira = update_existing_task(existing_task,user_input)
    # print(jira)

    #find task

    if __name__ == '__main__':
        main()
