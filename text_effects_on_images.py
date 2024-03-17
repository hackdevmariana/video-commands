from PIL import Image, ImageDraw, ImageFont, ImageFilter

effects_available = [
    'shadow',
    'emboss',
    'enhance',
    'relief',
]

def apply_effect(draw, font_size, effect):
    """ Applies the selected effect to the text."""

    if effect.lower() not in effects_available:
        return draw
    if effect.lower() == 'shadow':
        draw = shadow(draw, font_size)
    elif effect.lower() == 'emboss':
        draw = emboss(draw, font_size)
    elif effect.lower() == 'enhance':
        draw = enhance(draw, font_size)
    elif effect.lower() == 'relief':
        draw = relief(draw, font_size)

    return draw


def relief(img, font_size):
    """Applies a relief effect to the received text."""
    shadow_layer = Image.new("RGBA", img.size)
    color_shadow = (0, 0, 0)

    for x in range(img.width):
        for y in range(img.height):
            current_pixel = img.getpixel((x, y))
            new_pixel = current_pixel if current_pixel[3] == 0 else color_shadow + (current_pixel[3],)
            shadow_layer.putpixel((x, y), new_pixel)
    if font_size // 20 > 4:
        offset = (-1 * (font_size // 20), -1 * (font_size // 20))
    else:
        offset = (-4, -4)
    print(font_size)
    print(offset)
    shadow_layer.paste(img, offset, img)
    return shadow_layer

def shadow(img, font_size):
    """Applies a shadow effect to the received text."""
    shadow_layer = Image.new("RGBA", img.size)
    color_shadow = (0, 0, 0)

    for x in range(img.width):
        for y in range(img.height):
            current_pixel = img.getpixel((x, y))
            new_pixel = current_pixel if current_pixel[3] == 0 else color_shadow + (current_pixel[3],)
            shadow_layer.putpixel((x, y), new_pixel)
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=5))
    if font_size // 20 > 4:
        offset = (-1 * (font_size // 20), -1 * (font_size // 20))
    else:
        offset = (-4, -4)
    print(font_size)
    print(offset)
    shadow_layer.paste(img, offset, img)
    return shadow_layer

def emboss(img, font_size):
    """Applies a emboss effect to the received text."""
    emboss_layer = img
    emboss_layer = emboss_layer.filter(ImageFilter.GaussianBlur(radius=5))
    if font_size // 30 > 4:
        offset = (font_size // 30, font_size // 30)
    else:
        offset = (4, 4)
    img.paste(emboss_layer, offset, emboss_layer)

    return img

def make_mask(img):
    mask = Image.new("RGBA", img.size)
    color_transparent = (255, 255, 255)
    color_visible = (0, 0, 0)

    for x in range(img.width):
        for y in range(img.height):
            current_pixel = img.getpixel((x, y))
            new_pixel = color_visible if current_pixel[3] == 0 else color_transparent + (current_pixel[3],)
            mask.putpixel((x, y), new_pixel)
    return mask

def make_transparent_mask(img):
    mask = Image.new("RGBA", img.size)
    color_visible = (0, 0, 0)
    bgcolor = (0, 0, 0, 0)

    for x in range(img.width):
        for y in range(img.height):
            current_pixel = img.getpixel((x, y))
            # Si el píxel es transparente, usa el color de fondo; de lo contrario, usa el color visible.
            new_pixel = bgcolor if current_pixel[3] == 0 else color_visible + (current_pixel[3],)
            mask.putpixel((x, y), new_pixel)
    return mask

def enhance(img, font_size):
    """Applies a enhance effect to the received text."""
    img.save('original.png')
    mask = make_transparent_mask(img)
    mask.save('mascara.png')

    enhance_layer = img.filter(ImageFilter.EMBOSS)

    enhance_layer = Image.composite(enhance_layer, Image.new('RGBA', enhance_layer.size, (0,0,0,0)), mask)

    return enhance_layer



def list_effects():
    """Shows the available effects."""
    print()
    print('emboss:\t\tApplies a emboss effect to the text.')
    print('enhance:\t\tApplies a enhance effect to the text.')
    print('shadow:\t\tApplies a shadow to the text.')
    print()
