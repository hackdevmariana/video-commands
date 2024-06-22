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

from itertools import product

from random import uniform, randint

from PIL import ImageChops, Image

from video_commands_lib import random_filename

effects = [
            'blur',
            'blurx',
            'blury',
            'clarifyshadow',
            'oldphoto',
            'newspaperdotted',
            'alien',
            'judgment',
            'polaroid',
            'oilpainting',
            'cartoon',
            'posterize',
            'doodlepen',
            'smooth',
            'stencil',
            'charcoal',
            'edgeoffsets',
            'tetris',
            'weave',
            'cracks',
            'scanlines',
            'badprinter',
            'waxstains',
            'twirl',
            'gaussianblur',
            'wind',
            'spread',
            'lightmaptones',
            'darkmaptones',
            'softpixelate',
            'unsharp',
            'oldtiles',
            'pencilsketch',
            'polkadots',
            'rainbow',
            'blocks3d',
            'upscale',
            'droste',
            'stripesy',
            'shadestripes',
            'fxscanlines',
            'colorellipses',
            'shockwaves',
            'sponge',
            'stainedglass',
            'thickmarker',
            'triangles',
            'rhombuses',
            'squares',
            'fxhalftone',
            'pales',
            'kitt',
            'normalizelocal',
            'deblur',
            'blurangular',
            'blurdof',
            'blurradial',
            'noise',
            'raindrops',
            'deform',
            'reflect',
            'sphere',
            'embossedmetal',
            'isophotes',
            'gradientnorm',
            'gradientrgb',
            'alienvision',
            'maze',
            'telesketch',
            'mineralmosaic',
            'solarize',
            'mirrory',
            'mirrorx',
            'intensifies',
            'framefuzzy',
            'vignette',
            'imagetunnel',
            'lightrays',
            'lightpatch',
            'lightglow',
            'oldphotowithframe',
            'burnoldphoto',
            'contrastswm',
            'dices',
            'brokenglass',
            'waxpaint',
            'feltpen',
            'fractalize',
            'rotatetiles',
            'tiles',
            'nebula',
            'blackhole',
            'acid',
            'expandingblackhole',
            'flash',
            'lightoff',
            'offwhites',
            'veiled',
            'turnspurple',
            'blueandblack',
            'turquoiseandblack',
            'seaandblack',
            'greenandblackcontrasted',
            'blueandblackcontrasted',
            'darkgreenandblack',
            'lightamericannight',
            'contrastedturquoise',
            'luminousred',
            'dimred',
            'reddishorange',
            'intenseamber',
            'paleamber',
            'pink',
            'luminousyellow',
            'ambertoasted',
            'amber',
            'contrastedamber',
            'amberoff',
            'orange',
            'orangeoff',
            'purple',
            'lime',
            'greenlime',
            'luminousgreen',
            'lemonlime',
            'dullyellow',
            'intenseyellow',
            'yellow',
            'redlightgreenspectral',
            'redlightbluespectral',
            'redbluespectral',
            'redturquoisespectral',
            'redindigospectral',
            'redgreenspectral',
            'darkyellow',
            'luminousindigo',
            'paleblue',
            'darkintensered',
            'intenseyellow',
            'darkblueblack',
            'orangeblack',
            'palecobalt',
            'bluesubtleyellow',
            'palebluepurple',
            'greenpurple',
            'garnetlime',
            'blueplum',
            'inblue',
            'subtleblue',
            'darkintenselilac',
            'luminousintensegreen',
            'luminousindigo',
            'indigo',
            'paleindigoblack',
            'darkpalegreenblack',
            'darknight',
            'palepink',
            'luminousredblack',
            'intenselime',
            'darkintensepurple',
            'paleindigo',
            'intensedarklime',
            'naturaldarkyellow',
            'darkorange',
            'darkpurple',
            'lilacluminous',
            'lilacblue',
            'lilac',
            'lilacblueluminous',
            'redoff',
            'luminouslilac',
            'luminouspurple',
            'intensered',
            'contrastedalien',
            'americannight',
            'electricgreen',
            'maritime',
            'electricalienandwhite',
            'darkwine',
            'contrastedblue',
            'spectralblue',
            'spectralsky',
            'seaweed',
            'aliencobalt',
            'intensepinkandblack',
            'intenseyellowandblack',
            'skyandwhite',
            'grapeandwhite',
            'indigoandwhite',
            'basilandwhite',
            'wineandwhite',
            'tealandwhite',
            'pasteltealandwhite',
            'pearwhite',
            'purplewhite',
            'purpleyellow',
            'yellowandsky',
            'whiteandsky',
            'whiteandgreen',
            'whiteandgarnet',
            'whiteandpurple',
            'yellowandpurple',
            'yellowandbrown',
            'whiteandsapphire',
            'pinetree',
            'palesky',
            'electricblue',
            'electricgreenblue',
            'clearscolumns',
            'intensifiesdark',
            'spectral',
            'lucy',
            'pastelchalk',
            'colorfulborders',
            'sepia',
            'quantize',
            'reversevertical',
            'reversehorizontal',
            'appendtiles',
            'hydraulictiles',
            'dotstorm',
            'dotmarkerpen',
            'stipplingmarker',
            'gaussiandifferences',
            'erodecirc',
            'multipoint',
            'coloredtelesketch',
            'double',
            'delimitedcontour',
            'contourdetails',
            'enhancesblurring',
            'vanvliet',
            'colordots',
            'bwdots',
            'outline',
            'fineoutline',
            'cracked',
            'lowlevel',
            'projectcontours',
            'outlineonblack',
            'thirdpartyguides',
            'greyish',
            'fourfour',
            'arraymirror',
            'vignetteblur',
            'rotatetiles',
            'shifttiles',
            'intensestains',
            'vinylstains',
            'oilstains',
            'fingerpaint',
            'woodpaint',
            'mural',
            'colorfulmural',
            'greatpointillism',
            'flattenscolors',
            'flattenscolorsbw',
            'uniformink',
            'aqueousink',
            'brightdetails',
            'pressing',
            'colorsketch',
            'flatcomic',
            'hero',
            'handstrokes',
            'uniformstains',
            'colorareas',
            'coloredmarker',
            'intenseposter',
            'colourstains',
            'airbrushing',
            'colorellipses',
            'cubism',
            'drawing',
            'fireedges',
            'fractalize',
            'ellipsionism',
            'blurrysketch',
            'hardsketchbw',
            'handsketch',
            'linify',
            'pencilbw',
            'posteredges',
            'subtledrawing',
            'multicross',
            'stainsbw',
            'areasbw',
            'inked',
            'inkedhardstroke',
            'roundedstains',
            'rorschach',
            'rainbw',
            'multilinebw',
            'subtlewhirls',
            'ripple',
            'rotoidoscope',
            'rotatedcross',
            'inflates',
            'implosion',
            'recreation',
            'warpperspective',
            'breeze',
            'pixelize',
            'texturizepaper',
            'framefuzzy',
            'framecube',
            'dottedbw',
            'darktogarnet',
            'darkandoutline',
            'clarified',
            'badtonner',
            'deriche',
            'blackembossed',
            'luminance',
            'gaussiandog',
            'taquin',
            'erode',
            'saltnoise',
            'inpaint',
            'kuwahara',
            'normalizelocal',
            'breaksstains',
            'fog',
            'luster',
            'oldgame',
            'oilbw',
            'warhol',
            'gridtriangular',
            'removepixels',
            'glitteronblack',
            'pointwise',
            'darkenbw',
            'calormap',
            'darkensteps',
            'lightsteps',
            'glaze',
            'squaresoflight',
            'sparkles',
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
            'unsharpoctave',
            'sharpeninversediff',
            'unsharpgoldmeinel',
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
            'gridhexagonal',
            'bokeh',
            'posterhope',
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
            'lightrelief',
            'lava',
            'hearts',
            'crystal',
            'diagonalprojection',
            'paper',
            'whirls',
            'sackcloth',
            'sectionalboxfitting',
            'frameround',
            'shadowpatch',
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
            'wheatfield',
            ]

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
def smoothed(input, output):
    """Applies smoothed effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_smoothed.png"

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
def nebula(input, output):
    """Applies nebula effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_nebula.png"

    instruction = "max 'R=((x/w-0.5)^2+(y/h-0.5)^2)^0.5;255*R'"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def blackhole(input, output):
    """Applies black hole effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_black_hole.png"

    instruction = "min 'R=((x/w-0.5)^2+(y/h-0.5)^2)^0.5;255*R'"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def acid(input, output):
    """Applies acid effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_acid.png"

    instruction = "mod 'R=((x/w-0.5)^2+(y/h-0.5)^2)^0.5;255*R'"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def expandingblackhole(input, output):
    """Applies expanding black hole effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_expanding_black_hole.png"

    instruction = "mul 'R=((x/w-0.5)^2+(y/h-0.5)^2)^0.5;255*R'"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def flash(input, output):
    """Applies flash effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_flash.png"

    instruction = "mul 2 cut 0,255"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lightoff(input, output):
    """Applies light off effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_light_off.png"

    instruction = "mul .3"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def offwhites(input, output):
    """Applies off whites effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_off_whites.png"

    instruction = "cut 0,128"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def veiled(input, output):
    """Applies veiled effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_veiled.png"

    instruction = "cut 128,255"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def turnspurple(input, output):
    """Applies purple tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_purple.png"

    instruction = "mul_channels 1,0.5,0.8"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def blueandblack(input, output):
    """Applies blue and black tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_purple.png"

    instruction = "mul_channels 0,0.1,0.4"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def turquoiseandblack(input, output):
    """Applies turquoise and black tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_turquoiseandblack.png"

    instruction = "mul_channels 0,0.2,0.2"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def seaandblack(input, output):
    """Applies sea and black tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_seaandblack.png"

    instruction = "mul_channels 0,0.2,0.3"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def greenandblackcontrasted(input, output):
    """Applies green and black contrasted tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_green_and_black_contrasted.png"

    instruction = "mul_channels 0,0.4,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def blueandblackcontrasted(input, output):
    """Applies blue and black contrasted tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_blue_and_black_contrasted.png"

    instruction = "mul_channels 0,0.2,1.0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkgreenandblack(input, output):
    """Applies dark green and black tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_darkgreenandblack.png"

    instruction = "mul_channels 0,0.2,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lightamericannight(input, output):
    """Applies light american night tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_lightamericannight.png"

    instruction = "mul_channels 0,0.5,0.9"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def contrastedturquoise(input, output):
    """Applies contrasted turquoise tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_contrasted_turquoise.png"

    instruction = "mul_channels 0,0.8,0.7"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def luminousred (input, output):
    """Applies luminous red tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_luminous_red.png"

    instruction = "mul_channels 1,0.1,0.4"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def dimred (input, output):
    """Applies dim red tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_dim_red.png"

    instruction = "mul_channels 1,0.2,0.3"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def reddishorange (input, output):
    """Applies reddish orange tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_reddish_orange.png"

    instruction = "mul_channels 1,0.3,0.4"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def intenseamber (input, output):
    """Applies intense amber tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_intense_amber.png"

    instruction = "mul_channels 1,0.6,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def paleamber (input, output):
    """Applies pale amber tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_pale_amber.png"

    instruction = "mul_channels 1,0.6,0.3"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def pink (input, output):
    """Applies pink tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_pink.png"

    instruction = "mul_channels 1,0.6,0.8"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def luminousyellow (input, output):
    """Applies luminous yellow tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_luminous_yellow.png"

    instruction = "mul_channels 1,0.7,0.2"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def ambertoasted (input, output):
    """Applies amber toasted tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_amber_toasted.png"

    instruction = "mul_channels 1,0.7,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def amber (input, output):
    """Applies amber tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_amber.png"

    instruction = "mul_channels 1,0.7,0.5"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def contrastedamber (input, output):
    """Applies contrasted amber tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_contrasted_amber.png"

    instruction = "mul_channels 1,0.7,0.3"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def amberoff (input, output):
    """Applies amber off tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_amber_off.png"

    instruction = "mul_channels 1,0.5,0.2"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def orange (input, output):
    """Applies orange tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_orange.png"

    instruction = "mul_channels 1,0.4,0.0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def orangeoff (input, output):
    """Applies orange off tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_orange_off.png"

    instruction = "mul_channels 1,0.4,0.2"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def purple (input, output):
    """Applies purple tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_purple.png"

    instruction = "mul_channels 1,1.0,1.0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lime (input, output):
    """Applies lime tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_lime.png"

    instruction = "mul_channels 1,1.0,0.5"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def greenlime (input, output):
    """Applies green lime tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_green_lime.png"

    instruction = "mul_channels 1,1.0,0.3"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def luminousgreen (input, output):
    """Applies luminous green tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_luminous_green.png"

    instruction = "mul_channels 1,1.0,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lemonlime (input, output):
    """Applies lemon lime tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_lemon_lime.png"

    instruction = "mul_channels 1,0.9,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def dullyellow (input, output):
    """Applies dull yellow tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_dull_yellow.png"

    instruction = "mul_channels 1,0.8,0.5"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def intenseyellow (input, output):
    """Applies intense yellow tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_intense_yellow.png"

    instruction = "mul_channels 1,0.8,0.3"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def yellow (input, output):
    """Applies yellow tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_yellow.png"

    instruction = "mul_channels 1,0.8,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def redlightgreenspectral (input, output):
    """Applies red green spectral tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_red_light_green_spectral.png"

    instruction = "mul_channels -1,1.0,0.2"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def redlightbluespectral (input, output):
    """Applies red blue spectral tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_red_light_blue_spectral.png"

    instruction = "mul_channels -1,0.6,0.9"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def redbluespectral (input, output):
    """Applies red blue spectral tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_red_blue_spectral.png"

    instruction = "mul_channels -1,0.3,0.9"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def redturquoisespectral (input, output):
    """Applies red turquoise spectral tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_red_turquoise_spectral.png"

    instruction = "mul_channels -1,0.9,0.8"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def redindigospectral (input, output):
    """Applies red indigo spectral tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_red_indigo_spectral.png"

    instruction = "mul_channels -1,0.5,0.5"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def redgreenspectral (input, output):
    """Applies red green spectral tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_red_green_spectral.png"

    instruction = "mul_channels -1,0.9,0.4"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkyellow (input, output):
    """Applies dark yellow tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_dark_yellow.png"

    instruction = "mul_channels 0.7,0.5,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def luminousindigo (input, output):
    """Applies luminous indigo tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_luminous_indigo.png"

    instruction = "mul_channels 0.7,0.4,1.0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def paleblue (input, output):
    """Applies pale blue tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_pale_blue.png"

    instruction = "mul_channels 0.7,0.7,0.9"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkintensered (input, output):
    """Applies dark intense red tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_dark_intense_red.png"

    instruction = "mul_channels 1.0,0.0,0.3"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def intenseyellow (input, output):
    """Applies intense yellow tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_intense_yellow.png"

    instruction = "mul_channels 1.0,1.0,0.0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkblueblack (input, output):
    """Applies dark blue black tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_dark_blue_black.png"

    instruction = "mul_channels 0.0,0.0,0.7"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def orangeblack (input, output):
    """Applies orange black tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_orange_black.png"

    instruction = "mul_channels 1.0,0.2,0.0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def palecobalt (input, output):
    """Applies pale cobalt tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_pale_cobalt.png"

    instruction = "mul_channels 0.0,-0.7,-0.6"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def bluesubtleyellow (input, output):
    """Applies blue subtle yellow tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_blue_subtle_yellow.png"

    instruction = "mul_channels 0.8,0.8,-0.8"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def palebluepurple (input, output):
    """Applies pale blue purple tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_pale_blue_purple.png"

    instruction = "mul_channels 0.7,-0.9,-0.4"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def greenpurple (input, output):
    """Applies green purple tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_green_purple.png"

    instruction = "mul_channels 0.6,-1.0,0.6"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def garnetlime (input, output):
    """Applies garnet lime tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_garnet_lime.png"

    instruction = "mul_channels 0.6,-0.8,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def blueplum (input, output):
    """Applies blue plum tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_blue_plum.png"

    instruction = "mul_channels 0.6,-0.8,-0.4"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def inblue (input, output):
    """Applies in blue tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_in_blue.png"

    instruction = "mul_channels 0.2,-0.8,-0.5"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def subtleblue (input, output):
    """Applies subtle blue tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_subtle_blue.png"

    instruction = "mul_channels 0.2,-0.6,-0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkintenselilac (input, output):
    """Applies dark intense lilac tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_dark_intense_lilac.png"

    instruction = "mul_channels 1.0,0.0,0.9"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def luminousintensegreen (input, output):
    """Applies luminous intense green tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_luminous_intense_green.png"

    instruction = "mul_channels 0.0,1.0,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def luminousindigo (input, output):
    """Applies luminous indigo tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_luminous_indigo.png"

    instruction = "mul_channels 0.0,0.9,1.0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def indigo (input, output):
    """Applies indigo tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_indigo.png"

    instruction = "mul_channels 0.0,0.6,0.8"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def paleindigoblack (input, output):
    """Applies pale indigo black tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_pale_indigo_black.png"

    instruction = "mul_channels 0.0,0.6,0.8"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkpalegreenblack (input, output):
    """Applies dark pale green black tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_dark_pale_green_black.png"

    instruction = "mul_channels 0.0,0.2,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darknight (input, output):
    """Applies dark night tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_dark_night.png"

    instruction = "mul_channels 0.0,0.1,0.3"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def palepink (input, output):
    """Applies pale pink tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_pale_pink.png"

    instruction = "mul_channels 0.9,0.3,0.4"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def luminousredblack (input, output):
    """Applies luminous red black tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_luminous_red_black.png"

    instruction = "mul_channels 0.9,0.0,0.0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def intenselime (input, output):
    """Applies intense lime tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_intense_lime.png"

    instruction = "mul_channels 0.8,0.9,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkintensepurple (input, output):
    """Applies dark intense purple tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_dark_intense_purple.png"

    instruction = "mul_channels 0.8,0.0,0.6"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def paleindigo (input, output):
    """Applies pale indigo tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_pale_indigo.png"

    instruction = "mul_channels 0.7,0.9,0.5"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def intensedarklime (input, output):
    """Applies intense dark lime tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_intense_dark_lime.png"

    instruction = "mul_channels 0.7,0.8,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def naturaldarkyellow (input, output):
    """Applies natural dark yellow tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_natural_dark_yellow.png"

    instruction = "mul_channels 0.7,0.6,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkorange (input, output):
    """Applies dark orange tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_dark_orange.png"

    instruction = "mul_channels 0.7,0.4,0.0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkpurple (input, output):
    """Applies dark purple tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_dark_purple.png"

    instruction = "mul_channels 0.7,0.2,0.9"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lilacluminous (input, output):
    """Applies lilac luminous tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_lilac_luminous.png"

    instruction = "mul_channels 1,0.7,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lilacblue (input, output):
    """Applies lilac and blue tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_lilac_and_blue.png"

    instruction = "mul_channels 1,0.3,1.0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")



