import random
import re

# Your 4 videos
videos = [
    "https://img1.wsimg.com/blobby/go/bbaabe63-6ba9-4c65-a2ee-d538211cda2a/video/Metaphy%20City.mp4",
    "https://img1.wsimg.com/blobby/go/bbaabe63-6ba9-4c65-a2ee-d538211cda2a/video/Metaphy%20Circle%20Disk.mp4",
    "https://img1.wsimg.com/blobby/go/bbaabe63-6ba9-4c65-a2ee-d538211cda2a/video/Raining%20Metaphy.mp4",
    "https://img1.wsimg.com/blobby/go/bbaabe63-6ba9-4c65-a2ee-d538211cda2a/video/Metaphy%20City%20Skyline.mp4"
]

fallback_image = "https://img1.wsimg.com/isteam/ip/bbaabe63-6ba9-4c65-a2ee-d538211cda2a/Universal%20Computing%20(2).png/:/rs=w:1160,h:773"

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