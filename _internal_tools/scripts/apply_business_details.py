import os
import glob
import re

phone_display = "+977 9818188459"
whatsapp_url = "https://wa.me/9779818188459"
location_display = "Budhanilkantha, Kathmandu, Nepal"
author_display = "Sugam Shrestha"

# Find all HTML files
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
html_files = []
for root, dirs, files in os.walk(ROOT_DIR):
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

print(f"Found {len(html_files)} HTML files to update.")

for fpath in html_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update WhatsApp links
    # Replace href="https://wa.me/" or href="https://wa.me" with href="https://wa.me/9779818188459"
    content = re.sub(r'href="https://wa\.me/?"', f'href="{whatsapp_url}"', content)
    
    # 2. Update phone numbers in text
    content = content.replace("+977 980 000 0000", phone_display)
    content = content.replace("+977 61 000000", phone_display)
    content = content.replace("WhatsApp: +977 980 000 0000", f"WhatsApp: {phone_display}")
    content = content.replace("Direct WhatsApp: +977 980 000 0000", f"Direct WhatsApp: {phone_display}")
    content = content.replace("Emergency Line / WhatsApp: +977 980 000 0000", f"Emergency & WhatsApp: {phone_display}")
    content = content.replace("WhatsApp Concierge: +977 980 000 0000", f"WhatsApp: {phone_display}")

    # 3. Update Location references where relevant
    content = content.replace("Thamel, Kathmandu, Nepal", location_display)
    content = content.replace("Thamel Marg, Kathmandu, Nepal", location_display)
    
    # 4. Update Author Box references
    content = content.replace("Lead Guide Pemba Sherpa", f"{author_display}")
    content = content.replace("Verified by Lead Guide Pemba Sherpa", f"Verified by {author_display} (Expedition Director)")
    content = content.replace("Lead Expedition Operations Team", f"{author_display} & Mountain Operations Team")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("All HTML files updated with real phone, WhatsApp, location, and author details.")
