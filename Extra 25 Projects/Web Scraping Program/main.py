import requests
from bs4 import BeautifulSoup

username = input("Enter GitHub username: ")
url = f"https://github.com/{username}"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the profile image using the class selector
profile_img_tag = soup.find('img', {'class': 'avatar-user'})

if profile_img_tag:
    profile_image = profile_img_tag['src']
    print(f"Profile Image URL: {profile_image}")
else:
    print("Error: Profile image not found. Check GitHub's HTML structure.")
