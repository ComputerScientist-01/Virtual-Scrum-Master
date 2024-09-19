import json
import streamlit as st
import static_buttons

# Load JSON data
with open('dummy_data.json', 'r') as file:
    jira_dashboard_data = json.load(file)

# Define the sidebar
st.sidebar.title("Jira Task Manager")
st.sidebar.write("Manage your Jira tasks with ease!")

# Add buttons to the sidebar
create_task_button = st.sidebar.button("Create New Task")
clone_task_button = st.sidebar.button("Clone Task")
update_task_button = st.sidebar.button("Update Existing Task")

# Define the main page
st.title("Jira Task Manager")

# Create a text input for the user to enter their prompt
prompt = st.text_input("Enter your prompt:")

# Define the functionality for each button
if create_task_button:
    # Create a new task
    st.write("Create a new task")
    task_details = st.text_input("Enter task details (e.g. title, description, assignee):")
    jira_task = static_buttons.create_jira_task(task_details)
    st.write("Task created successfully!")
    st.write(jira_task)

if clone_task_button:
    # Clone a task
    st.write("Clone a task")
    task_to_clone = st.text_input("Enter the title of the task to clone:")
    clone_details = st.text_input("Enter the details to update (e.g. title, description, assignee):")
    jira_task = static_buttons.clone_jira_task(task_to_clone, clone_details)
    st.write("Task cloned successfully!")
    st.write(jira_task)

if update_task_button:
    # Update an existing task
    st.write("Update an existing task")
    task_to_update = st.text_input("Enter the title of the task to update:")
    update_details = st.text_input("Enter the details to update (e.g. title, description, assignee):")
    jira_task = static_buttons.update_existing_task(task_to_update, update_details)
    st.write("Task updated successfully!")
    st.write(jira_task)

# Call the main function
#if __name__ == '__main__':
#    main()