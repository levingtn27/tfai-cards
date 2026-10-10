#!/usr/bin/env python3
"""Render a Talents for AI job card (1080x1080 PNG).
Usage: python3 tools/make_card.py spec.json out.png
spec.json: {"title": "...", "flags": [["ca","Canada"],["za","South Africa"]], "pay": "up to $23/h", "sub": "Remote · via SME Careers"}
Flag codes are ISO 3166-1 alpha-2 (flat SVGs from the flag-icons npm package; run `npm i flag-icons` inside tools/ first).
Labels may contain <br> for a second line (e.g. per-language pay).
"""
import json, os, sys
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
FLAGS = os.path.join(HERE, "node_modules", "flag-icons", "flags", "4x3")

def layout(n):
    if n <= 4:  return dict(w=190, h=142, gap="26px 56px", lab=32, title=108, pay=124)
    if n <= 8:  return dict(w=170, h=128, gap="26px 44px", lab=30, title=92,  pay=110)
    return dict(w=130, h=98, gap="18px 34px", lab=26, title=84, pay=100)

def build_html(spec):
    L = layout(len(spec.get("flags", [])))
    flags = "".join(
        f'<div style="text-align:center"><img src="file://{FLAGS}/{c}.svg" style="width:{L["w"]}px;height:{L["h"]}px;border-radius:14px;box-shadow:0 0 0 2px #e3e3e3;object-fit:cover">'
        f'<div style="font-size:{L["lab"]}px;color:#555;margin-top:10px">{n}</div></div>'
        for c, n in spec.get("flags", []))
    flag_row = f'<div style="display:flex;gap:{L["gap"]};justify-content:center;flex-wrap:wrap;width:900px">{flags}</div>' if flags else ""
    return f'''<html><body style="margin:0;width:1080px;height:1080px;background:#fff;font-family:Inter,'Helvetica Neue',Arial,sans-serif;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:80px 60px;box-sizing:border-box;text-align:center">
<div style="font-weight:800;font-size:{L["title"]}px;line-height:1.03;letter-spacing:-3px;color:#0a0a0a">{spec["title"]}</div>
{flag_row}
<div style="font-weight:800;font-size:{L["pay"]}px;letter-spacing:-3px;color:#4f2bd9">{spec["pay"]}</div>
<div style="font-size:38px;color:#666">{spec.get("sub","Remote")}</div>
<div style="font-weight:700;font-size:34px;color:#111">talentsforai.com</div></body></html>'''

def render(spec, out):
    html_path = out + ".html"
    open(html_path, "w").write(build_html(spec))
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1080})
        pg.goto("file://" + os.path.abspath(html_path))
        pg.screenshot(path=out)
        b.close()
    os.remove(html_path)

if __name__ == "__main__":
    render(json.load(open(sys.argv[1])), sys.argv[2])
