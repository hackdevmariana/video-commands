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
            'blurradial',
            'gaussianblur',
            'blurdof',
            'blurangular',
            'stripesy',
            'spread',
            'squares',
            'oldphoto',
            'polkadots',
            'upscale',
            'unsharp',
            'blocks3d',
            'lightmaptones',
            'darkmaptones',
            'newspaperdotted',
            'deblur',
            'pencilsketch',
            'rainbow',
            'judgment',
            'normalizelocal',
            'gridtriangular',
            'fxscanlines',
            'unsharpgoldmeinel',
            'warhol',
            'lightpatch',
            'twirl',
            'oilbw',
            'noise',
            'reflect',
            'hearts',
            'vignette',
            'tiles',
            'clarifyshadow',
            'frameround',
            'raindrops',
            'crystal',
            'deform',
            'charcoal',
            'edgeoffsets',
            'gradientnorm',
            'gradientrgb',
            'isophotes',
            'embossedmetal',
            'waxstains',
            'sectionalboxfitting',
            'framefuzzy',
            'rotatetiles',
            'fractalize',
            'sackcloth',
            'waxpaint',
            'feltpen',
            'burnoldphoto',
            'brokenglass',
            'dices',
            'oldphotowithframe',
            'intensifies',
            'colorellipses',
            'contrastswm',
            'maze',
            'alienvision',
            'solarize',
            'mineralmosaic',
            'mirrory',
            'polaroid',
            'oilpainting',
            'cartoon',
            'posterize',
            'doodlepen',
            'smooth',
            'stencil',
            'posterhope',
            'stainedglass',
            'tetris',
            'weave',
            'gridhexagonal',
            'cracks',
            'scanlines',
            'badprinter',
            'lava',
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
            'imagetunnel',
            'removepixels',
            'glitteronblack',
            'emanation',
            'sponged',
            'diagonalprojection',
            'markerpen',
            'polygonize',
            'pendrawing',
            'boxfitting',
            'drawwhirl',
            'cubism',
            'halftone',
            'shockwaves',
            'mosaic',
            'sphere',
            'thickstroke',
            'frameblur',
            'puzzle',
            'shadowpatch',
            'arrayfade',
            'tiles',
            'sharpeninversediff',
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
            'lightglow',
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
            'alien',
            'sharpen',
            'reddens',
            'grid',
            'littlebayatlaciotat',
            'leviaducalestaque',
            'summertime9a',
            'convergence',
            'irises',
            'themandola',
            'lightrelief',
            'orientalgarden',
            'squarescircles',
            'kairouan',
            'unsharpoctave',
            'polyphony2',
            'summer',
            'lightrays',
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
def clarifyshadow(input, output):
    """Applies clarify shadow to the received image."""

    if not output:
        output = f"{Path(input).stem}_clarify_shadow.png"

    gmic.run(f'{input} fx_equalize_shadow 1,0 output {output}')

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
def alien(input, output):
    """Applies alien effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_alien.png"

    gmic.run(f'{input} repeat 3 smooth 40,0,1,1,2 done output {output}')

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
def charcoal(input, output):
    """Applies charcoal effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_charcoal.png"

    gmic.run(f'{input} fx_engrave 0.5,50,0,8,40,0,0,0,10,1,0,0,0,1,0 output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def edgeoffsets(input, output):
    """Applies edge offsets effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_edge_offsets.png"

    gmic.run(f'{input} fx_edge_offsets 0,15,4,1,0,0 output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")




@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=10, help='Blur intensity')
def tetris(input, output, intensity):
    """Applies tetris effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_tetris.png"

    gmic.run(f'{input} tetris {intensity} output {output}')

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
def waxstains(input, output):
    """Applies wax stains effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_wax_stains.png"

    instruction = "fx_segment_watershed 2,1,0,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def twirl(input, output):
    """Applies twirl effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_twirl.png"

    instruction = "fx_twirl 1,50,50,1"
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
def gaussianblur(input, output, intensity):
    """Applies gaussian blur effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_gaussianblur.png"

    instruction = f"fx_gaussian_blur {intensity},0,0,1,0,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def wind(input, output):
    """Applies wind effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_wind.png"

    instruction = "fx_wind 20,0,0.7,20,1,0,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def spread(input, output):
    """Applies spread effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_spread.png"

    instruction = "fx_spread 2,1,0,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lightmaptones(input, output):
    """Applies light map tones effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_lightmaptones.png"

    instruction = "fx_map_tones_fast 3,0.5,11,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkmaptones(input, output):
    """Applies dark map tones effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_darkmaptones.png"

    instruction = "fx_map_tones 0.5,0.7,0.1,30,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")




@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def softpixelate(input, output):
    """Applies soft pixelate effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_softpixelate.png"

    instruction = "fx_sharpen_shock 150,0.1,0.8,1.1,1,0,0,24,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def unsharp(input, output):
    """Applies soft pixelate effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_unsharp.png"

    instruction = "fx_unsharp_richardsonlucy 1,10,1,1,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def oldtiles(input, output):
    """Applies old tiles texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_old_tiles.png"

    instruction = f'split_tiles 5,5 -blur 8 -sharpen 1000 -equalize 255 -append_tiles 5,5'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def pencilsketch(input, output):
    """Applies pencil sketch effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_pencil_sketch.png"

    instruction = f'-sketchbw , -rv -blend overlay'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def polkadots(input, output):
    """Applies polka dots texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_polka_dots.png"

    instruction = f'fx_polka_dots 80,20,50,50,0,0.5,0.1,1,255,0,0,25'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def rainbow(input, output):
    """Applies rainbow texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_rainbow.png"

    instruction = f'fx_rainbow 80,80,175,175,3,8'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")





@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def blocks3d(input, output):
    """Applies blocks3d texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_blocks3d.png"

    instruction = f'fx_blocks3d 32,0,4,1.5,30,60,45,50,50,0,-50,-100,0.5,0.7,1,1,0,0,0,128'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")




@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--percentage', '-p', default=200, help='Enlargement percentage')
def upscale(input, output, percentage):
    """Upscale to the received image."""

    if not output:
        output = f"{Path(input).stem}_upscale.png"

    instruction = f'fx_upscale_smart "{percentage}%","{percentage}%",2,0.4,50'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")




@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def droste(input, output):
    """Applies droste effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_droste.png"

    instruction = "fx_droste 20,20,80,20,80,80,20,80,1,0,0,0,1,0,1,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=50, help='Waves intensity')
def stripesy(input, output, intensity):
    """Applies stripes in y axis to the received image."""

    if not output:
        output = f"{Path(input).stem}_stripesy.png"

    instruction = f"fx_stripes_y {intensity},0,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=50, help='Waves intensity')
def shadestripes(input, output, intensity):
    """Applies shade stripes effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_shadestripes.png"

    instruction = f"fx_shade_stripes {intensity},1,0.8,1.3,0,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=50, help='Waves intensity')
def fxscanlines(input, output, intensity):
    """Applies fx scanlines effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_fxscanlines.png"

    instruction = f"fx_scanlines {intensity},2,0,0,0,0,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def colorellipses(input, output):
    """Applies color ellipses texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_color_ellipses.png"

    instruction = "fx_color_ellipses 400,8,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def shockwaves(input, output):
    """Applies shockwaves texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_shockwaves.png"

    instruction = "fx_shockwaves 10,10,20,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=10, help='Sponged intensity')
def sponge(input, output, intensity):
    """Applies sponged texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_sponge.png"

    instruction = f"fx_sponge {intensity},0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=20, help='Sponged intensity')
def stainedglass(input, output, intensity):
    """Applies stained glass effects to the received image."""

    if not output:
        output = f"{Path(input).stem}_stained_glass.png"

    instruction = f"fx_stained_glass {intensity},0.1,1,1,1,0,1,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=2, help='Sponged intensity')
def thickmarker(input, output, intensity):
    """Applies thick marker effects to the received image."""

    if not output:
        output = f"{Path(input).stem}_thick_marker.png"

    instruction = f"fx_stencil {intensity},0,8,0,2,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def triangles(input, output):
    """Applies triangles bw texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_triangles_bw.png"

    instruction = f"fx_shapes 4,16,10,2,5,90,0,0,1,1,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def rhombuses(input, output):
    """Applies rhombuses bw texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_rhombuses_bw.png"

    instruction = f"fx_shapes 3,16,10,2,5,90,0,0,1,1,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def squares(input, output):
    """Applies squares bw texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_squares_bw.png"

    instruction = f"fx_shapes 2,16,10,2,5,90,0,0,1,1,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def fxhalftone(input, output):
    """Applies fx halftone effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_fx_halftone.png"

    instruction = f"fx_halftone 0,1,0,0,5,8,8,5,0.1,00"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def pales(input, output):
    """Applies pales effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_pales.png"

    instruction = f"apply_gamma 1.5"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def kitt(input, output):
    """Applies Knight Rider texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_knight_rider.png"

    instruction = f"fx_shapes 5,16,10,2,5,90,0,0,1,1,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def normalizelocal(input, output):
    """Applies normalize local effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_normalizelocal.png"

    instruction = "fx_normalize_local 2,6,5,20,1,11,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def deblur(input, output):
    """Applies deblur effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_deblur.png"

    instruction = "fx_deblur 2,10,20,0.1,1,11,0,24,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def blurangular(input, output):
    """Applies blur angular effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_blurangular.png"

    instruction = "fx_blur_angular 2,50,50,0,1,7,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def blurdof(input, output):
    """Applies blur dof effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_blurdof.png"

    instruction = "fx_blur_dof 3,3,0,0,50,50,30,30,0,1,1,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def blurradial(input, output):
    """Applies blur radial effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_blurradial.png"

    instruction = "fx_blur_radial 3,50,50,0,1,7,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=10, help='Waves intensity')
def noise(input, output, intensity):
    """Applies noise effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_noise.png"

    instruction = f"fx_noise {intensity},0,0,1,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def raindrops(input, output):
    """Applies raindrops effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_raindrops.png"

    instruction = "raindrops 80,0.1,1,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=10, help='Waves intensity')
def deform(input, output, intensity):
    """Applies deform waves effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_deform.png"

    instruction = f"deform {intensity}"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def reflect(input, output):
    """Applies reflect effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_reflect.png"

    instruction = "fx_reflect 50,1,110,160,190,64,0,1.5,0,-3.3,7,1.5"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def sphere(input, output):
    """Applies sphere effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_sphere.png"

    instruction = "fx_map_sphere 512,512,90,0.5,0,0,20,0,0,0,0.5"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def embossedmetal(input, output):
    """Applies embossed metal effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_embossed_metal.png"

    instruction = "fx_local_orientation 0,0,100,0,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def isophotes(input, output):
    """Applies isophotes effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_embossed_metal.png"

    instruction = "fx_isophotes 8,0,1,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def gradientnorm(input, output):
    """Applies gradient norm effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_gradient_norm.png"

    instruction = "fx_gradient_norm 0,0.5,0,100,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def gradientrgb(input, output):
    """Applies gradient rgb effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_gradient_rgb.png"

    instruction = "fx_gradient2rgb 0,0,100,0,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")




