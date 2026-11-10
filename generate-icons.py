from PIL import Image, ImageDraw
import os

src = Image.open("icon-source.png").convert("RGBA")
w, h = src.size
side = min(w, h)
left = (w - side) // 2
top = (h - side) // 2
src = src.crop((left, top, left + side, top + side))


def make_round(img):
    size = img.size
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)
    out = Image.new("RGBA", size, (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


mipmap_sizes = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192,
}

base = "android/app/src/main/res"
for folder, size in mipmap_sizes.items():
    dir_path = os.path.join(base, folder)
    os.makedirs(dir_path, exist_ok=True)
    square = src.resize((size, size), Image.LANCZOS)
    round_icon = make_round(square)
    square.save(os.path.join(dir_path, "ic_launcher.png"))
    round_icon.save(os.path.join(dir_path, "ic_launcher_round.png"))
    square.save(os.path.join(dir_path, "ic_launcher_foreground.png"))
    print(f"Wrote icons to {dir_path} at {size}px")
