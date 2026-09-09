from PIL import Image
from collections import deque

img_path = r"C:\Users\user\.gemini\antigravity-ide\brain\abf1610e-f8e3-41a6-ac41-ffa3516aa03e\.user_uploaded\media_1788835189229.jpg"
img = Image.open(img_path).convert("RGBA")
w, h = img.size
pixels = img.load()

# We want to identify the exterior background via flood-fill / BFS from borders.
# A pixel is considered background if it is reachable from the border through white/near-white pixels.
# Let's define threshold:
# If RGB is >= 250, it is pure background white.
# Also we can handle anti-aliasing near the boundary!

visited = [[False]*w for _ in range(h)]
queue = deque()

# Initialize queue with boundary pixels
for x in range(w):
    queue.append((x, 0))
    queue.append((x, h-1))
    visited[0][x] = True
    visited[h-1][x] = True

for y in range(h):
    queue.append((0, y))
    queue.append((w-1, y))
    visited[y][0] = True
    visited[y][w-1] = True

# BFS to flood fill external background
# Threshold: how white a pixel must be to be part of the external background
# In JPEG compression, white background might have slight artifacts, e.g. 245-255
while queue:
    x, y = queue.popleft()
    r, g, b, a = pixels[x, y]
    
    # Check 4 neighbors
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx]:
            nr, ng, nb, _ = pixels[nx, ny]
            # If it's near white background:
            # Let's say all channels > 242
            if nr > 242 and ng > 242 and nb > 242:
                visited[ny][nx] = True
                queue.append((nx, ny))

# Now visited[y][x] == True are the exterior background pixels.
# Let's compute alpha for anti-aliasing:
# If visited[y][x] is True:
# If nr, ng, nb are all 255 -> alpha = 0
# If nr, ng, nb are between 230 and 255, we can feather alpha based on distance to dark pixel or luminance
out_img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
out_pixels = out_img.load()

for y in range(h):
    for x in range(w):
        r, g, b, _ = pixels[x, y]
        if visited[y][x]:
            # Exterior background
            # Check how close to 255
            min_val = min(r, g, b)
            if min_val >= 253:
                out_pixels[x, y] = (r, g, b, 0)
            else:
                # Feathering at boundary
                alpha = int(255 * (255 - min_val) / (255 - 242))
                alpha = max(0, min(255, alpha))
                out_pixels[x, y] = (r, g, b, alpha)
        else:
            out_pixels[x, y] = (r, g, b, 255)

# Find bounding box of non-transparent content
bbox = out_img.getbbox()
print("Full logo bounding box with transparent background:", bbox)

# Crop to bounding box with 10px padding
pad = 10
cropped_bbox = (
    max(0, bbox[0] - pad),
    max(0, bbox[1] - pad),
    min(w, bbox[2] + pad),
    min(h, bbox[3] + pad)
)
cropped_logo = out_img.crop(cropped_bbox)
cropped_logo.save(r"c:\Users\user\Downloads\ABC Trek Website\images\logo-full.png", "PNG")
print("Saved logo-full.png size:", cropped_logo.size)
