import os, math
from PIL import Image

src_path = r"C:\Users\user\.gemini\antigravity-ide\brain\abf1610e-f8e3-41a6-ac41-ffa3516aa03e\.user_uploaded\media_1788835189229.jpg"
out_dir = r"c:\Users\user\Downloads\ABC Trek Website\images"
os.makedirs(out_dir, exist_ok=True)

img = Image.open(src_path).convert("RGBA")
pixels = img.load()

# -------------------------------------------------------------
# 1. GENERATE PRISTINE CIRCULAR EMBLEM (logo.png & logo-emblem.png)
# -------------------------------------------------------------
# Circle center: x=520.0, y=461.5, radius=146.5
cx, cy, r_val = 520.0, 461.5, 146.5
size = 320
emblem_img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
emb_pix = emblem_img.load()

offset_x = cx - size / 2.0
offset_y = cy - size / 2.0

for y in range(size):
    for x in range(size):
        sx = int(offset_x + x)
        sy = int(offset_y + y)
        if 0 <= sx < img.width and 0 <= sy < img.height:
            dist = math.hypot(sx - cx, sy - cy)
            r, g, b, _ = pixels[sx, sy]
            if dist <= r_val - 1.0:
                emb_pix[x, y] = (r, g, b, 255)
            elif dist <= r_val + 1.0:
                # Anti-aliased alpha
                alpha = int(255 * (r_val + 1.0 - dist) / 2.0)
                emb_pix[x, y] = (r, g, b, max(0, min(255, alpha)))
            else:
                emb_pix[x, y] = (0, 0, 0, 0)

# Save circular emblem
emblem_img.save(os.path.join(out_dir, "logo.png"), "PNG")
emblem_img.save(os.path.join(out_dir, "logo-emblem.png"), "PNG")
print("1. Saved logo.png and logo-emblem.png:", emblem_img.size)

# -------------------------------------------------------------
# 2. GENERATE CLEAN FULL LOGO (logo-full.png)
# -------------------------------------------------------------
# Crop bounds: x from 195 to 845, y from 310 to 720
# For pixels outside the circle and outside text, make pure white transparent
# Outside circle: dist > 147.5
# In text region: luminance-based alpha or background removal
crop_box = (195, 310, 845, 720)
crop_w = crop_box[2] - crop_box[0]
crop_h = crop_box[3] - crop_box[1]

full_img = Image.new("RGBA", (crop_w, crop_h), (255, 255, 255, 0))
full_pix = full_img.load()

for y in range(crop_h):
    for x in range(crop_w):
        orig_x = crop_box[0] + x
        orig_y = crop_box[1] + y
        r, g, b, _ = pixels[orig_x, orig_y]
        
        # Check if inside circle
        dist = math.hypot(orig_x - cx, orig_y - cy)
        if dist <= r_val:
            # Inside circle -> keep exact colors
            full_pix[x, y] = (r, g, b, 255)
        elif dist <= r_val + 1.2:
            alpha = int(255 * (r_val + 1.2 - dist) / 1.2)
            full_pix[x, y] = (r, g, b, max(0, min(255, alpha)))
        else:
            # Outside circle: in the text region (or white space between)
            # If it's the text below (y > 610)
            if orig_y >= 612:
                # Text is navy blue (#053063)
                # Background is white (255, 255, 255)
                # Luminance: 0.299*R + 0.587*G + 0.114*B
                lum = 0.299*r + 0.587*g + 0.114*b
                if lum > 248:
                    full_pix[x, y] = (r, g, b, 0)
                else:
                    # Alpha inversely proportional to whiteness
                    alpha = int(255 * (255 - lum) / (255 - 60))
                    alpha = max(0, min(255, alpha))
                    # Color should be the brand dark navy #0A2F5E
                    full_pix[x, y] = (r, g, b, alpha)
            else:
                # Between circle and text -> transparent
                full_pix[x, y] = (0, 0, 0, 0)

full_img.save(os.path.join(out_dir, "logo-full.png"), "PNG")
print("2. Saved logo-full.png:", full_img.size)

# Also generate a crisp full logo with white background for opengraph / schema / share
full_white_bg = Image.new("RGB", (crop_w, crop_h), (255, 255, 255))
for y in range(crop_h):
    for x in range(crop_w):
        full_white_bg.putpixel((x, y), pixels[crop_box[0] + x, crop_box[1] + y][:3])
full_white_bg.save(os.path.join(out_dir, "logo-card.jpg"), "JPEG", quality=95)
print("3. Saved logo-card.jpg:", full_white_bg.size)
