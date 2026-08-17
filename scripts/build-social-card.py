#!/usr/bin/env python3
"""Build the exact-size social card from a background and the project logo."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


CARD_SIZE = (1280, 640)


def fit_cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    source_ratio = image.width / image.height
    target_ratio = size[0] / size[1]
    if source_ratio > target_ratio:
        height = size[1]
        width = round(height * source_ratio)
    else:
        width = size[0]
        height = round(width / source_ratio)
    resized = image.resize((width, height), Image.Resampling.LANCZOS)
    left = (width - size[0]) // 2
    top = (height - size[1]) // 2
    return resized.crop((left, top, left + size[0], top + size[1]))


def load_font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size=size)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--background", required=True, type=Path)
    parser.add_argument("--logo", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    background = Image.open(args.background).convert("RGB")
    background = fit_cover(background, CARD_SIZE)
    background = ImageEnhance.Contrast(background).enhance(1.08)
    background = ImageEnhance.Color(background).enhance(0.92)

    card = background.convert("RGBA")

    # Increase foreground readability while preserving the generated voxel light.
    shade = Image.new("RGBA", CARD_SIZE, (0, 0, 0, 0))
    shade_pixels = shade.load()
    for x in range(CARD_SIZE[0]):
        alpha = int(122 - (x / CARD_SIZE[0]) * 46)
        for y in range(CARD_SIZE[1]):
            shade_pixels[x, y] = (2, 9, 22, max(58, alpha))
    card = Image.alpha_composite(card, shade)

    logo = Image.open(args.logo).convert("RGBA")
    logo_width = 690
    logo_height = round(logo.height * logo_width / logo.width)
    logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)

    shadow = Image.new("RGBA", CARD_SIZE, (0, 0, 0, 0))
    shadow.paste(logo, (40, 144), logo)
    shadow = shadow.filter(ImageFilter.GaussianBlur(16))
    shadow_alpha = shadow.getchannel("A").point(lambda value: int(value * 0.55))
    shadow.putalpha(shadow_alpha)
    card = Image.alpha_composite(card, shadow)
    card.alpha_composite(logo, (40, 128))

    draw = ImageDraw.Draw(card)
    font_dir = Path("C:/Windows/Fonts")
    eyebrow_font = load_font(font_dir / "seguisb.ttf", 27)
    headline_font = load_font(font_dir / "segoeuib.ttf", 51)
    detail_font = load_font(font_dir / "segoeui.ttf", 25)

    text_x = 760
    draw.text(
        (text_x, 185),
        "STANDALONE META QUEST",
        font=eyebrow_font,
        fill=(255, 211, 42, 255),
        stroke_width=1,
        stroke_fill=(40, 24, 0, 220),
    )
    draw.multiline_text(
        (text_x, 235),
        "No gaming PC\nrequired.",
        font=headline_font,
        fill=(247, 251, 255, 255),
        spacing=2,
        stroke_width=1,
        stroke_fill=(0, 8, 20, 220),
    )
    draw.multiline_text(
        (text_x, 385),
        "Quest-native launcher\nOpenXR • Tracked controls",
        font=detail_font,
        fill=(173, 197, 224, 255),
        spacing=5,
    )
    draw.rounded_rectangle(
        (text_x, 472, 955, 521),
        radius=13,
        fill=(255, 211, 42, 255),
    )
    draw.text(
        (text_x + 20, 481),
        "PUBLIC BETA",
        font=eyebrow_font,
        fill=(5, 18, 38, 255),
    )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    card.convert("RGB").save(
        args.out,
        format="JPEG",
        quality=90,
        optimize=True,
        progressive=True,
    )


if __name__ == "__main__":
    main()
