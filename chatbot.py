import json
import streamlit as st
import requests

# Load JSON data
with open('mock_data/jira_dashboard.json', 'r') as file:
    jira_dashboard_data = json.load(file)

with open('mock_data/jira_all_sprints.json', 'r') as file:
    all_sprints_data = json.load(file)

with open('mock_data/jira_sprint1.json', 'r') as file:
    sprint1_data = json.load(file)

with open('mock_data/jira_sprint2.json', 'r') as file:
    sprint2_data = json.load(file)

with open('mock_data/jira_sprint3.json', 'r') as file:
    sprint3_data = json.load(file)

# def read_prompt(prompt):
#     data = {}
#     if "Sprint 1" or "sprint 1" in prompt:
#         data.update(sprint1_data)
#     if "Sprint 2" or "sprint 2" in prompt:
#         data.update(sprint2_data)
#     if "Sprint 3" or "sprint 3" in prompt:
#         data.update(sprint3_data)
#     if "All sprints" or "all sprints":
#         data.update(all_sprints_data)
#     return data

def read_prompt(prompt):
    return jira_dashboard_data

def get_llm_response(context,prompt):
    api_endpoint = 'http://hkl20164337.hc.cloud.hk.hsbc:12234/v1/chat/completions'
    access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0X2lkIjoiZmFkZTk2ODg2ODJhYjRiMjY1OTZmZTUyNWRlYzY1MTIiLCJ1c2VyX25hbWUiOiIyYWNmNTI4YTY2YTAxOGUxZjMyZmY2MmUxZjk5OTVmNCIsInNjb3BlIjpbImFsbCJdLCJ1cmxMaXN0IjoiL3Rlc3QvcGVybWlzc2lvbiIsImV4cCI6MTczNjM1NzAxMSwiYXV0aG9yaXRpZXMiOlsiMmFjZjUyOGE2NmEwMThlMWYzMmZmNjJlMWY5OTk1ZjQiXSwianRpIjoiOThhMDUyMjktZmY0Ni00MjRlLTlkYjMtMmNlOTdkMTAzNWZjIiwia2V5IjoiMmFjZjUyOGE2NmEwMThlMWYzMmZmNjJlMWY5OTk1ZjQiLCJjbGllbnRfaWQiOiJjbGllbnQtYXBwIn0.Tz745gy37qqNEwatBQCl9j5ZkmM8sc055CrMmSjofQFa8RkWoKlFzg_d9MgxMbi4wHKRzYVDWVVDYjGk5ktrxrkPK46h8LYlEd5k16kKD13_WL4aZuk_eCbPWhkMIlsd0s7yvwLcnvWAfdRn4pcntdOXVZp-cyrdsbCTl8f2LeK2SFZXlJtVc8ROIWOjLjnoocfWjVadLzd3TEbLW7JPv_QaLL-qCHkq09AB2wuxKeIDjdVEuX7esCzbU7A5nnH2_NX9ZA6wYUpwHPmURZL1ZccMB_krrFOhf6kW9JMgtw5LJiYE8oft9F8AMSz_Vv0eBljVxJaZqMDcqpX6Diojzw'
    model = 'gpt-4-turbo-2024-04-09'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    
    data = {
        'model': model,
        'messages': [{'role': 'user', 'content': f"{context}\n\n{prompt}"}]
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

def main():
    st.title("Welcome to Virtual Scrum Master")
    prompt = st.text_input("Hello! How can I help you?")
    sprint_data = read_prompt(prompt)
    response = get_llm_response(sprint_data,prompt)
    st.success(response)

if __name__ == '__main__':
    main()
