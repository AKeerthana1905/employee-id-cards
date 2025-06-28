employee_data = {
    "id": "EMP23456",
    "name": "John Doe",
    "department": "Software Engineering",
    "role": "Backend Developer",
    "email": "john.doe@company.com",
    "phone": "+91 9876543210",
    "company": "Company Name Pvt. Ltd.",
    "valid_until": "10-10-2030"
}

html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Employee ID Card - {employee_data['name']}</title>
  <style>
    html, body {{
      margin: 0;
      padding: 0;
      height: 100%;
      width: 100%;
      background-color: #0a0a0a;
      color: white;
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
    }}

    .card {{
      background-color: #001f3f;
      padding: 40px 30px;
      border-radius: 20px;
      box-shadow: 0 0 30px rgba(255, 255, 255, 0.2);
      width: 350px;
      height: 600px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      text-align: center;
    }}

    .card h2 {{
      font-size: 28px;
      color: #00bfff;
      margin-bottom: 20px;
    }}

    .info {{
      font-size: 18px;
      margin: 10px 0;
    }}

    .label {{
      font-weight: bold;
      color: #ccc;
    }}

    .footer {{
      font-size: 16px;
      color: #aaa;
      margin-top: 20px;
    }}
  </style>
</head>
<body>
  <div class="card">
    <div>
      <h2>Employee Details</h2>
      <div class="info"><span class="label">ID:</span> {employee_data['id']}</div>
      <div class="info"><span class="label">Name:</span> {employee_data['name']}</div>
      <div class="info"><span class="label">Department:</span> {employee_data['department']}</div>
      <div class="info"><span class="label">Role:</span> {employee_data['role']}</div>
      <div class="info"><span class="label">Email:</span> {employee_data['email']}</div>
      <div class="info"><span class="label">Phone:</span> {employee_data['phone']}</div>
    </div>
    <div class="footer">
      {employee_data['company']}<br>
      Valid Until: {employee_data['valid_until']}
    </div>
  </div>
</body>
</html>
"""

# Write to file
with open("EMP23456.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("✅ Portrait-style HTML ID card generated: EMP23456.html")