@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lilac (input, output):
    """Applies lilac tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_lilac.png"

    instruction = "mul_channels 1,0.3,0.7"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lilacblueluminous (input, output):
    """Applies lilac blue luminous tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_lilac_blue_luminous.png"

    instruction = "mul_channels 1,0.1,1.0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def redoff(input, output):
    """Applies red off tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_red_off.png"

    instruction = "mul_channels 1,0.1,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def luminouslilac(input, output):
    """Applies luminous lilac tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_luminous_lilac.png"

    instruction = "mul_channels 1,0.0,0.8"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def luminouspurple(input, output):
    """Applies luminous purple tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_luminous_purple.png"

    instruction = "mul_channels 1,0.0,0.5"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def intensered(input, output):
    """Applies intense red tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_intense_red.png"

    instruction = "mul_channels 1,0.0,0.2"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def contrastedalien(input, output):
    """Applies contrasted alien tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_contrasted_alien.png"

    instruction = "mul_channels 0,0.9,0.6"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def americannight(input, output):
    """Applies american night tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_americannight.png"

    instruction = "mul_channels 0,0.1,0.3"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def electricgreen(input, output):
    """Applies electric green tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_electric_blue.png"

    instruction = "mul_channels 0,-0.4,0.3"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def maritime(input, output):
    """Applies maritime tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_maritime.png"

    instruction = "mul_channels 0,-0.5,-0.9"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def electricalienandwhite(input, output):
    """Applies electric alien and white tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_electric_alien_and_white.png"

    instruction = "mul_channels -1.0,-0.2,-0.6"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkwine(input, output):
    """Applies dark wine tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_dark_wine.png"

    instruction = "mul_channels 0.2,0.0,0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def contrastedblue(input, output):
    """Applies contrasted blue tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_contrasted_blue.png"

    instruction = "mul_channels 0.1,-1.0,-0.3"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def spectralblue(input, output):
    """Applies spectral blue tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_spectral_blue.png"

    instruction = "mul_channels 0.1,-0.6,-0.2"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def spectralsky(input, output):
    """Applies spectral sky tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_spectral_sky.png"

    instruction = "mul_channels 0.1,-0.4,-0.4"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def seaweed(input, output):
    """Applies seaweed tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_seaweed.png"

    instruction = "mul_channels 0.0,-0.6,-0.9"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def aliencobalt(input, output):
    """Applies alien cobalt tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_alien_cobalt.png"

    instruction = "mul_channels 0.0,-0.5,0.4"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def intensepinkandblack(input, output):
    """Applies intense pink and black tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_intense_pink_and_black.png"

    instruction = "mul_channels -1.0,0.0,-0.9"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def intenseyellowandblack(input, output):
    """Applies intense yellow and black tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_intense_yellow_and_black.png"

    instruction = "mul_channels -1.0,-0.9,0.0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def skyandwhite(input, output):
    """Applies sky and white tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_sky_and_white.png"

    instruction = "mul_channels -1.0,-0.5,-0.2"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def grapeandwhite(input, output):
    """Applies grape and white tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_grape_and_white.png"

    instruction = "mul_channels -0.9,-0.9,-0.6"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def indigoandwhite(input, output):
    """Applies indigo and white tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_indigo_and_white.png"

    instruction = "mul_channels -0.9,-0.7,-0.2"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def basilandwhite(input, output):
    """Applies basil and white tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_basil_and_white.png"

    instruction = "mul_channels -0.9,-0.5,-0.9"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def wineandwhite(input, output):
    """Applies wine and white tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_wine_and_white.png"

    instruction = "mul_channels -0.9,-1.0,-0.5"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def tealandwhite(input, output):
    """Applies teal and white tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_teal_and_white.png"

    instruction = "mul_channels -0.9,-0.5,-0.5"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def pasteltealandwhite(input, output):
    """Applies pastel teal and white tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_pastel_teal_and_white.png"

    instruction = "mul_channels -0.9,-0.2,-0.3"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def pearwhite(input, output):
    """Applies pear and white tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_pear_and_white.png"

    instruction = "mul_channels -0.9,-0.1,-0.8"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def purplewhite(input, output):
    """Applies purple and white tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_purple_and_white.png"

    instruction = "mul_channels -0.8,-1.0,-0.3"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def purpleyellow(input, output):
    """Applies purple and yellow tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_purple_and_yellow.png"

    instruction = "mul_channels -0.8,-0.9,0.8"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def yellowandsky(input, output):
    """Applies yellow and sky tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_yellow_and_sky.png"

    instruction = "mul_channels -0.8,-0.4,-0.7"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def whiteandsky(input, output):
    """Applies white and sky tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_white_and_sky.png"

    instruction = "mul_channels -0.8,-0.4,-0.2"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def whiteandgreen(input, output):
    """Applies white and green tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_white_and_green.png"

    instruction = "mul_channels -0.8,-0.3,-0.8"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def whiteandgarnet(input, output):
    """Applies white and garnet tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_white_and_garnet.png"

    instruction = "mul_channels -0.7,-1.0,-0.9"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def whiteandpurple(input, output):
    """Applies white and purple tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_white_and_purple.png"

    instruction = "mul_channels -0.7,-0.9,-0.7"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def yellowandpurple(input, output):
    """Applies yellow and purple tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_yellow_and_purple.png"

    instruction = "mul_channels -0.7,-0.8,0.4"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def yellowandbrown(input, output):
    """Applies yellow and brown tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_yellow_and_brown.png"

    instruction = "mul_channels -0.7,-0.7,-0.0"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def whiteandsapphire(input, output):
    """Applies white and sapphire tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_white_and_sapphire.png"

    instruction = "mul_channels -0.7,-0.5,-0.1"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def pinetree(input, output):
    """Applies pine tree tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_pine_tree.png"

    instruction = "mul_channels 0,0.8,0.4"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def palesky(input, output):
    """Applies pale sky tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_pale_sky.png"

    instruction = "mul_channels 0,-0.6,-0.5"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def electricblue(input, output):
    """Applies electric blue tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_electric_blue.png"

    instruction = "mul_channels 0,-0.3,0.4"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def electricgreenblue(input, output):
    """Applies electric green blue tones to the received image."""

    if not output:
        output = f"{Path(input).stem}_electric_green_blue.png"

    instruction = "mul_channels 0,-0.5,0.8"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--columns', '-c', default=3, help='Output file path')
