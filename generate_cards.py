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
  html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
    overflow: hidden; /* Prevents scrolling */
  }
  .fullscreen-container {
    height: 100vh;
    width: 100vw;
    background: #f0f0f0; /* change to your background */
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>

<body>
  <div class="fullscreen-container">
    <h1>Employee ID Details</h1>
    <!-- Your content here -->
  </div>
</body>

</head>
<body>
  <div class="card">
    <h2>Employee Details</h2>
    <div class="info"><span class="label">ID:</span> {employee_data['id']}</div>
    <div class="info"><span class="label">Name:</span> {employee_data['name']}</div>
    <div class="info"><span class="label">Department:</span> {employee_data['department']}</div>
    <div class="info"><span class="label">Role:</span> {employee_data['role']}</div>
    <div class="info"><span class="label">Email:</span> {employee_data['email']}</div>
    <div class="info"><span class="label">Phone:</span> {employee_data['phone']}</div>
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

print("✅ Fullscreen, bold HTML file generated: EMP23456.html")
