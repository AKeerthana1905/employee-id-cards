import qrcode

# === EMPLOYEE DETAILS ===
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

# === GITHUB USERNAME ===
github_username = "akeerthana1905"  # change if needed
html_filename = f"{employee_data['id']}.html"
hosted_url = f"https://{github_username}.github.io/employee-id-cards/{html_filename}"

# === HTML FULLSCREEN CARD ===
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Employee Details</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Roboto', sans-serif; }}
    body {{ display: flex; justify-content: center; align-items: center; height: 100vh; background: white; color: white; }}
    .card {{ background: #000080; padding: 40px; border-radius: 16px; box-shadow: 0 8px 24px rgba(0,0,0,0.1); width: 90%; max-width: 500px; }}
    h2 {{ margin-bottom: 20px; color: #2c3e50; }}
    p {{ margin: 10px 0; font-size: 18px; }}
    strong {{ color: #555; }}
  </style>
</head>
<body>
  <div class="card">
    <h2>Employee Details</h2>
    <p><strong>ID:</strong> {employee_data['id']}</p>
    <p><strong>Name:</strong> {employee_data['name']}</p>
    <p><strong>Department:</strong> {employee_data['department']}</p>
    <p><strong>Role:</strong> {employee_data['role']}</p>
    <p><strong>Email:</strong> {employee_data['email']}</p>
    <p><strong>Phone:</strong> {employee_data['phone']}</p>
    <p><strong>Company:</strong> {employee_data['company']}</p>
    <p><strong>Valid Until:</strong> {employee_data['valid_until']}</p>
  </div>
</body>
</html>
"""

# === SAVE HTML FILE ===
with open(html_filename, "w", encoding="utf-8") as f:
    f.write(html_content)

# === GENERATE QR CODE ===
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(hosted_url)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("employee_qr.png")
img.show()

print("\n✅ Upload this HTML file to GitHub Pages:")
print(f"🔗 {hosted_url}")
print("✅ QR code image saved as 'employee_qr.png'")
