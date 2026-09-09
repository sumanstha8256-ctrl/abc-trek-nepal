from PIL import Image

logo = Image.open(r"c:\Users\user\Downloads\ABC Trek Website\images\logo.png")

# Save multi-size favicon.ico
logo.save(r"c:\Users\user\Downloads\ABC Trek Website\favicon.ico", format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
print("Saved favicon.ico")

# Save 64x64 and 192x192 favicon.png
fav64 = logo.resize((64, 64), Image.Resampling.LANCZOS)
fav64.save(r"c:\Users\user\Downloads\ABC Trek Website\images\favicon.png", "PNG")

fav192 = logo.resize((192, 192), Image.Resampling.LANCZOS)
fav192.save(r"c:\Users\user\Downloads\ABC Trek Website\images\apple-touch-icon.png", "PNG")
print("Saved images/favicon.png and images/apple-touch-icon.png")
