with open("image_urls.txt", "w") as f:

    for i in range(1, 101):
        f.write(f"https://picsum.photos/seed/{i}/600/400\n")

print("Write 100 image and link to image_urls.txt")
