from PIL import Image, ImageOps
import math

img_path = r"C:\Users\user\.gemini\antigravity-ide\brain\abf1610e-f8e3-41a6-ac41-ffa3516aa03e\.user_uploaded\media_1788835189229.jpg"
img = Image.open(img_path).convert("RGBA")

# Let's find exact center and radius of outer circle
# The emblem bbox was: left=373, top=316, right=667, bottom=607
# width = 667 - 373 + 1 = 295
# height = 607 - 316 + 1 = 292
# center_x = (373 + 667) / 2 = 520.0
# center_y = (316 + 607) / 2 = 461.5
# radius = (295 + 292) / 4 = 146.75

cx = 520.0
cy = 461.5
radius = 147.0

print(f"Calculated Circle: Center=({cx}, {cy}), Radius={radius}")

# Let's crop the emblem into a square of size (2*radius + 20) with transparent background
size = int(radius * 2 + 16) # ~310x310
emblem = Image.new("RGBA", (size, size), (255, 255, 255, 0))

src_pixels = img.load()
emb_pixels = emblem.load()

offset_x = cx - size / 2.0
offset_y = cy - size / 2.0

for y in range(size):
    for x in range(size):
        src_x = int(offset_x + x)
        src_y = int(offset_y + y)
        if 0 <= src_x < img.width and 0 <= src_y < img.height:
            # distance from center
            dist = math.hypot(src_x - cx, src_y - cy)
            r, g, b, a = src_pixels[src_x, src_y]
            
            # Anti-aliased circle edge
            if dist <= radius - 1.0:
                emb_pixels[x, y] = (r, g, b, 255)
            elif dist <= radius + 1.0:
                # smooth alpha falloff
                alpha = int(255 * (radius + 1.0 - dist) / 2.0)
                emb_pixels[x, y] = (r, g, b, alpha)
            else:
                emb_pixels[x, y] = (0, 0, 0, 0)

import os
os.makedirs(r"c:\Users\user\Downloads\ABC Trek Website\images", exist_ok=True)
emblem.save(r"c:\Users\user\Downloads\ABC Trek Website\images\logo-emblem.png", "PNG")
print("Saved logo-emblem.png successfully. Size:", emblem.size)
