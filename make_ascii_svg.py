from PIL import Image, ImageOps, ImageEnhance
import html, sys
source = sys.argv[1] if len(sys.argv) > 1 else "portrait-source.jpg"
image = Image.open(source).convert("RGB")
gray = ImageEnhance.Contrast(ImageOps.autocontrast(ImageOps.grayscale(image), cutoff=2)).enhance(1.25)
width, height = 88, 70
small = gray.resize((width, height), Image.Resampling.LANCZOS)
ramp = " .`:-=+*cs#%@"
rows = ["".join(ramp[min(len(ramp)-1, int((255-small.getpixel((x,y)))/255*(len(ramp)-1)))] for x in range(width)).rstrip() for y in range(height)]
svg = '<svg xmlns="http://www.w3.org/2000/svg" width="720" height="600" viewBox="0 0 720 600"><rect width="720" height="600" rx="14" fill="#050805"/><text x="16" y="22" fill="#c8ff3d" font-family="monospace" font-size="13">sharon@github:~$ ./portrait.sh</text><g fill="#c8ff3d" font-family="monospace" font-size="7.8" xml:space="preserve">'
for i, row in enumerate(rows):
    svg += f'<text x="10" y="{42+i*7.8}">{html.escape(row)}<animate attributeName="opacity" values="0;1" dur=".18s" begin="{i*.06:.2f}s" fill="freeze"/></text>'
svg += '</g><rect x="1" y="1" width="718" height="598" rx="14" fill="none" stroke="#c8ff3d" stroke-opacity=".35"/></svg>'
open("sharon-ascii.svg", "w", encoding="utf-8").write(svg)
