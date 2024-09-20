import requests
from requests.auth import HTTPBasicAuth
import json
import argparse

# Function to add a comment to a Jira issue
def add_comment_to_issue(domain, api_token, email, issue_key, comment_text):
    url = f'https://{domain}/rest/api/3/issue/{issue_key}/comment'
    auth = HTTPBasicAuth(email, api_token)
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "body": comment_text
    })

    response = requests.post(url, headers=headers, auth=auth, data=payload)

    if response.status_code == 201:
        print('Comment added successfully.')
    else:
        print(f'Failed to add comment. Status Code: {response.status_code}')
        print(f'Response: {response.text}')

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description='Add a comment to a Jira issue.')

    parser.add_argument('--domain', type=str, required=True, help='Your Jira domain (e.g., yourdomain.atlassian.net)')
    parser.add_argument('--api_token', type=str, required=True, help='Your Jira API token')
    parser.add_argument('--email', type=str, required=True, help='Your Jira account email')
    parser.add_argument('--issue_key', type=str, required=True, help='The Jira issue key (e.g., PROJECT-123)')
    parser.add_argument('--comment', type=str, required=True, help='The comment text to add to the issue')

    args = parser.parse_args()

    add_comment_to_issue(args.domain, args.api_token, args.email, args.issue_key, args.comment)

if __name__ == "__main__":
    main()