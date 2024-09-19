import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Task Management Dashboard",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

# Mock JSON data
mock_data = [
    {
        "issue_id": "TASK-001", "status": "To Do", "priority": "High",
        "created": "2024-09-01", "resolved": None, "assignee": "Alice"
    },
    {
        "issue_id": "TASK-002", "status": "In Progress", "priority": "Medium",
        "created": "2024-09-02", "resolved": None, "assignee": "Bob"
    },
    {
        "issue_id": "TASK-003", "status": "Done", "priority": "Low",
        "created": "2024-08-25", "resolved": "2024-09-03", "assignee": "Charlie"
    },
    {
        "issue_id": "TASK-004", "status": "To Do", "priority": "High",
        "created": "2024-09-03", "resolved": None, "assignee": "Alice"
    },
    {
        "issue_id": "TASK-005", "status": "Done", "priority": "High",
        "created": "2024-08-29", "resolved": "2024-09-05", "assignee": "David"
    },
]

# Convert to DataFrame
df = pd.DataFrame(mock_data)

# Parsing date columns
df['created'] = pd.to_datetime(df['created'])
df['resolved'] = pd.to_datetime(df['resolved'], errors='coerce')

# Sidebar filters
with st.sidebar:
    st.title('📝 Task Management Dashboard')
    
    # Status filter
    status_list = df['status'].unique()
    selected_status = st.multiselect('Filter by status', status_list, default=status_list)

    # Assignee filter
    assignee_list = df['assignee'].unique()
    selected_assignee = st.multiselect('Filter by assignee', assignee_list, default=assignee_list)

    # Priority filter
    priority_list = df['priority'].unique()
    selected_priority = st.multiselect('Filter by priority', priority_list, default=priority_list)

# Apply filters
df_filtered = df[df['status'].isin(selected_status) &
                 df['assignee'].isin(selected_assignee) &
                 df['priority'].isin(selected_priority)]

# Heatmap - Issues by Priority and Status
def make_heatmap(input_df):
    heatmap_data = input_df.groupby(['status', 'priority']).size().reset_index(name='count')
    
    heatmap = alt.Chart(heatmap_data).mark_rect().encode(
        y=alt.Y('status:O', axis=alt.Axis(title="Status", titleFontSize=18)),
        x=alt.X('priority:O', axis=alt.Axis(title="Priority", titleFontSize=18)),
        color=alt.Color('count:Q', scale=alt.Scale(scheme='blues')),
        tooltip=['status', 'priority', 'count']
    ).properties(width=400, height=300)
    
    return heatmap

# Bar chart - Issues by Assignee
def make_bar_chart(input_df):
    bar_data = input_df.groupby('assignee').size().reset_index(name='count')
    
    bar_chart = alt.Chart(bar_data).mark_bar().encode(
        x=alt.X('count:Q', axis=alt.Axis(title="Number of Issues")),
        y=alt.Y('assignee:O', axis=alt.Axis(title="Assignee")),
        color=alt.Color('assignee:N', legend=None),
        tooltip=['assignee', 'count']
    ).properties(width=400, height=300)
    
    return bar_chart

# Line chart - Issue Creation Over Time
def make_line_chart(input_df):
    line_data = input_df.groupby(pd.Grouper(key='created', freq='D')).size().reset_index(name='count')

    line_chart = alt.Chart(line_data).mark_line().encode(
        x=alt.X('created:T', axis=alt.Axis(title="Date")),
        y=alt.Y('count:Q', axis=alt.Axis(title="Issues Created")),
        tooltip=['created', 'count']
    ).properties(width=700, height=300)
    
    return line_chart

# Dashboard layout
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('### Issues by Priority and Status')
    heatmap = make_heatmap(df_filtered)
    st.altair_chart(heatmap)

with col2:
    st.markdown('### Issues by Assignee')
    bar_chart = make_bar_chart(df_filtered)
    st.altair_chart(bar_chart)

with col3:
    st.markdown('### Issues Created Over Time')
    line_chart = make_line_chart(df_filtered)
    st.altair_chart(line_chart)

# Display filtered data
st.markdown('### Filtered Issue Data')
st.dataframe(df_filtered)

with st.expander("About"):
    st.write('''
    - This dashboard tracks issues in a task management system similar to JIRA.
    - You can filter by status, assignee, and priority to see different views of the data.
    - The charts show distributions of issues by priority, status, and assignee, and their creation over time.
    ''')
