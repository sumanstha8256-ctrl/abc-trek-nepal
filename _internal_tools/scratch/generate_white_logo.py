import os, math
from PIL import Image

src_path = r"C:\Users\user\.gemini\antigravity-ide\brain\abf1610e-f8e3-41a6-ac41-ffa3516aa03e\.user_uploaded\media_1788835189229.jpg"
out_dir = r"c:\Users\user\Downloads\ABC Trek Website\images"

img = Image.open(src_path).convert("RGBA")
pixels = img.load()

cx, cy, r_val = 520.0, 461.5, 146.5
crop_box = (195, 310, 845, 720)
crop_w = crop_box[2] - crop_box[0]
crop_h = crop_box[3] - crop_box[1]

white_img = Image.new("RGBA", (crop_w, crop_h), (255, 255, 255, 0))
white_pix = white_img.load()

for y in range(crop_h):
    for x in range(crop_w):
        orig_x = crop_box[0] + x
        orig_y = crop_box[1] + y
        r, g, b, _ = pixels[orig_x, orig_y]
        
        # Circle emblem area
        dist = math.hypot(orig_x - cx, orig_y - cy)
        if dist <= r_val:
            white_pix[x, y] = (r, g, b, 255)
        elif dist <= r_val + 1.2:
            alpha = int(255 * (r_val + 1.2 - dist) / 1.2)
            white_pix[x, y] = (r, g, b, max(0, min(255, alpha)))
        else:
            # Text area
            if orig_y >= 612:
                lum = 0.299*r + 0.587*g + 0.114*b
                if lum > 248:
                    white_pix[x, y] = (255, 255, 255, 0)
                else:
                    # White letters on dark background
                    alpha = int(255 * (255 - lum) / (255 - 60))
                    alpha = max(0, min(255, alpha))
                    white_pix[x, y] = (255, 255, 255, alpha)
            else:
                white_pix[x, y] = (0, 0, 0, 0)

white_img.save(os.path.join(out_dir, "logo-full-white.png"), "PNG")
print("Saved logo-full-white.png:", white_img.size)
