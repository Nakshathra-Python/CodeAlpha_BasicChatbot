import re

with open("sample.txt", "r") as file:
    data = file.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", data)

with open("emails.txt", "w") as output:
    for email in emails:
        output.write(email + "\n")

print(" Email addresses extracted successfully!")

print("\nExtracted Emails:")
for email in emails:
    print(email)