def clearscolumns(input, output, columns):
    """Applies clears for columns to the received image."""

    instruction = f"rol 'round({columns}*x/w,0)' cut 0,255"

    if not output:
        output = f"{Path(input).stem}_clearscolumns.png"

    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def intensifiesdark(input, output):
    """Applies intensifies dark tones to the received image."""

    instruction = "sqr"

    if not output:
        output = f"{Path(input).stem}_intensifies_dark.png"

    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def spectral(input, output):
    """Applies purple tones to the received image."""

    instruction = "apply_curve 1,0,0,128,255,255,0"

    if not output:
        output = f"{Path(input).stem}_spectral.png"

    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

#        palettes = ["default", "hsv", "lines", "hot", "cool", "jet", "flag", "cube", "rainbow", "algae", "amp", "balance", "curl", "deep", "delta", "dense", "diff", "haline", "ice", "matter", "oxy", "phase", "rain", "solar", "speed", "tarn", "tempo", "thermal", "topo", "turbid", "aurora", "hocuspocus", "srb2", "uzebox"]
#        print(product([0, 1], repeat=3))

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lucy(input, output):
    """Applies lysergic tones to the received image."""

    instruction = f"luminance gradient append c blur 2 orientation direction2rgb"
    if not output:
        output = f"{Path(input).stem}_deltaE.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def pastelchalk(input, output):
    """Applies pastel chalk tones to the received image."""

    instruction = f"gradient2rgb 0 equalize"
    if not output:
        output = f"{Path(input).stem}_pastel_chalk.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def colorfulborders(input, output):
    """Applies colorful borders to the received image."""

    instruction = f"gradient2rgb 0"
    if not output:
        output = f"{Path(input).stem}_colorful_borders.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def sepia(input, output):
    """Applies sepia tone to the received image."""

    instruction = 'sepia'
    if not output:
        output = f"{Path(input).stem}_sepia.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=5, help='Quantize intensity')
