import qrcode
import os
import uuid
from string import Template  # ✅ NEW: for safe placeholder formatting

# ✅ Step 1: Employee data
employee = {
    "name": "Amit Sharma",
    "emp_id": "EMP123456",
    "designation": "Software Engineer",
    "department": "AI & ML",
    "email": "amit.sharma@company.com",
    "phone": "+91-9876543210",
    "location": "Bangalore, India"
}

# ✅ Step 2: Add a unique ID
employee['unique_id'] = str(uuid.uuid4())

# ✅ Step 3: Load the HTML template using string.Template
with open("employee_template.html", "r", encoding="utf-8") as f:
    template = Template(f.read())  # use Template instead of str.format()

# ✅ Step 4: Fill placeholders with employee data
html_content = template.substitute(employee)

# ✅ Step 5: Save the output HTML file
output_folder = "cards"
os.makedirs(output_folder, exist_ok=True)
filename = f"{employee['emp_id']}.html"
html_path = os.path.join(output_folder, filename)
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# ✅ Step 6: Create QR code for hosted URL (you'll update the URL later)
url = f"https://yourusername.github.io/employee-id-cards/{filename}"
qr = qrcode.make(url)
qr.save(os.path.join(output_folder, f"{employee['emp_id']}_qr.png"))

print(f"✅ HTML saved to: {html_path}")
print(f"✅ QR code saved. It links to: {url}")
