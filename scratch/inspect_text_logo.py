from PIL import Image

img_path = r"C:\Users\user\.gemini\antigravity-ide\brain\abf1610e-f8e3-41a6-ac41-ffa3516aa03e\.user_uploaded\media_1788835189229.jpg"
img = Image.open(img_path)
pixels = img.load()

# Check the letter A of ABC
# Bbox of text was left=200, top=615, right=841, bottom=711
# Let's inspect x from 200 to 280, y from 615 to 675
# Specifically let's see colors in the "A"
colors = set()
for y in range(615, 675):
    for x in range(200, 275):
        r, g, b = pixels[x, y]
        if r < 240 or g < 240 or b < 240:
            colors.add((r, g, b))

print(f"Sample of colors in 'ABC': {list(colors)[:10]}")

# Is there white inside the mountain cutout of the letter 'A'?
# Let's check the center of the 'A'
a_center_colors = []
for y in range(635, 660):
    for x in range(220, 245):
        a_center_colors.append(pixels[x, y])

print(f"Sample inside 'A': {a_center_colors[:5]}")