def quantize(input, output, intensity):
    """Applies quantize effect to the received image."""

    instruction = f'quantize {intensity}'
    if not output:
        output = f"{Path(input).stem}_quantize.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--cuts', type=int, default=10, help='Number of cuts.')
def reversevertical(input, output, cuts):
    """Cuts the image and recomposes it in reverse order."""

    instruction = f"split x,{cuts} reverse append x"
    if not output:
        output = f"{Path(input).stem}_reversevertical.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--cuts', type=int, default=10, help='Number of cuts.')
def reversehorizontal(input, output, cuts):
    """Cuts the image and recomposes it in reverse order."""

    instruction = f"split y,{cuts} reverse append y"
    if not output:
        output = f"{Path(input).stem}_reversehorizontal.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--cuts', type=int, default=10, help='Number of cuts.')
def appendtiles(input, output, cuts):
    """Cut the image into tiles and recompose it changing the order."""

    instruction = f"split xy,{cuts} append_tiles ,"
    if not output:
        output = f"{Path(input).stem}_appendtiles.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--cuts', type=int, default=10, help='Number of cuts.')
def hydraulictiles(input, output, cuts):
    """Creates a hydraulic tile effect over the image."""

    instruction = f"split_tiles {cuts},{cuts} blur 3,0 sharpen 700 append_tiles {cuts},{cuts}"
    if not output:
        output = f"{Path(input).stem}_appendtiles.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def dotstorm(input, output):
    """Applies a dispersion effect to the image points."""

    instruction = 'bandpass 10%,50%'
    if not output:
        output = f"{Path(input).stem}_dotstorm.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def dotmarkerpen(input, output):
    """Applies dotted marker pen effect to the received image."""

    instruction = 'bandpass 1%,3%'
    if not output:
        output = f"{Path(input).stem}_solarize.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def stipplingmarker(input, output):
    """Applies stippling marker to the received image."""

    instruction = 'blur 1 curvature'
    if not output:
        output = f"{Path(input).stem}_solarize.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def gaussiandifferences(input, output):
    """Applies Gaussian differences to the received image."""

    instruction = 'dog 1,8'
    if not output:
        output = f"{Path(input).stem}_solarize.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def erodecirc(input, output):
    """Applies erode circ effect to the received image."""

    instruction = 'erode_circ 7'
    if not output:
        output = f"{Path(input).stem}_solarize.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def multipoint(input, output):
    """Applies multiple stippling to the received image."""

    instruction = 'iee'
    if not output:
        output = f"{Path(input).stem}_solarize.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def coloredtelesketch(input, output):
    """Applies colored telesketch effect to the received image."""

    instruction = 'inn'
    if not output:
        output = f"{Path(input).stem}_solarize.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def double(input, output):
    """Horizontally and vertically duplicates the image."""

    instruction = 'periodize_poisson array 2,2,2 resize 50%,50%'
    if not output:
        output = f"{Path(input).stem}_double.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def delimitedcontour(input, output):
    """Delimits the outline of the figures in the image."""

    instruction = 'structuretensors abs'
    if not output:
        output = f"{Path(input).stem}_delimited_contour.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def contourdetails(input, output):
    """Delimits the outline of the figures and details in the image."""

    instruction = 'structuretensors abs pow 1.2'
    if not output:
        output = f"{Path(input).stem}_details_contour.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def enhancesblurring(input, output):
    """Blurs and enhances the shapes of the image."""

    instruction = 'blur 7 unsharp 3.5,35 cut 0,255'
    if not output:
        output = f"{Path(input).stem}_details_contour.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def vanvliet(input, output):
    """Applies vanvliet effect in the image."""

    instruction = 'vanvliet 3,1,x'
    if not output:
        output = f"{Path(input).stem}_vanvliet.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def colordots(input, output):
    """Applies color dots effect in the image."""

    instruction = 'stencil 1'
    if not output:
        output = f"{Path(input).stem}_colordots.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def bwdots(input, output):
    """Applies black and white dots effect in the image."""

    instruction = 'luminance stencil 1'
    if not output:
        output = f"{Path(input).stem}_colordots.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def outline(input, output):
    """Draw only the outline of the image."""

    instruction = 'blur 2 isophotes 6 dilate_circ 5'
    if not output:
        output = f"{Path(input).stem}_colordots.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def fineoutline(input, output):
    """Draw only the fine outline of the image."""

    instruction = 'blur 2 isophotes 6'
    if not output:
        output = f"{Path(input).stem}_colordots.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def cracked(input, output):
    """Draw only the fine outline of the image."""

    instruction = f'+srgb2lab slic[-1] 16 +blend shapeaverage f[-2] "j(1,0)==i && j(0,1)==i" *[-1] [-2]'

    temp_files = random_filename()

    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    if not output:
        output = f"{Path(input).stem}_cracked.png"

    shutil.copyfile(image[0], output)

    for del_image in generated_images:
        os.remove(del_image)

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lowlevel(input, output):
    """Define the image by lowering the level."""

    instruction = f'+equalize[0] 256 +apply_tiles[0] "equalize 256",16,16,1,50%,50%'

    temp_files = random_filename()

    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*1*')
    if not output:
        output = f"{Path(input).stem}_lowlevel.png"

    shutil.copyfile(image[0], output)

    for del_image in generated_images:
        os.remove(del_image)

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def projectcontours(input, output):
    """Project the contours of the image."""

    instruction = f'+equalize[0] 256 +apply_tiles[0] "equalize 256",16,16,1,50%,50%'

    temp_files = random_filename()

    gmic.run(f'{input} {instruction} output {temp_files}')

    generated_images = glob.glob(f'{Path(temp_files).stem}*')
    image = glob.glob(f'{Path(temp_files).stem}*2*')
    if not output:
        output = f"{Path(input).stem}_projectcontours.png"

    shutil.copyfile(image[0], output)

    for del_image in generated_images:
        os.remove(del_image)

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def outlineonblack(input, output):
    """Draw outline on black to the received image."""

    instruction = f"variance_patch 12"
    if not output:
        output = f"{Path(input).stem}_tones.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def thirdpartyguides(input, output):
    """Draw third party guides to the received image."""

    instruction = f"grid 33.33%,33.33%,-1,-1,1,255"
    if not output:
        output = f"{Path(input).stem}_thirdpartyguides.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def greyish(input, output):
    """Transforms the image into gray tones."""

    instruction = '+blur 5 sub normalize 0,255'
    if not output:
        output = f"{Path(input).stem}_greyish.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def fourfour(input, output):
    """Applies a four-by-four blurred array effect."""

    instruction = 'array_fade 4,4'
    if not output:
        output = f"{Path(input).stem}_tones.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def arraymirror(input, output):
    """Applies array mirror effect to the received image."""

    instruction = 'array_mirror 1'
    if not output:
        output = f"{Path(input).stem}_arraymirror.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def vignetteblur(input, output):
    """Applies vignette blur to the received image."""

    instruction = 'frame_blur 3,30,8,10%'
    if not output:
        output = f"{Path(input).stem}_vignetteblur.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def rotatetiles(input, output):
    """Draw rotate tiles to the received image."""

    instruction = 'to_rgba rotate_tiles 10,8 drop_shadow 10,10 display_rgba'
    if not output:
        output = f"{Path(input).stem}_rotate_tiles.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def shifttiles(input, output):
    """Applies shift tiles to the received image."""

    instruction = 'shift_tiles 8,8,10'
    if not output:
        output = f"{Path(input).stem}_shift_tiles.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def intensestains(input, output):
    """Applies intense stains texture to the received image."""

    instruction = 'cartoon 20,111,74,39.03,8.59,175'
    if not output:
        output = f"{Path(input).stem}_intensestains.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def vinylstains(input, output):
    """Applies intense stains texture to the received image."""

    instruction = 'cartoon 25,98,52,81.99,4.97,31'
    if not output:
        output = f"{Path(input).stem}_vinylstains.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def oilstains(input, output):
    """Applies oil stains texture to the received image."""

    instruction = 'cartoon 4,130,142,54.86,17.18,119'
    if not output:
        output = f"{Path(input).stem}_oilstains.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def fingerpaint(input, output):
    """Applies finger paint texture to the received image."""

    instruction = 'cartoon 11,117,26,35.23,21.99,69'
    if not output:
        output = f"{Path(input).stem}_fingerpaint.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def woodpaint(input, output):
    """Applies wood paint texture to the received image."""

    instruction = 'cartoon 0,107,171,171.78,6.12,162 blur 1'
    if not output:
        output = f"{Path(input).stem}_woodpaint.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def mural(input, output):
    """Applies mural texture to the received image."""

    instruction = 'cartoon 0,51,69,57.5,3.72,146'
    if not output:
        output = f"{Path(input).stem}_mural.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def colorfulmural(input, output):
    """Applies colorful mural texture to the received image."""

    instruction = 'cartoon 0,107,75,161.55,4.4,93'
    if not output:
        output = f"{Path(input).stem}_colorfulmural.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def greatpointillism(input, output):
    """Applies great pointillism texture to the received image."""

    instruction = 'cartoon 5,56,79,126.82,8.58,163'
    if not output:
        output = f"{Path(input).stem}_greatpointillism.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def flattenscolors(input, output):
    """Applies flattens colors texture to the received image."""

    instruction = 'cartoon 6,113,143,64.36,3.96,78'
    if not output:
        output = f"{Path(input).stem}_flattenscolors.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def flattenscolorsbw(input, output):
    """Applies flattens colors in black and white texture to the received image."""

    instruction = 'cartoon 6,131,20,157.73,0.08,167'
    if not output:
        output = f"{Path(input).stem}_flattenscolorsbw.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def uniformink(input, output):
    """Applies uniform ink texture to the received image."""

    instruction = 'cartoon 7,112,145,145.09,5.7,78'
    if not output:
        output = f"{Path(input).stem}_uniformink.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def aqueousink(input, output):
    """Applies aqueous ink texture to the received image."""

    instruction = 'cartoon 8,64,123,167.82,7.66,173'
    if not output:
        output = f"{Path(input).stem}_aqueousink.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def brightdetails(input, output):
    """Applies bright details texture to the received image."""

    instruction = 'cartoon 8,145,55,165.72,23.25,195'
    if not output:
        output = f"{Path(input).stem}_brightdetails.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def pressing(input, output):
    """Applies pressing texture to the received image."""

    instruction = 'cartoon 9,146,41,37.4,0.34,134'
    if not output:
        output = f"{Path(input).stem}_pressing.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def colorsketch(input, output):
    """Applies color sketch texture to the received image."""

    instruction = 'cartoon 10,90,171,56.34,3.81,37'
    if not output:
        output = f"{Path(input).stem}_colorsketch.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def flatcomic(input, output):
    """Applies flat comic texture to the received image."""

    instruction = 'cartoon 9,127,158,60.95,6.1,100'
    if not output:
        output = f"{Path(input).stem}_flatcomic.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def hero(input, output):
    """Applies hero texture to the received image."""

    instruction = 'cartoon 8,148,188,56.23,10.25,183'
    if not output:
        output = f"{Path(input).stem}_hero.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def handstrokes(input, output):
    """Applies hand strokes texture to the received image."""

    instruction = 'cartoon 8,81,26,125.74,17.21,199'
    if not output:
        output = f"{Path(input).stem}_handstrokes.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def uniformstains(input, output):
    """Applies uniform stains texture to the received image."""

    instruction = 'cartoon 6,58,109,139.49,19.61,180 blur 1'
    if not output:
        output = f"{Path(input).stem}_uniformstains.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def colorareas(input, output):
    """Applies color areas texture to the received image."""

    instruction = 'cartoon 5,87,125,70.78,2.05,164'
    if not output:
        output = f"{Path(input).stem}_colorareas.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def coloredmarker(input, output):
    """Applies colored with marker texture to the received image."""

    instruction = 'cartoon 5,144,111,160.23,8.71,42'
    if not output:
        output = f"{Path(input).stem}_coloredmarker.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def intenseposter(input, output):
    """Applies intense poster texture to the received image."""

    instruction = 'cartoon 4,80,37,139.24,2.37,40'
    if not output:
        output = f"{Path(input).stem}_intenseposter.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def colourstains(input, output):
    """Applies colour stains texture to the received image."""

    instruction = 'cartoon 3,102,71,173.45,4.27,35'
    if not output:
        output = f"{Path(input).stem}_colourstains.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def airbrushing(input, output):
    """Applies airbrushing texture to the received image."""

    instruction = 'cartoon 0,51,69,57.5,3.72,146'
    if not output:
        output = f"{Path(input).stem}_airbrushing.png"
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

    instruction = 'color_ellipses ,,0.15'
    if not output:
        output = f"{Path(input).stem}_color_ellipses.png"
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
    """Applies cubism texture to the received image."""

    instruction = 'cubism ,'
    if not output:
        output = f"{Path(input).stem}_cubism.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def drawing(input, output):
    """Applies drawing texture to the received image."""

    instruction = 'drawing ,'
    if not output:
        output = f"{Path(input).stem}_drawing.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def fireedges(input, output):
    """Applies fire edges texture to the received image."""

    instruction = 'fire_edges ,'
    if not output:
        output = f"{Path(input).stem}_fire_edges.png"
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
    """Applies fire edges texture to the received image."""

    instruction = 'fractalize ,'
    if not output:
        output = f"{Path(input).stem}_fractalize.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def ellipsionism(input, output):
    """Applies ellipsionism texture to the received image."""

    instruction = 'ellipsionism ,'
    if not output:
        output = f"{Path(input).stem}_ellipsionism.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def blurrysketch(input, output):
    """Applies blurry sketch texture to the received image."""

    instruction = 'hardsketchbw 200,70,0.1,10 median 2 reverse blur 3 blend overlay'
    if not output:
        output = f"{Path(input).stem}_blurry_sketch.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def hardsketchbw(input, output):
    """Applies blurry sketch texture to the received image."""

    instruction = 'hardsketchbw 200,70,0.1,10 median 2 reverse'
    if not output:
        output = f"{Path(input).stem}_hardsketchbw.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def handsketch(input, output):
    """Applies blurry sketch texture to the received image."""

    instruction = 'hardsketchbw 100,50,0.1,10'
    if not output:
        output = f"{Path(input).stem}_handsketch.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--intensity', type=int, default=25, help='linify intensity')
