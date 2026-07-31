#!/usr/bin/env python3
"""
RevisTech Week 1 Email Campaign - SMTP Version (FREE)
Sends 20 personalized sponsor emails using Gmail SMTP
No Google Cloud required. No costs.
"""

import re
import smtplib
import time
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def __init__(self, sender_email, app_password):
        self.sender_email = sender_email
        self.app_password = app_password
        self.tracking_file = "tracking_week1.txt"
        self.sent_emails = []

    def authenticate(self):
        """Connect to Gmail SMTP"""
        try:
            self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.server.login(self.sender_email, self.app_password)
            print("✅ Gmail SMTP authenticated (FREE)\n")
            return True
        except Exception as e:
            print(f"❌ Authentication failed: {e}")
            print("   Verifica:")
            print("   1. Email correcto")
            print("   2. Contraseña de app correcta")
            print("   3. 2FA habilitado en Gmail")
            return False

    def parse_emails(self):
        """Parse emails from EMAILS_TO_SEND_WEEK1.md"""
        try:
            with open('EMAILS_TO_SEND_WEEK1.md', 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print("❌ EMAILS_TO_SEND_WEEK1.md no encontrado")
            return []

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

        print(f"✅ Parsed {len(emails)} emails from EMAILS_TO_SEND_WEEK1.md\n")
        return emails

    def send_email(self, to, subject, body):
        """Send a single email via Gmail SMTP"""
        try:
            # Create message
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = self.sender_email
            message["To"] = to

            # Attach body
            message.attach(MIMEText(body, "plain"))

            # Send
            self.server.sendmail(self.sender_email, to, message.as_string())

            return True
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return False

    def log_email(self, company, to, subject, success):
        """Log email to tracking"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "✓ Sent" if success else "✗ Failed"

        self.sent_emails.append({
            'company': company,
            'to': to,
            'timestamp': timestamp,
            'status': status
        })

        print(f"   {status} | {company} → {to}")

    def save_tracking(self):
        """Save tracking to file"""
        with open(self.tracking_file, 'w', encoding='utf-8') as f:
            f.write("=== SEMANA 1 - TRACKING ===\n\n")

            for email in self.sent_emails:
                f.write(f"[{email['status']}] {email['company']}\n")
                f.write(f"    To: {email['to']}\n")
                f.write(f"    Time: {email['timestamp']}\n\n")

            f.write(f"\n--- RESUMEN ---\n")
            successful = sum(1 for e in self.sent_emails if '✓' in e['status'])
            failed = sum(1 for e in self.sent_emails if '✗' in e['status'])

            f.write(f"Total enviados: {len(self.sent_emails)}\n")
            f.write(f"Exitosos: {successful}\n")
            f.write(f"Fallidos: {failed}\n")

        print(f"\n✅ Tracking guardado en {self.tracking_file}")

    def run(self):
        """Main execution"""
        print("\n🚀 RevisTech Week 1 Email Campaign (SMTP - FREE)\n")

        # Authenticate
        if not self.authenticate():
            return

        # Parse emails
        emails = self.parse_emails()

        if not emails:
            print("❌ No emails found!")
            return

        # Send emails
        print(f"📧 Enviando {len(emails)} emails...\n")

        for i, email in enumerate(emails, 1):
            print(f"[{i}/{len(emails)}] {email['company']}...", end='')
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

            # Delay between emails (respeta limite de Gmail)
            if i < len(emails):
                time.sleep(1)

        # Close connection
        self.server.quit()

        # Save tracking
        self.save_tracking()

        print(f"\n✅ ¡Campaña completada! Check {self.tracking_file}")

if __name__ == '__main__':
    # CONFIGURACION
    SENDER_EMAIL = "jaguilar0925@pearson.com"
    APP_PASSWORD = input("Ingresa tu contraseña de app de Gmail: ")

    # Run
    sender = EmailSender(SENDER_EMAIL, APP_PASSWORD)
    sender.run()
