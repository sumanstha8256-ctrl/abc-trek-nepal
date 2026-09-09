from PIL import Image

img_path = r"C:\Users\user\.gemini\antigravity-ide\brain\abf1610e-f8e3-41a6-ac41-ffa3516aa03e\.user_uploaded\media_1788835189229.jpg"
img = Image.open(img_path).convert("RGB")
pixels = img.load()

print("Pixel at (158, 288):", pixels[158, 288])
print("Pixel at (200, 315):", pixels[200, 315])
print("Pixel at (100, 100):", pixels[100, 100])

# Let's check distribution of pixels across the image
# What are the actual logo pixel values?
# Circle border is blue: what RGB is it?
print("Emblem top pixel (520, 316):", pixels[520, 316])
print("Emblem bottom pixel (520, 607):", pixels[520, 607])
print("Emblem left pixel (373, 461):", pixels[373, 461])
print("Emblem right pixel (667, 461):", pixels[667, 461])
