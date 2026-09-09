from PIL import Image

img_path = r"C:\Users\user\.gemini\antigravity-ide\brain\abf1610e-f8e3-41a6-ac41-ffa3516aa03e\.user_uploaded\media_1788835189229.jpg"
img = Image.open(img_path)
print("Image format:", img.format)
print("Image size:", img.size)
print("Image mode:", img.mode)

# Let's inspect pixel values to check background
# Check border pixels
w, h = img.size
pixels = img.load()
corner_pixels = [pixels[0, 0], pixels[w-1, 0], pixels[0, h-1], pixels[w-1, h-1]]
print("Corner pixels:", corner_pixels)

# Check bounding box of non-white pixels
# A pixel is non-white if any RGB < 250
bbox_left = w
bbox_top = h
bbox_right = 0
bbox_bottom = 0

for y in range(h):
    for x in range(w):
        r, g, b = pixels[x, y]
        if r < 245 or g < 245 or b < 245:
            if x < bbox_left: bbox_left = x
            if x > bbox_right: bbox_right = x
            if y < bbox_top: bbox_top = y
            if y > bbox_bottom: bbox_bottom = y

print(f"Content bbox: left={bbox_left}, top={bbox_top}, right={bbox_right}, bottom={bbox_bottom}, width={bbox_right - bbox_left}, height={bbox_bottom - bbox_top}")

# Also check circular emblem bbox separately:
# Let's find where the circular badge is vs text below
# The circular badge is in the upper portion
