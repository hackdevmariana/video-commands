#!/usr/bin/env python3

from pathlib import Path

import click
import colorama
import gmic
import PIL.Image

from PIL import ImageChops, Image

from video_commands_lib import random_filename

effects = ['old_photo', 'stained_glass', 'poster_hope', 'polygon', 'sketch', 'lifiny', 'paloraid', 'cubism', 'vector_paint', 'cartoon', 'poster', 'pencil', 'paint', 'edge_fire', 'boxfitting', 'color_abstraction', 'freaky_details', 'gogh', 'polloc', 'klee', 'picasso', 'blur', 'bokeh', 'shine', 'diamond']

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
    gmic.run(f'{input} fx_engrave 0.2,2,0,1.34,1.1,0,0,1,5,1,0,0,0,1,0 gui_merge_layers output {temp_file}')

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
        output = f"{Path(input).stem}_poster_hope.png"

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



if __name__ == '__main__':
    cli()
