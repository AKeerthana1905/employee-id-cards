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
github_username = "akeerthana1905"
html_filename = f"{employee_data['id']}.html"
hosted_url = f"https://{github_username}.github.io/employee-id-cards/{html_filename}"

# === HTML FULLSCREEN CARD WITH FIXED CURLY BRACES ===
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Employee Details</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
  <style>
    html, body {{
      margin: 0;
      padding: 0;
      height: 100%;
      width: 100%;
      font-family: 'Roboto', sans-serif;
      background: url('https://images.unsplash.com/photo-1521790945508-bf2a36314e85?auto=format&fit=crop&w=1350&q=80') no-repeat center center fixed;
      background-size: cover;
      background-color: #000080;
      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
    }}

    .card {{
      width: 95vw;
      max-width: 700px;
      padding: 6vw;
      background: rgba(0, 0, 128, 0.9);
      border-radius: 20px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }}

    h2 {{
      color: darkgoldenrod;
      font-size: 8vw;
      margin-bottom: 5vw;
      text-align: center;
    }}

    p {{
      font-size: 6vw;
      margin: 3vw 0;
    }}

    strong {{
      color: #ffcc00;
    }}

    @media (min-width: 600px) {{
      .card {{ padding: 40px; }}
      h2 {{ font-size: 36px; }}
      p {{ font-size: 22px; }}
    }}
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
