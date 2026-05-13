import os
import shutil
import requests
from PIL import Image
from io import BytesIO
import time
from concurrent.futures import ProcessPoolExecutor

def download_and_resize_task(task):
    url, index = task
    try:
        response = requests.get(url, timeout=10)
        image = Image.open(BytesIO(response.content)).convert("RGB")
        image.save(f"images/image_{index}.jpg", format="JPEG")
        image = image.resize((128, 128))
        image.save(f"thumbnails/thumb_{index}.jpg", format="JPEG")
    except Exception as e:
        print(f"[Error] URL {url} - {e}")

if __name__ == '__main__':
    shutil.rmtree("images", ignore_errors=True)
    shutil.rmtree("thumbnails", ignore_errors=True)

    os.makedirs("images", exist_ok=True)
    os.makedirs("thumbnails", exist_ok=True)

    with open("image_urls.txt") as f:
        urls = [line.strip() for line in f.readlines()]

    start = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        executor.map(download_and_resize_task, [(url, i + 1) for i, url in enumerate(urls)])

    end = time.perf_counter()
    print(f"Parallel version completed in {end - start:.2f} seconds")
