import json
import requests

url = "http://career.wemine.hk/cv-submit"

payload = {
    "name": "Ho Sze Tung",
    "email": "hoszetung2@gmail.com",
    "position": "Web Developer Trainee",
    "cv_url": "https://go.fliplink.me/view/3A0A909A-C459-4C47-BA33-6BCC9BBC3BB9",
    "intro": "Hi! I am Ho Sze Tung, a motivated Information Technology graduate with hands-on experience in full-stack web development and database management. I am eager to use my technical skills to deliver reliable software solutions as a programmer.",
    "website": "https://github.com/tungxd/HoSzeTung_Portfolio",
    "note": "I look forward to hearing from you. Thank you!",
    "code_url": "https://github.com/tungxd/application"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
try:
    print("Response Body:", response.json())
except Exception:
    print("Response Text:", response.text)