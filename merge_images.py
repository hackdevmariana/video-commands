#!/usr/bin/env python3

from itertools import permutations
from pathlib import Path
import os
from PIL import Image, ImageChops

def shuffle_channels(image_1, image_2):
    if os.path.isfile(image_1) and os.path.isfile(image_2):
        img_1 = Image.open(image_1)
        img_2 = Image.open(image_2)

        if img_1.mode != 'RGB':
            img_1 = img_1.convert('RGB')
        if img_2.mode != 'RGB':
            img_2 = img_2.convert('RGB')

        if img_1.size != img_2.size:
            img_2 = img_2.resize(img_1.size)

        r_1, g_1, b_1 = img_1.split()
        r_2, g_2, b_2 = img_2.split()

        channels = [r_1, g_1, b_1, r_2, g_2, b_2]
        channels_strings = ['r_1', 'g_1', 'b_1', 'r_2', 'g_2', 'b_2']
        channel_combinations = list(permutations(channels, 3))
        combinations_strings = list(permutations(channels_strings, 3))

        for i, combination in enumerate(channel_combinations):
            image = Image.merge("RGB", combination)
            combination_string = "_".join(combinations_strings[i])
            output = f"{Path(image_1).stem}_{Path(image_2).stem}_comb_{combination_string}.png"
            image.save(output)

def blend_images(image_1, image_2):
    if os.path.isfile(image_1) and os.path.isfile(image_2):
        img_1 = Image.open(image_1)
        img_2 = Image.open(image_2)

        if img_1.mode != 'RGB':
            img_1 = img_1.convert('RGB')
        if img_2.mode != 'RGB':
            img_2 = img_2.convert('RGB')

        if img_1.size != img_2.size:
            img_2 = img_2.resize(img_1.size)

        blended_image = Image.blend(img_1, img2, alpha=0.5)

        output = f"{Path(image_1).stem}_{Path(image_2).stem}_blended.png"
        blended_image.save(output)

def with_mask(image_1, image_2, image_mask):
    if os.path.isfile(image_1) and os.path.isfile(image_2) and os.path.isfile(image_mask):
        img_1 = Image.open(image_1)
        img_2 = Image.open(image_2)
        mask = Image.open(image_mask)

        if img_1.mode != 'RGB':
            img_1 = img_1.convert('RGB')
        if img_2.mode != 'RGB':
            img_2 = img_2.convert('RGB')
        if mask.mode != 'L':
            mask = mask.convert('L')

        if img_1.size != img_2.size:
            img_2 = img_2.resize(img_1.size)
        if img_1.size != mask.size:
            mask = mask.resize(img_1.size)

        # Crear la imagen compuesta utilizando la máscara
        composite_image = Image.composite(img_1, img_2, mask)

        # Generar el nombre de salida y guardar la imagen compuesta
        output = f"{Path(image_1).stem}_{Path(image_2).stem}__mask_{Path(image_mask).stem}.png"
        composite_image.save(output)

def combine_images(image_1, image_2, image_mask):
    if os.path.isfile(image_1) and os.path.isfile(image_2):
        img_1 = Image.open(image_1)
        img_2 = Image.open(image_2)
        mask = Image.open(image_mask)

        if img_1.mode != 'RGB':
            img_1 = img_1.convert('RGB')
        if img_2.mode != 'RGB':
            img_2 = img_2.convert('RGB')
        if mask.mode != 'L':
            mask = mask.convert('L')

        if img_1.size != img_2.size:
            img_2 = img_2.resize(img_1.size)
        if img_1.size != mask.size:
            mask = mask.resize(img_1.size)

        # ImageChops.add
        add_image = ImageChops.add(img_1, img_2)
        output = f"{Path(image_1).stem}_{Path(image_2).stem}_add.png"
        add_image.save(output)

        # ImageChops.add_modulo
        add_image = ImageChops.add_modulo(img_1, img_2)
        output = f"{Path(image_1).stem}_{Path(image_2).stem}_add_modulo.png"
        add_image.save(output)

        # ImageChops.blend
        add_image = ImageChops.blend(img_1, img_2, 0.5)
        output = f"{Path(image_1).stem}_{Path(image_2).stem}_blend.png"
        add_image.save(output)

        # ImageChops.composite
        add_image = ImageChops.composite(img_1, img_2, mask)
        output = f"{Path(image_1).stem}_{Path(image_2).stem}_composite.png"
        add_image.save(output)

        # ImageChops.darker
        add_image = ImageChops.darker(img_1, img_2)
        output = f"{Path(image_1).stem}_{Path(image_2).stem}_darker.png"
        add_image.save(output)

        # ImageChops.difference
        add_image = ImageChops.difference(img_1, img_2)
        output = f"{Path(image_1).stem}_{Path(image_2).stem}_difference.png"
        add_image.save(output)

        # ImageChops.lighter
        add_image = ImageChops.lighter(img_1, img_2)
        output = f"{Path(image_1).stem}_{Path(image_2).stem}_lighter.png"
        add_image.save(output)

        # ImageChops.multiply
        add_image = ImageChops.multiply(img_1, img_2)
        output = f"{Path(image_1).stem}_{Path(image_2).stem}_multiply.png"
        add_image.save(output)

        # ImageChops.soft_light
        add_image = ImageChops.soft_light(img_1, img_2)
        output = f"{Path(image_1).stem}_{Path(image_2).stem}_soft_light.png"
        add_image.save(output)

        # ImageChops.hard_light
        add_image = ImageChops.hard_light(img_1, img_2)
        output = f"{Path(image_1).stem}_{Path(image_2).stem}_hard_light.png"
        add_image.save(output)

        # ImageChops.overlay
        add_image = ImageChops.overlay(img_1, img_2)
        output = f"{Path(image_1).stem}_{Path(image_2).stem}_overlay.png"
        add_image.save(output)

        # ImageChops.screen
        add_image = ImageChops.screen(img_1, img_2)
        output = f"{Path(image_1).stem}_{Path(image_2).stem}_screen.png"
        add_image.save(output)

        # ImageChops.subtract
        add_image = ImageChops.subtract(img_1, img_2)
        output = f"{Path(image_1).stem}_{Path(image_2).stem}_subtract.png"
        add_image.save(output)

        # ImageChops.subtract_modulo
        add_image = ImageChops.subtract_modulo(img_1, img_2)
        output = f"{Path(image_1).stem}_{Path(image_2).stem}_subtract_modulo.png"
        add_image.save(output)

if __name__ == '__main__':
    image_1 = 'image.jpeg'
    image_2 = 'image.png'
    image_mask = 'mask.png'
    combine_images(image_1, image_2, image_mask)
