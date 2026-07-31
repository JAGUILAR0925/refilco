#!/usr/bin/env python3
"""
RevisTech Week 1 Email Campaign Sender
Automatically sends 20 personalized sponsor emails from EMAILS_TO_SEND_WEEK1.md
"""

import re
import base64
import os
from datetime import datetime
from pathlib import Path
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle

# Gmail API scope
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

class EmailSender:
    def __init__(self):
        self.service = None
        self.tracking_file = "tracking_week1.txt"
        self.sent_emails = []

    def authenticate(self):
        """Authenticate with Gmail API using OAuth2"""
        creds = None

        # Check if token already exists
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        # If no valid credentials, get new ones
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            # Save credentials for next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('gmail', 'v1', credentials=creds)
        print("✅ Gmail API authenticated")

    def parse_emails(self):
        """Parse emails from EMAILS_TO_SEND_WEEK1.md"""
        with open('EMAILS_TO_SEND_WEEK1.md', 'r', encoding='utf-8') as f:
            content = f.read()

        # Split by EMAIL X: pattern
        email_blocks = re.split(r'## EMAIL \d+:', content)[1:]

        emails = []
        for block in email_blocks:
            lines = block.strip().split('\n')

            # Extract company name
            company = lines[0].strip()

            # Extract To and Subject
            to_line = [l for l in lines if l.startswith('**To**')]
            subject_line = [l for l in lines if l.startswith('**Subject**')]

            if not to_line or not subject_line:
                continue

            to = to_line[0].split('**To**:')[1].strip()
            subject = subject_line[0].split('**Subject**:')[1].strip()

            # Extract body (everything after ```line until next ```)
            body_start = block.find('```\n') + 4
            body_end = block.find('\n```', body_start)
            body = block[body_start:body_end].strip()

            emails.append({
                'company': company,
                'to': to,
                'subject': subject,
                'body': body
            })

        print(f"✅ Parsed {len(emails)} emails from EMAILS_TO_SEND_WEEK1.md")
        return emails

    def send_email(self, to, subject, body):
        """Send a single email via Gmail API"""
        try:
            message = MIMEText(body)
            message['to'] = to
            message['subject'] = subject

            raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            send_message = {'raw': raw_message}

            self.service.users().messages().send(
                userId='me',
                body=send_message
            ).execute()

            return True
        except Exception as e:
            print(f"❌ Error sending to {to}: {e}")
            return False

    def log_email(self, company, to, subject, success):
        """Log email to tracking file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "✓ Sent" if success else "✗ Failed"

        self.sent_emails.append({
            'company': company,
            'to': to,
            'timestamp': timestamp,
            'status': status
        })

        print(f"{status} | {company} → {to} ({timestamp})")

    def save_tracking(self):
        """Save tracking to file"""
        with open(self.tracking_file, 'w', encoding='utf-8') as f:
            f.write("=== SEMANA 1 - TRACKING ===\n\n")

            for email in self.sent_emails:
                f.write(f"[{email['status']}] {email['company']}\n")
                f.write(f"    To: {email['to']}\n")
                f.write(f"    Time: {email['timestamp']}\n\n")

            f.write(f"\n--- RESUMEN ---\n")
            f.write(f"Total enviados: {len(self.sent_emails)}\n")
            f.write(f"Exitosos: {sum(1 for e in self.sent_emails if '✓' in e['status'])}\n")
            f.write(f"Fallidos: {sum(1 for e in self.sent_emails if '✗' in e['status'])}\n")

        print(f"✅ Tracking saved to {self.tracking_file}")

    def run(self):
        """Main execution"""
        print("\n🚀 RevisTech Week 1 Email Campaign\n")

        # Authenticate
        self.authenticate()

        # Parse emails
        emails = self.parse_emails()

        if not emails:
            print("❌ No emails found!")
            return

        # Send emails
        print(f"\n📧 Sending {len(emails)} emails...\n")

        for i, email in enumerate(emails, 1):
            print(f"[{i}/{len(emails)}] {email['company']}...")
            success = self.send_email(
                email['to'],
                email['subject'],
                email['body']
            )
            self.log_email(
                email['company'],
                email['to'],
                email['subject'],
                success
            )

        # Save tracking
        self.save_tracking()

        print(f"\n✅ Campaign complete! Check {self.tracking_file}")

if __name__ == '__main__':
    sender = EmailSender()
    sender.run()