def linify(input, output, intensity):
    """Applies linify effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_linify.png"

    instruction = "linify"
    gmic.run(f'{input} {instruction} {intensity} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def pencilbw(input, output):
    """Applies pencil black and white texture to the received image."""

    instruction = 'pencilbw ,'
    if not output:
        output = f"{Path(input).stem}_pencilbw.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def posteredges(input, output):
    """Applies poster edges texture to the received image."""

    instruction = 'poster_edges ,'
    if not output:
        output = f"{Path(input).stem}_poster_edges.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def subtledrawing(input, output):
    """Applies subtle texture to the received image."""

    instruction = 'normalize_local 10,16 smooth 60,0,1,1,4 normalize_local 10,16'
    if not output:
        output = f"{Path(input).stem}_subtle_drawing.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def multicross(input, output):
    """Applies multi cross texture to the received image."""

    instruction = 'sponge 3'
    if not output:
        output = f"{Path(input).stem}_subtle_drawing.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def stainsbw(input, output):
    """Applies stains black and white to the received image."""

    instruction = 'stencilbw 7,0'
    if not output:
        output = f"{Path(input).stem}_stainsbw.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def areasbw(input, output):
    """Applies areas black and white to the received image."""

    instruction = 'stencilbw 18,24'
    if not output:
        output = f"{Path(input).stem}_areasbw.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def inked(input, output):
    """Applies inked black and white texture to the received image."""

    instruction = 'stencilbw 25,3'
    if not output:
        output = f"{Path(input).stem}_inked.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def inkedhardstroke(input, output):
    """Applies inked black and white with hard stroke texture to the received image."""

    instruction = 'stencilbw 37,6'
    if not output:
        output = f"{Path(input).stem}_inkedhardstroke.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def roundedstains(input, output):
    """Applies rounded stains black and white texture to the received image."""

    instruction = 'stencilbw 48,30'
    if not output:
        output = f"{Path(input).stem}_roundedstains.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def rorschach(input, output):
    """Applies rorschach black and white texture to the received image."""

    instruction = 'stencilbw 59,19'
    if not output:
        output = f"{Path(input).stem}_rorschach.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def rainbw(input, output):
    """Applies rain black and white texture to the received image."""

    instruction = 'stencilbw 6,86'
    if not output:
        output = f"{Path(input).stem}_rainbw.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def multilinebw(input, output):
    """Applies multi line black and white texture to the received image."""

    instruction = 'stencilbw 12,100'
    if not output:
        output = f"{Path(input).stem}_multilinebw.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def subtlewhirls(input, output):
    """Applies subtle whirls texture to the received image."""

    instruction = 'whirls ,'
    if not output:
        output = f"{Path(input).stem}_subtlewhirls.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def ripple(input, output):
    """Applies ripple texture to the received image."""

    instruction = 'ripple ,'
    if not output:
        output = f"{Path(input).stem}_ripple.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def rotoidoscope(input, output):
    """Applies rotoidoscope texture to the received image."""

    instruction = 'rotoidoscope ,'
    if not output:
        output = f"{Path(input).stem}_rotoidoscope.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def rotatedcross(input, output):
    """Applies rotated cross effect to the received image."""

    instruction = 'transform_polar r,2*a'
    if not output:
        output = f"{Path(input).stem}_rotatedcross.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def inflates(input, output):
    """Applies inflates effect to the received image."""

    instruction = 'transform_polar R*(r/R)^2,a'
    if not output:
        output = f"{Path(input).stem}_inflates.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def implosion(input, output):
    """Applies implosion effect to the received image."""

    instruction = 'transform_polar R-(r/R)^2,a'
    if not output:
        output = f"{Path(input).stem}_implosion.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def recreation(input, output):
    """Applies recreation effect to the received image."""

    instruction = 'transform_polar "R-r",a'
    if not output:
        output = f"{Path(input).stem}_recreation.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def warpperspective(input, output):
    """Applies warp perspective effect to the received image."""

    instruction = 'warp_perspective ,'
    if not output:
        output = f"{Path(input).stem}_warp_perspective.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def breeze(input, output):
    """Applies breeze effect to the received image."""

    instruction = 'wind ,'
    if not output:
        output = f"{Path(input).stem}_breeze.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def pixelize(input, output):
    """Applies pixelize effect to the received image."""

    instruction = 'pixelize ,'
    if not output:
        output = f"{Path(input).stem}_pixelize.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def texturizepaper(input, output):
    """Applies paper texture to the received image."""

    instruction = 'texturize_paper'
    if not output:
        output = f"{Path(input).stem}_texturize_paper.png"
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
    """Applies frame fuzzy to the received image."""

    instruction = 'frame_fuzzy 20'
    if not output:
        output = f"{Path(input).stem}_frame_fuzzy.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def framecube(input, output):
    """Applies frame cube effect to the received image."""

    instruction = 'frame_cube ,'
    if not output:
        output = f"{Path(input).stem}_frame_cube.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def dottedbw(input, output):
    """Applies dotted black and white to the received image."""

    instruction = f"rgb2bayer 1"
    if not output:
        output = f"{Path(input).stem}_dottedbw.png"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darktogarnet(input, output):
    """Applies garnet to dark areas of the image."""

    instruction = "balance_gamma 128,64,64"

    if not output:
        output = f"{Path(input).stem}_dark_to_garnet.png"

    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkandoutline(input, output):
    """Applies dark and outline effect to the received image."""

    instruction = "gradient pow 8 add pow 0.1"

    if not output:
        output = f"{Path(input).stem}_dark_and_outline.png"

    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def clarified(input, output):
    """Applies clarified tones to the received image."""

    instruction = "div 255 pow 0.5 mul 255"

    if not output:
        output = f"{Path(input).stem}_clarified.png"

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
@click.option('--intensity', type=int, default=5, help='Taquin intensity')
def taquin(input, output, intensity):
    """Applies taquin effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_taquin.png"

    instruction = "taquin"
    gmic.run(f'{input} {instruction} {intensity} output {output}')

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
@click.option('--intensity', type=int, default=10, help='Blur intensity')
def saltnoise(input, output, intensity):
    """Applies salt noise effect to the received image."""

    if not output:
        output = f"{Path(input).stem}_saltnoise.png"

    instruction = f"noise {intensity},2"
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
def breaksstains(input, output):
    """Breaks stains of the received image."""

    if not output:
        output = f"{Path(input).stem}_normalize_local.png"

    instruction = "normalize_local 83,21"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def fog(input, output):
    """Applies fog filter to the received image."""

    if not output:
        output = f"{Path(input).stem}_normalize_local.png"

    instruction = "normalize_local 53,53"
    gmic.run(f'{input} {instruction} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def luster(input, output):
    """Applies luster filter to the received image."""

    if not output:
        output = f"{Path(input).stem}_normalize_local.png"

    instruction = "normalize_local 45,20"
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
        output = f"{Path(input).stem}_gridhexagonal.png"

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
        output = f"{Path(input).stem}_fx_bokeh.png"

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