@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def alienvision(input, output):
    """Applies alien vision effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_alien_vision.png"

    instruction = "fx_marble .5,1,0,0,.4,.6,.6,1.1,0,100"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def maze(input, output):
    """Create an image with maze to size of the received image."""

    if not output:
        output = f"{Path(input).stem}_alien_vision.png"

    instruction = "fx_maze 24,1,0,1,0"
    gmic.run(f'{input} {instruction} output {output}')

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
def mineralmosaic(input, output):
    """Applies mineral mosaic effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_mineral_mosaic.png"

    instruction = "fx_mineral_mosaic 1,2,1,100,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def solarize(input, output):
    """Applies solarize effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_solarize.png"

    instruction = "solarize"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")
@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def mirrory(input, output):
    """Applies mirror y effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_mirror_y.png"

    instruction = "mirror y"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def mirrorx(input, output):
    """Applies mirror x effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_mirror_x.png"

    instruction = "mirror x"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def intensifies(input, output):
    """Applies intensifies color effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_intensifies.png"

    instruction = "apply_gamma 0.5"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def framefuzzy(input, output):
    """Applies a frame fuzzy to the received image."""

    if not output:
        output = f"{Path(input).stem}_frame_fuzzy.png"

    instruction = "fx_frame_fuzzy 5,5,10,1,255,255,255,255"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def vignette(input, output):
    """Applies a vignette effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_vignette.png"

    instruction = "fx_vignette 70,70,95,0,0,0,255"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def imagetunnel(input, output):
    """Applies a all image tunnel effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_image_tunnel.png"

    instruction = "fx_tunnel 4,80,0.5,0.5,0.2,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lightrays(input, output):
    """Applies lightrays in black and white to the received image."""

    if not output:
        output = f"{Path(input).stem}_lightrays.png"

    instruction = "fx_lightrays 80,50,50,1,0.5,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lightpatch(input, output):
    """Applies a light patch effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_light_patch.png"

    instruction = "fx_light_patch 5,0.7,2.5,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lightglow(input, output):
    """Applies lightglow effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_lightglow.png"

    instruction = "fx_lightglow 30,0.5,8,0.8,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def oldphotowithframe(input, output):
    """Applies a old photo with frame effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_old_photo_with_frame.png"

    instruction = "fx_old_photo 200,50,85"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def burnoldphoto(input, output):
    """Applies a burny old photo effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_burn_old_photo.png"

    instruction = "fx_burn 0.5,30,1,0,0,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def contrastswm(input, output):
    """Applies a contrast swm to the received image."""

    if not output:
        output = f"{Path(input).stem}_frame_fuzzy.png"

    instruction = "fx_contrast_swm 2,0,1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def dices(input, output):
    """Applies black and white dice texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_dices.png"

    instruction = "fx_dices 2,24,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def brokenglass(input, output):
    """Applies brokenglass effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_brokenglass.png"

    instruction = "fx_polygonize 300,10,10,10,10,0,0,0,255,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def waxpaint(input, output):
    """Applies wax paint effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_wax_paint.png"

    instruction = "fx_pen_drawing 10,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def feltpen(input, output):
    """Applies feltpen effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_feltpen.png"

    instruction = "fx_feltpen 300,50,1,0.1,20,5,0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def fractalize(input, output):
    """Applies fractalize effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_fractalize.png"

    instruction = "fractalize 0.8"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('-x', default=5, help='Tiles on the x axis')
@click.option('-y', default=5, help='Tiles on the y axis')
def rotatetiles(input, output, x, y):
    """Applies rotate tiles texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_rotate_tiles.png"

    instruction = f"fx_rotate_tiles {x},{y},15,3,3,1.8"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('-x', default=3, help='Tiles on the x axis')
