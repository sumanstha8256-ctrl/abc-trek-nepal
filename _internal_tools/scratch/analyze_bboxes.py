from PIL import Image

img_path = r"C:\Users\user\.gemini\antigravity-ide\brain\abf1610e-f8e3-41a6-ac41-ffa3516aa03e\.user_uploaded\media_1788835189229.jpg"
img = Image.open(img_path)
pixels = img.load()
w, h = img.size

# Find bounds of circle emblem (y from 310 to 610)
c_left, c_top, c_right, c_bottom = w, h, 0, 0
for y in range(310, 610):
    for x in range(w):
        r, g, b = pixels[x, y]
        if r < 240 or g < 240 or b < 240:
            if x < c_left: c_left = x
            if x > c_right: c_right = x
            if y < c_top: c_top = y
            if y > c_bottom: c_bottom = y

print(f"Emblem bbox: left={c_left}, top={c_top}, right={c_right}, bottom={c_bottom}")
print(f"Emblem width={c_right - c_left}, height={c_bottom - c_top}")
print(f"Emblem center x={(c_left+c_right)/2}, y={(c_top+c_bottom)/2}")

# Find bounds of text (y from 610 to 725)
t_left, t_top, t_right, t_bottom = w, h, 0, 0
for y in range(610, 725):
    for x in range(w):
        r, g, b = pixels[x, y]
        if r < 240 or g < 240 or b < 240:
            if x < t_left: t_left = x
            if x > t_right: t_right = x
            if y < t_top: t_top = y
            if y > t_bottom: t_bottom = y

print(f"Text bbox: left={t_left}, top={t_top}, right={t_right}, bottom={t_bottom}")
print(f"Text width={t_right - t_left}, height={t_bottom - t_top}")
