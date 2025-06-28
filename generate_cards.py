from PIL import Image, ImageDraw, ImageFont
import qrcode

# Employee details
employee = {
    "name": "Michal Smith",
    "position": "General Manager",
    "id_no": "EMP123456",
    "blood": "AB+",
    "phone": "+91 123 456 7890",
    "email": "name@mail.com",
    "valid_until": "10-10-2030",
    "qr_url": "https://akeerthana1905.github.io/employee-id-cards/EMP123456.html"
}

# Create the ID card canvas
width, height = 650, 400
card = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(card)

# Fonts
try:
    title_font = ImageFont.truetype("arialbd.ttf", 26)
    label_font = ImageFont.truetype("arial.ttf", 18)
    small_font = ImageFont.truetype("arial.ttf", 16)
except:
    title_font = label_font = small_font = ImageFont.load_default()

# Header with gradient effect simulation (simple solid)
draw.rectangle([(0, 0), (width, 70)], fill="#673AB7")
draw.text((20, 20), "EMPLOYEE ID CARD", font=title_font, fill="white")

# Profile Image Placeholder
photo_box = [30, 100, 150, 220]
draw.rectangle(photo_box, fill="#e0e0e0")
draw.text((60, 150), "Photo", font=small_font, fill="black")

# Draw employee details
info_x = 180
y = 100
spacing = 30
draw.text((info_x, y), f"Name: {employee['name']}", font=label_font, fill="#212121"); y += spacing
draw.text((info_x, y), f"Position: {employee['position']}", font=label_font, fill="#424242"); y += spacing
draw.text((info_x, y), f"ID No: {employee['id_no']}", font=label_font, fill="#424242"); y += spacing
draw.text((info_x, y), f"Phone: {employee['phone']}", font=label_font, fill="#424242"); y += spacing
draw.text((info_x, y), f"Email: {employee['email']}", font=label_font, fill="#424242"); y += spacing
draw.text((info_x, y), f"Blood Group: {employee['blood']}", font=label_font, fill="#424242"); y += spacing
draw.text((info_x, y), f"Valid Until: {employee['valid_until']}", font=label_font, fill="#424242")

# QR Code
qr = qrcode.make(employee["qr_url"])
qr = qr.resize((110, 110))
card.paste(qr, (width - 140, height - 140))

# Footer
draw.rectangle([(0, height - 40), (width, height)], fill="#673AB7")
draw.text((20, height - 35), "Scan QR for verification", font=small_font, fill="white")

# Save output
card.save("employee_id_card_attractive_output.png")
print("✅ Stylish ID card generated: employee_id_card_attractive_output.png")
