from PIL import Image

img_path = r"C:\Users\user\.gemini\antigravity-ide\brain\abf1610e-f8e3-41a6-ac41-ffa3516aa03e\.user_uploaded\media_1788835189229.jpg"
img = Image.open(img_path).convert("RGB")
w, h = img.size
pixels = img.load()

# Find true bbox where pixel is significantly different from white background
# Let's say any channel < 220
left, top, right, bottom = w, h, 0, 0
for y in range(h):
    for x in range(w):
        r, g, b = pixels[x, y]
        if r < 220 or g < 220 or b < 220:
            if x < left: left = x
            if x > right: right = x
            if y < top: top = y
            if y > bottom: bottom = y

print(f"True Content bbox (threshold < 220): left={left}, top={top}, right={right}, bottom={bottom}")
print(f"Width={right - left + 1}, Height={bottom - top + 1}")
