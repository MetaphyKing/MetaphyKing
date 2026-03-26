import random
import re

# Your 4 videos
videos = [
    "https://github.com/user-attachments/assets/0a4ae2e4-9ef1-47d7-bd20-cdf29cd13102",
    "https://github.com/user-attachments/assets/ff3aada3-63d2-40b8-b7e6-fe436c53879a",
    "https://github.com/user-attachments/assets/d6263d0a-e7d4-4f13-914a-72ed2459a2a6",
    "https://github.com/user-attachments/assets/f2f48b68-5341-4c9b-9cfa-cf7c5f63e904"
]

fallback_image = "https://github.com/user-attachments/assets/113ea173-bc28-4898-ace2-be41e9511e75"

# Pick one at random
random_video = random.choice(videos)

video_html = f'''<div align="center">
  <video src="{random_video}"
    poster="{fallback_image}"
    muted="muted"
    autoplay="autoplay"
    loop="loop"
    playsinline
    controlslist="nodownload"
    style="width: 100%; max-width: 800px; height: auto; border-radius: 10px; display: block;">
    <img src="{fallback_image}" style="width: 100%; max-width: 800px; border-radius: 10px;">
  </video>
</div>'''

# Read current README
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace everything between the markers
new_content = re.sub(
    r'<!-- RANDOM_VIDEO_START -->.*?<!-- RANDOM_VIDEO_END -->',
    f'<!-- RANDOM_VIDEO_START -->\n{video_html}\n<!-- RANDOM_VIDEO_END -->',
    content,
    flags=re.DOTALL
)

# Write back
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ README updated with random video")
