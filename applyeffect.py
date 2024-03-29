#!/usr/bin/env python3

from pathlib import Path

import click
import colorama
import gmic
import glob
import os
import PIL.Image
import shutil
import subprocess


from PIL import ImageChops, Image

from video_commands_lib import random_filename

effects = [
            'blur',
            'blurx',
            'blury',
            'oldphoto',
            'newspaperdotted',
            'judgment',
            'polaroid',
            'oilpainting',
            'cartoon',
            'posterize',
            'doodlepen',
            'smooth',
            'stencil',
            'tetris',
            'weave',
            'cracks',
            'scanlines',
            'badprinter',
            'telesketch',
            'badtonner',
            'deriche',
            'blackembossed',
            'luminance',
            'gaussiandog',
            'erode',
            'inpaint',
            'kuwahara',
            'normalizelocal',
            'oldgame',
            'removepixels',
            'glitteronblack',
            'emanation',
            'sponged',
            'markerpen',
            'polygonize',
            'pendrawing',
            'boxfitting',
            'drawwhirl',
            'cubism',
            'halftone',
            'mosaic',
            'thickstroke',
            'frameblur',
            'puzzle',
            'arrayfade',
            'tiles',
            'tunnel',
            'framepainting',
            'colorabstraction',
            'portraitbw',
            'glow',
            'retrofade',
            'clarify',
            'glass',
            'spherize',
            'water',
            'wave',
            'dirty',
            'details',
            'mightydetails',
            'fxglow',
            'lomo',
            'noiseperlin',
            'circles',
            'shapeism',
            'starrynight',
            'yellowredblue',
            'graytree',
            'sharpen',
            'reddens',
            'grid',
            'littlebayatlaciotat',
            'leviaducalestaque',
            'summertime9a',
            'convergence',
            'irises',
            'themandola',
            'orientalgarden',
            'squarescircles',
            'kairouan',
            'polyphony2',
            'summer',
            'portrait',
            'redtree',
            'redwaistcoat',
            'ebro',
            'blossom',
            'landscape',
            'wheatfield',]

