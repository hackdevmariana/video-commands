#!/usr/bin/env python3

from pathlib import Path
from random import randint, uniform, choice
import click
import colorama
import gmic


@click.group()
def cli():
    pass

def apply_filter(input, output, filter_cmd, suffix):
    """Applies a GMIC filter to the input image and saves the output."""
    if not output:
        output = f"{Path(input).stem}_{suffix}.png"

    gmic.run(f'{input} {filter_cmd} output {output}')

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created {colorama.Fore.GREEN}successfully{colorama.Style.RESET_ALL}: {output}")
    else:
        click.echo(f"An {colorama.Fore.RED}error{colorama.Style.RESET_ALL} occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def sponged(input, output):
    """Transforms the received image into a mask with a fluffy texture."""
    apply_filter(input, output, 'sponge 11 luminance', 'mask_sponged')

if __name__ == '__main__':
    colorama.init()  # Initialize colorama
    cli()