@click.option('-y', default=3, help='Tiles on the y axis')
def tiles(input, output, x, y):
    """Applies tiles to the received image."""

    if not output:
        output = f"{Path(input).stem}_tiles.png"

    instruction = f"fx_shift_tiles {x},{y},10,1"
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
def oilbw(input, output):
    """Applies black and white oil effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_oldgame.png"

    instruction = "fx_cutout 4,0.5,4,1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('-x', default=3, help='Repetitions on the x axis')
@click.option('-y', default=3, help='Repetitions on the y axis')
def warhol(input, output, x, y):
    """Applies warhol effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_oldgame.png"

    instruction = f"warhol {x},{y},2,40"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def gridtriangular(input, output):
    """Applies grid triangular to the received image."""

    if not output:
        output = f"{Path(input).stem}_oldgame.png"

    instruction = "fx_imagegrid_triangular 10,18,0,0,0,0,255"
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
def pointwise(input, output):
    """Applies pointwise absolute values of  the received image."""

    if not output:
        output = f"{Path(input).stem}_pointwise_absolute.png"

    instruction = "sub {ia} abs[-1]"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkenbw(input, output):
    """Applies darken and black and white of the received image."""

    if not output:
        output = f"{Path(input).stem}_darkenwb.png"

    instruction = "luminance -normalize 0,{30*pi}"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def calormap(input, output):
    """Applies calor map in the received image."""

    if not output:
        output = f"{Path(input).stem}_calormap.png"

    instruction = "normalize -1,1 asin[-1]"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkensteps(input, output):
    """Applies darken steps in the received image."""

    if not output:
        output = f"{Path(input).stem}_darkensteps.png"

    instruction = "bsl 'round(3*x/w,0)' cut 0,255"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lightsteps(input, output):
    """Applies light steps in the received image."""

    if not output:
        output = f"{Path(input).stem}_lightsteps.png"

    instruction = "bsr 'round(3*x/w,0)' cut 0,255"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def glaze(input, output):
    """Applies glaze in the received image."""

    if not output:
        output = f"{Path(input).stem}_glaze.png"

    instruction = "normalize -6,6 cosh[-1]"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def squaresoflight(input, output):
    """Applies squares of light in the received image."""

    if not output:
        output = f"{Path(input).stem}_squares_of_light.png"

    instruction = "div '1+abs(cos(x/10)*sin(y/10))'"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def sparkles(input, output):
    """Applies sparkles in the received image."""

    if not output:
        output = f"{Path(input).stem}_sparkles.png"

    instruction = "div 'abs(cos(x/10)*sin(y/10))'"
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
def unsharpoctave(input, output):
    """Applies unsharp octave to the received image."""

    if not output:
        output = f"{Path(input).stem}_unsharp_octave.png"

    instruction = 'fx_unsharp_octave 4,5,3,0,0,0,24,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def sharpeninversediff(input, output):
    """Applies sharpen inversediff to the received image."""

    if not output:
        output = f"{Path(input).stem}_sharpen_inversediff.png"

    instruction = 'fx_sharpen_inversediff 50,2,11,0,24,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def unsharpgoldmeinel(input, output):
    """Applies unsharp goldmeinel to the received image."""

    if not output:
        output = f"{Path(input).stem}_unsharp_goldmeinel.png"

    instruction = 'fx_unsharp_goldmeinel 1,5,1,1,1,11,0,24,0'
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
def gridhexagonal(input, output):
    """Applies grid hexagonal to the received image."""

    if not output:
        output = f"{Path(input).stem}_poster_hope.png"

    instruction = 'fx_imagegrid_hexagonal 32,0.1,1'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def bokeh(input, output):
    """Applies bokeh effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_poster_hope.png"

    instruction = 'fx_bokeh 3,8,0,30,8,4,0.3,0.2,210,210,80,160,0.7,30,20,20,1,2,170,130,20,110,0.15,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def posterhope(input, output):
    """Applies poster hope to the received image."""

    if not output:
        output = f"{Path(input).stem}_poster_hope.png"

    instruction = 'fx_poster_hope 0,3,0'
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
def lightrelief(input, output):
    """Applie light relief to the received image."""

    if not output:
        output = f"{Path(input).stem}_light_relief.png"

    instruction = 'fx_light_relief 0.3,0.2,0.2,0,1,0.5,0.5,5,0.5,0,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lava(input, output):
    """Applie lava effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_lava.png"

    instruction = 'fx_lava 8,5,3,0,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def hearts(input, output):
    """Applie hearts texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_lava.png"

    instruction = 'fx_hearts 10,0,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def crystal(input, output):
    """Applie broken crystal texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_crystal.png"

    instruction = 'fx_crystal 50,0.2,20,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def diagonalprojection(input, output):
    """Applie diagonal projection effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_diagonal_projection.png"

    instruction = 'fx_canvas 70,45,400,1,70,135,400,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def paper(input, output):
    """Applie paper texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_paper.png"

    instruction = 'fx_paper 0,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def whirls(input, output):
    """Applie whirls texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_whirls.png"

    instruction = 'fx_whirls 7,2,0.2,1.8,11,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def sackcloth(input, output):
    """Applie sackcloth texture to the received image."""

    if not output:
        output = f"{Path(input).stem}_sackcloth.png"

    instruction = 'texturize_canvas 20,3,0.6'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")




@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def sectionalboxfitting(input, output):
    """Applies sectional boxfitting to the received image."""

    if not output:
        output = f"{Path(input).stem}_sectional_boxfitting.png"

    instruction = 'fx_boxfitting 3,0,0.1,0'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def frameround(input, output):
    """Applies frame round to the received image."""

    if not output:
        output = f"{Path(input).stem}_frame_round.png"

    instruction = 'fx_frame_round 6,20,0.1,0,255,255,255,255,0,0.1,3'
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")




@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def shadowpatch(input, output):
    """Applies shadow patch to the received image."""

    if not output:
        output = f"{Path(input).stem}_shadow_patch.png"

    instruction = 'fx_shadow_patch 0.7,0'
    gmic.run(f'{input} {instruction} output {output}')

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
