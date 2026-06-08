import os
import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

missing = []

for match in re.findall(r'src="([^"]+)"', html):
    if match == "script.js":
        continue
    if not os.path.exists(match):
        missing.append(match)

for match in re.findall(r'url\(\'([^\']+)\'\)', html):
    if not os.path.exists(match):
        missing.append(match)

print("Missing:", missing)
