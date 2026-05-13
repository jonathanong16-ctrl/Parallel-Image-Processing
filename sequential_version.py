import os
import shutil
import requests
from PIL import Image
from io import BytesIO
import time

shutil.rmtree("images", ignore_errors=True)
shutil.rmtree("thumbnails", ignore_errors=True)

os.makedirs("images", exist_ok=True)
os.makedirs("thumbnails", exist_ok=True)

with open("image_urls.txt") as f:
    urls = [line.strip() for line in f.readlines()]

def download_and_resize(url, index):
    try:
        response = requests.get(url, timeout=10)
        image = Image.open(BytesIO(response.content))
        image.save(f"images/image_{index}.jpg")
        image = image.resize((128, 128))
        image.save(f"thumbnails/thumb_{index}.jpg")
    except Exception as e:
        print(f"[Error] URL {url} - {e}")

start = time.perf_counter()
for i, url in enumerate(urls):
    download_and_resize(url, i + 1)
end = time.perf_counter()

print(f"Sequential version completed in {end - start:.2f} seconds")
