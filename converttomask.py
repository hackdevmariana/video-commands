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

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def whirl(input, output):
    """Transforms the received image into a mask with a whirl texture."""
    apply_filter(input, output, 'draw_whirl 18 luminance', 'mask_whirl')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def eddy(input, output):
    """Transforms the received image into a mask with an eddy texture."""
    apply_filter(input, output, 'draw_whirl 232 luminance', 'mask_eddy')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def inked(input, output):
    """Transforms the received image into a mask with an inked texture."""
    apply_filter(input, output, 'stencilbw 70', 'mask_inked')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def hardrain(input, output):
    """Transforms the received image into a mask with a hard rain texture."""
    apply_filter(input, output, 'stencilbw 2,122 blur_y 10', 'mask_hardrain')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def torrential(input, output):
    """Transforms the received image into a mask with a torrential rain texture."""
    apply_filter(input, output, 'stencilbw 5,111 blur_y 5', 'mask_torrential')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def rainyday(input, output):
    """Transforms the received image into a mask with a rainy day texture."""
    apply_filter(input, output, 'stencilbw 6,111 blur_y 3', 'mask_rainyday')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def multistroke(input, output):
    """Transforms the received image into a mask with a multi stroke texture."""
    apply_filter(input, output, 'stencilbw 7,23', 'mask_multistroke')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def horizontalmultiline(input, output):
    """Transforms the received image into a mask with a horizontal multi line texture."""
    apply_filter(input, output, 'stencilbw 13,144', 'mask_horizontalmultiline')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def chineseink(input, output):
    """Transforms the received image into a mask with a Chinese ink texture."""
    apply_filter(input, output, 'stencilbw 20,4', 'mask_chineseink')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def markerpen(input, output):
    """Transforms the received image into a mask with a marker pen texture."""
    apply_filter(input, output, 'stencilbw 32,4', 'mask_markerpen')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def diffusespots(input, output):
    """Transforms the received image into a mask with a marker pen texture."""
    apply_filter(input, output, 'stencilbw 36,37 blur 10', 'mask_diffusespots')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def harddarkening(input, output):
    """Transforms the received image into a mask with a hard darkening texture."""
    apply_filter(input, output, 'stencilbw 41,17', 'mask_harddarkening')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def diffusedarkening(input, output):
    """Transforms the received image into a mask with a diffuse darkening texture."""
    apply_filter(input, output, 'stencilbw 41,17 blur 5', 'mask_diffusedarkening')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def oldcomic(input, output):
    """Transforms the received image into a mask with an old comic texture."""
    apply_filter(input, output, 'stencilbw 48,9', 'mask_oldcomic')

    
if __name__ == '__main__':
    colorama.init()  # Initialize colorama
    cli()