@click.group()
def cli():
    pass

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=2, help='Blur intensity')
def blur(input, output, intensity):
    """Applies blur effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_blurred.png"

    gmic.run(f'{input} blur {intensity} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=20, help='Blur intensity')
def blurx(input, output, intensity):
    """Applies blur effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_blurred_x.png"

    gmic.run(f'{input} blur_x {intensity} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=20, help='Blur intensity')
def blury(input, output, intensity):
    """Applies blur effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_blurred_y.png"

    gmic.run(f'{input} blur_y {intensity} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def oldphoto(input, output):
    """Applies old photo effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_old_photo.png"

    gmic.run(f'{input} old_photo output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def newspaperdotted(input, output):
    """Applies newspaper dotted effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_newspaper_dotted.png"

    temp_file = random_filename()
    gmic.run(f'{input} cartoon 1,50,30,0.75,5,26 output {temp_file}')

    img_1 = Image.open(input)
    img_2 = Image.open(temp_file)

    max_width = max(img_1.width, img_2.width)
    max_height = max(img_1.height, img_2.height)
    img_1 = img_1.resize((max_width, max_height))
    img_2 = img_2.resize((max_width, max_height))
    imagen1 = img_1.convert('1')
    imagen2 = img_2.convert('1')
    imagen_or = ImageChops.logical_or(imagen1, imagen2)
    imagen_or.save(output)
    os.remove(temp_file)

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def judgment(input, output):
    """Applies judgment draw effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_judgment_draw.png"

    gmic.run(f'{input} +sketchbw 20 reverse blur[-1] 3 blend[-2,-1] overlay gui_merge_layers output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def polaroid(input, output):
    """Applies polaroid effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_polaroid.png"

    gmic.run(f'{input} to_rgba polaroid 5,30 output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def oilpainting(input, output):
    """Applies oil painting effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_oil_painting.png"

    gmic.run(f'{input} fx_vector_painting 9.5,0 output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def cartoon(input, output):
    """Applies cartoon effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_cartoon.png"

    gmic.run(f'{input} cartoon 1,50,30,0.75,5,26 output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def posterize(input, output):
    """Applies posterize effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_posterize.png"

    gmic.run(f'{input} fx_posterize 8,8,1,5,0,0,1,0 output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def doodlepen(input, output):
    """Applies doodle pen effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_doodle_pen.png"

    gmic.run(f'{input} fx_feltpen 500,50,5,0.1,5,1,0 output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def smooth(input, output):
    """Applies smooth effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_smooth.png"

    gmic.run(f'{input} smooth 80,0,1,1,2 output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def stencil(input, output):
    """Applies stencil effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_stencil.png"

    gmic.run(f'{input} stencil 8,2,1 output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def tetris(input, output):
    """Applies tetris effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_tetris.png"

    gmic.run(f'{input} tetris 10 output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def weave(input, output):
    """Applies weave effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_weave.png"

    gmic.run(f'{input} weave , output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def cracks(input, output):
    """Applies cracks effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_cracks.png"

    gmic.run(f'{input} cracks 40,0,1,0 output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def scanlines(input, output):
    """Applies scanlines effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_scanlines.png"

    gmic.run(f'{input} scanlines , output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def badprinter(input, output):
    """Applies bad printer effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_bad_printer.png"

    temp_file = random_filename()
    gmic.run(f'{input} cartoon 1,20,30,0.75,5,26 scanlines , scanlines , output {temp_file}')

    img_1 = Image.open(input)
    img_2 = Image.open(temp_file)

    max_width = max(img_1.width, img_2.width)
    max_height = max(img_1.height, img_2.height)
    img_1 = img_1.resize((max_width, max_height))
    img_2 = img_2.resize((max_width, max_height))
    imagen1 = img_1.convert('1')
    imagen2 = img_2.convert('1')
    imagen_or = ImageChops.logical_or(imagen1, imagen2)
    imagen_or.save(output)
    os.remove(temp_file)

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def telesketch(input, output):
    """Applies telesketch effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_telesketch.png"

    instruction = "(0,1,0;1,-4,1;0,1,0) convolve[-2] [-1] keep[-2]"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def badtonner(input, output):
    """Applies badtonner effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_badtonner.png"

    instruction = "curvature"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def deriche(input, output):
    """Applies deriche effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_deriche.png"

    instruction = "deriche 1,1,x"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def blackembossed(input, output):
    """Applies blackembossed effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_blackembossed.png"

    instruction = "deriche 1,1,y"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def luminance(input, output):
    """Applies luminance effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_luminance.png"

    instruction = "luminance"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def gaussiandog(input, output):
    """Applies difference of gaussian effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_gaussiandog.png"

    instruction = "dog 1,7"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=5, help='Blur intensity')
def erode(input, output, intensity):
    """Applies erode effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_erode.png"

    instruction = "erode 5"
    gmic.run(f'{input} {instruction} {intensity} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def inpaint(input, output):
    """Applies inpaint effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_inpaint.png"

    instruction = "inpaint_holes 8,40,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=7, help='Blur intensity')
def kuwahara(input, output, intensity):
    """Applies Kuwahara filter effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_kuwahara.png"

    instruction = "kuwahara"
    gmic.run(f'{input} {instruction} {intensity} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def normalizelocal(input, output):
    """Applies normalize local filter to the received image."""

    if not output:
        output = f"{Path(input).stem}_normalize_local.png"

    instruction = "normalize_local 8,10"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def oldgame(input, output):
    """Applies 8 bits effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_oldgame.png"

    instruction = "fx_8bits 25,800,16,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=50, help='Blur intensity')
def removepixels(input, output, intensity):
    """Remove pixels to the received image."""

    if not output:
        output = f"{Path(input).stem}_remove_pixels.png"

    instruction = "remove_pixels"
    gmic.run(f'{input} {instruction} {intensity}% output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def glitteronblack(input, output):
    """Applies glitter on black to the received image."""

    if not output:
        output = f"{Path(input).stem}_glitter_on_black.png"

    instruction = "structuretensors abs pow 1.5"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def emanation(input, output):
    """Applies emanation effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_emanation.png"

    instruction = "100%,100% circle[-1] 50%,50%,25%,1,255 append c +solidify , gui_merge_layers"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def sponged(input, output):
    """Applies sponged effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_sponged.png"

    instruction = 'fx_lylejk_painting 10,2,4,10,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def markerpen(input, output):
    """Applies marker pen effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_marker_pen.png"

    instruction = 'fx_painting 5,2.5,1.5,5,1,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def polygonize(input, output):
    """Applies polygonize effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_polygonize.png"

    instruction = 'blur 1 fx_polygonize_delaunay 40,5,75,0.5,3,50,0,0,0,255,1,0,50,50'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def pendrawing(input, output):
    """Applies pen drawing effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_pendrawing.png"

    instruction = 'fx_sketchbw 3,45,180,30,1.75,0.02,0.5,0.75,0.1,0.7,3,6,0,1,4,0,0,50,50'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def boxfitting(input, output):
    """Applies boxfitting effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_boxfitting.png"

    instruction = 'boxfitting ,'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def drawwhirl(input, output):
    """Applies draw whirl effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_draw_whirl.png"

    instruction = 'draw_whirl ,'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def cubism(input, output):
    """Applies cubism effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_cubism.png"

    instruction = 'cubism ,'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def halftone(input, output):
    """Applies halftone effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_halftone.png"

    instruction = 'halftone ,'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def mosaic(input, output):
    """Applies mosaic effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_mosaic.png"

    instruction = 'mosaic , +fill "I!=J(1) || I!=J(0,1)?[0,0,0]:I" gui_merge_layers'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def thickstroke(input, output):
    """Applies thick stroke effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_thick_stroke.png"

    instruction = 'norm stencil. 2,1,4 +mul gui_merge_layers'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def frameblur(input, output):
    """Applies frame blur effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_frame_blur.png"

    instruction = 'fx_frame_blur 30,30,0,5,0,0,128,128,128,0,5,255,255,255,2,2,1,0,0.5,0.5,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def puzzle(input, output):
    """Applies puzzle effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_puzzle.png"

    instruction = 'fx_puzzle 5,5,0.5,0,0,0.3,100,0.2,255,100,0,0,0,0,0,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def arrayfade(input, output):
    """Applies array fade effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_array_fade.png"

    instruction = 'array_fade 2,2'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=50, help='Blur intensity')
def tiles(input, output, intensity):
    """Applies tiles effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_tiles.png"

    instruction = f'to_rgba rotate_tiles 10,{intensity} drop_shadow 10,10'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=50, help='Blur intensity')
def tunnel(input, output, intensity):
    """Applies tiles effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_tunnel.png"

    instruction = f'tunnel {intensity}'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def framepainting(input, output):
    """Frame painting to the received image."""

    if not output:
        output = f"{Path(input).stem}_frame_painting.png"

    instruction = 'frame_painting ,'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def colorabstraction(input, output):
    """Applies color abstraction to the received image."""

    if not output:
        output = f"{Path(input).stem}_color_abstraction.png"

    instruction = 'fx_color_abstraction 1,10,0.2,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def portraitbw(input, output):
    """Applies pencil portrait effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_pencil_portraitbw.png"

    instruction = 'fx_pencil_portraitbw 30,120,1,0.5,144,79,21,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=20, help='Blur intensity')
def glow(input, output, intensity):
    """Applies pencil portrait effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_glow.png"

    instruction = f'-glow {intensity}%'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def retrofade(input, output):
    """Applies color retrofade to the received image."""

    if not output:
        output = f"{Path(input).stem}_retrofade.png"

    instruction = 'fx_retrofade 20,6,40,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def clarify(input, output):
    """Applies clarify colors to the received image."""

    if not output:
        output = f"{Path(input).stem}_vintage.png"

    instruction = 'fx_retinex 75,16,1,1,1,5,15,80,250,0,50,50'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=20, help='Glass intensity')
def glass(input, output, intensity):
    """Applies glass texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_glass.png"

    instruction = f'fx_textured_glass {intensity},{intensity},1,1,0,2,0,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def spherize(input, output, intensity):
    """Applies spherize texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_spherize.png"

    instruction = f'fx_spherize 50,1,0,50,50,0,0,2,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def water(input, output):
    """Applies water texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_water.png"

    instruction = f'water ,'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def wave(input, output):
    """Applies wave texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_wave.png"

    instruction = f'wave ,'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=20, help='Glass intensity')
def dirty(input, output, intensity):
    """Applies dirt to the received image."""

    if not output:
        output = f"{Path(input).stem}_dirty.png"

    instruction = f'fx_dirty {intensity},1,0,0,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def details(input, output):
    """Applies color abstraction to the received image."""

    if not output:
        output = f"{Path(input).stem}_details.png"

    instruction = 'fx_freaky_details 2,10,1,11,0,32,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def mightydetails(input, output):
    """Applies mighty details to the received image."""

    if not output:
        output = f"{Path(input).stem}_mighty_details.png"

    instruction = 'fx_mighty_details 25,1,25,1,11,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def fxglow(input, output):
    """Applies fx glow to the received image."""

    if not output:
        output = f"{Path(input).stem}_fx_glow.png"

    instruction = 'fx_glow 6,7,0,0,50,50'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lomo(input, output):
    """Applies lomo to the received image."""

    if not output:
        output = f"{Path(input).stem}_lomo.png"

    instruction = 'fx_lomo 10,0,15,15'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def noiseperlin(input, output):
    """Applies fx glow to the received image."""

    if not output:
        output = f"{Path(input).stem}_noiseperlin.png"

    instruction = 'fx_noise_perlin 0,100,8,0,0,4,0,0,2,0,0,1,0,2,0,50,50'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def circles(input, output):
    """Applies circles to the received image."""

    if not output:
        output = f"{Path(input).stem}_circles.png"

    instruction = 'fx_shapes 1,16,10,2,5,106.8,2,0,0,1,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def shapeism(input, output):
    """Applies circles shapeism to the received image."""

    if not output:
        output = f"{Path(input).stem}_shapeism.png"

    instruction = 'fx_shapeism 2,7,0.38,0,1,5,32,8,3,1,5,0.5,1,0,0,0,255'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def starrynight(input, output):
    """Applies starrynight texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_starrynight.png"

    temp_files = random_filename()

    instruction = '_fx_stylize starrynight +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def yellowredblue(input, output):
    """Applies yellowredblue texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_yellowredblue.png"

    temp_files = random_filename()

    instruction = '_fx_stylize yellowredblue +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def graytree(input, output):
    """Applies graytree texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_graytree.png"

    temp_files = random_filename()

    instruction = '_fx_stylize graytree +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=300, help='Blur intensity')
def sharpen(input, output, intensity):
    """Applies sharpen to the received image."""

    if not output:
        output = f"{Path(input).stem}_sharpen.png"

    instruction = f'sharpen {intensity}'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def reddens(input, output):
    """Applies color abstraction to the received image."""

    if not output:
        output = f"{Path(input).stem}_reddens.png"

    instruction = 'fx_boost_chroma 90,0,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=20, help='Blur intensity')
def grid(input, output, intensity):
    """Convert the received image in grid."""

    if not output:
        output = f"{Path(input).stem}_grid.png"

    instruction = 'imagegrid'
    gmic.run(f'{input} {instruction} {intensity} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")




@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def littlebayatlaciotat(input, output):
    """Applies littlebayatlaciotat texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_littlebayatlaciotat.png"

    temp_files = random_filename()

    instruction = '_fx_stylize littlebayatlaciotat +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def leviaducalestaque(input, output):
    """Applies leviaducalestaque texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_leviaducalestaque.png"

    temp_files = random_filename()

    instruction = '_fx_stylize leviaducalestaque +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def summertime9a(input, output):
    """Applies summertime9a texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_summertime9a.png"

    temp_files = random_filename()

    instruction = '_fx_stylize summertime9a +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def convergence(input, output):
    """Applies convergence texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_convergence.png"

    temp_files = random_filename()

    instruction = '_fx_stylize convergence +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def irises(input, output):
    """Applies irises texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_irises.png"

    temp_files = random_filename()

    instruction = '_fx_stylize irises +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def themandola(input, output):
    """Applies themandola texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_themandola.png"

    temp_files = random_filename()

    instruction = '_fx_stylize themandola +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def orientalgarden(input, output):
    """Applies oriental pleasure garden anagoria texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_orientalpleasuregardenanagoria.png"

    temp_files = random_filename()

    instruction = '_fx_stylize orientalpleasuregardenanagoria +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def squarescircles(input, output):
    """Applies squares with concentric circles texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_squareswithconcentriccircles.png"

    temp_files = random_filename()

    instruction = '_fx_stylize squareswithconcentriccircles +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def kairouan(input, output):
    """Applies in the style of kairouan texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_inthestyleofkairouan.png"

    temp_files = random_filename()

    instruction = '_fx_stylize inthestyleofkairouan +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def polyphony2(input, output):
    """Applies polyphony2 texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_polyphony2.png"

    temp_files = random_filename()

    instruction = '_fx_stylize polyphony2 +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def summer(input, output):
    """Applies wheat stacks end of summer texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_wheatstacksendofsummer.png"

    temp_files = random_filename()

    instruction = '_fx_stylize wheatstacksendofsummer +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def portrait(input, output):
    """Applies portrait de metzinger texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_portraitdemetzinger.png"

    temp_files = random_filename()

    instruction = '_fx_stylize portraitdemetzinger +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def redtree(input, output):
    """Applies red tree texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_redtree.png"

    temp_files = random_filename()

    instruction = '_fx_stylize redtree +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def redwaistcoat(input, output):
    """Applies red waistcoat texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_redwaistcoat.png"

    temp_files = random_filename()

    instruction = '_fx_stylize redwaistcoat +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def ebro(input, output):
    """Applies reservoir horta de ebro texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_reservoirhortadeebro.png"

    temp_files = random_filename()

    instruction = '_fx_stylize reservoirhortadeebro +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def blossom(input, output):
    """Applies almond blossom texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_almondblossom.png"

    temp_files = random_filename()

    instruction = '_fx_stylize almondblossom +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def landscape(input, output):
    """Applies landscape near antwerp texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_landscapenearantwerp.png"

    temp_files = random_filename()

    instruction = '_fx_stylize landscapenearantwerp +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def wheatfield(input, output):
    """Applies wheat field with crows texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_wheatfieldwithcrows.png"

    temp_files = random_filename()

    instruction = '_fx_stylize wheatfieldwithcrows +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,5,2,1.85,0'
    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    shutil.copyfile(image[0], output)
    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred. Fewer than 3 images were generated.")

    for image in generated_images:
        os.remove(image)

@cli.command()
def list():
    for effect in effects:
        print(effect)


@cli.command()
@click.argument('input', type=click.Path(exists=True))
def alleffects(input):
    import time
    for effect in effects:
        function_name = globals().get(effect)
        if function_name and callable(function_name):
            command = f'{os.path.basename(__file__)} {effect} {input}'
            result = subprocess.run(command, shell=True, capture_output=True)
            print(effect)
            print(result.stdout.decode())
            time.sleep(1)


if __name__ == '__main__':
    cli()
