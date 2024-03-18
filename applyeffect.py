#!/usr/bin/env python3

from pathlib import Path

import click
import colorama
import gmic
import PIL.Image

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





if __name__ == '__main__':
    cli()
