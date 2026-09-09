from PIL import Image

img_path = r"C:\Users\user\.gemini\antigravity-ide\brain\abf1610e-f8e3-41a6-ac41-ffa3516aa03e\.user_uploaded\media_1788835189229.jpg"
img = Image.open(img_path)
pixels = img.load()
w, h = img.size

# Row by row non-white pixel count
for y in range(310, 725, 5):
    non_white = sum(1 for x in range(w) if pixels[x, y][0] < 240 or pixels[x, y][1] < 240 or pixels[x, y][2] < 240)
    if non_white > 0 or (y > 580 and y < 620):
        print(f"y={y:3d}: non-white count = {non_white:3d}")
