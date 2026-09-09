from PIL import Image, ImageOps
import numpy as np

img_path = r"C:\Users\user\.gemini\antigravity-ide\brain\abf1610e-f8e3-41a6-ac41-ffa3516aa03e\.user_uploaded\media_1788835189229.jpg"
img = Image.open(img_path).convert("RGB")
w, h = img.size

# Check what color the background is outside the logo content
arr = np.array(img, dtype=np.float32)

# Find background color around the edges
bg_samples = []
bg_samples.extend(arr[0:20, :].reshape(-1, 3))
bg_samples.extend(arr[-20:, :].reshape(-1, 3))
bg_samples.extend(arr[:, 0:20].reshape(-1, 3))
bg_samples.extend(arr[:, -20:].reshape(-1, 3))
bg_mean = np.mean(bg_samples, axis=0)
print("Background sample mean RGB:", bg_mean)
