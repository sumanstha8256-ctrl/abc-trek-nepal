from PIL import Image

img_path = r"C:\Users\user\.gemini\antigravity-ide\brain\abf1610e-f8e3-41a6-ac41-ffa3516aa03e\.user_uploaded\media_1788835189229.jpg"
img = Image.open(img_path).convert("RGB")
w, h = img.size
pixels = img.load()

# Count non-(255,255,255) pixels in the outermost 10 pixels
edge_non_white = 0
for x in range(w):
    for y in [0, 1, 2, 3, 4, h-5, h-4, h-3, h-2, h-1]:
        if pixels[x, y] != (255, 255, 255):
            edge_non_white += 1
for y in range(h):
    for x in [0, 1, 2, 3, 4, w-5, w-4, w-3, w-2, w-1]:
        if pixels[x, y] != (255, 255, 255):
            edge_non_white += 1

print(f"Edge non-white count: {edge_non_white} (out of {w*10 + h*10} pixels)")
