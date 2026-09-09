from PIL import Image
import math

src = Image.open(r"C:\Users\user\.gemini\antigravity-ide\brain\abf1610e-f8e3-41a6-ac41-ffa3516aa03e\.user_uploaded\media_1788835189229.jpg").convert("RGBA")
pixels = src.load()

# Emblem bounding box was found: left=373, top=316, right=667, bottom=607
# Center is x=520, y=461.5
# Let's verify outer border of circle
# The dark ring of the circle:
# Let's find the exact radius along multiple angles (0, 45, 90, 135, etc.)

cx = 520.0
cy = 461.5

radii = []
for angle_deg in range(0, 360, 5):
    rad = math.radians(angle_deg)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)
    # march from center outwards until dark border transitions back to white
    # The outer circle has dark ring. Let's find outermost pixel with dark color (e.g. luminance < 200)
    outer_r = None
    for r in range(160, 130, -1):
        x = int(cx + r * cos_a)
        y = int(cy + r * sin_a)
        if 0 <= x < src.width and 0 <= y < src.height:
            cr, cg, cb, _ = pixels[x, y]
            # If not background white
            if cr < 220 or cg < 220 or cb < 220:
                outer_r = r
                break
    if outer_r:
        radii.append(outer_r)

avg_radius = sum(radii) / len(radii)
min_radius = min(radii)
max_radius = max(radii)
print(f"Circle analysis: avg radius={avg_radius:.2f}, min={min_radius}, max={max_radius}")
