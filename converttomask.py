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

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def portrait(input, output):
    """Transforms the received image into a mask with a portrait texture."""
    apply_filter(input, output, 'stencilbw 55,2', 'mask_portrait')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def punk(input, output):
    """Transforms the received image into a mask with a punk fanzine texture."""
    apply_filter(input, output, 'stencilbw 66,10', 'mask_punk')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def fanzine(input, output):
    """Transforms the received image into a mask with a fanzine texture."""
    apply_filter(input, output, 'stencilbw 74,0', 'mask_fanzine')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def doctordoom(input, output):
    """Transforms the received image into a mask with a Doctor Doom comic texture."""
    apply_filter(input, output, 'stencilbw 77,1', 'mask_doctordoom')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def pulp(input, output):
    """Transforms the received image into a mask with a pulp comic texture."""
    apply_filter(input, output, 'stencilbw 92,4', 'mask_pulp')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def machete(input, output):
    """Transforms the received image into a mask with a series b comic texture."""
    apply_filter(input, output, 'stencilbw 95,1', 'mask_machete')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def grindhouse(input, output):
    """Transforms the received image into a mask with a series b comic texture."""
    apply_filter(input, output, 'stencilbw 106,3', 'mask_grindhouse')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def imprecise(input, output):
    """Transforms the received image into a mask with an imprecise spots texture."""
    apply_filter(input, output, 'stencilbw 114,16', 'mask_imprecise')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def poster(input, output):
    """Transforms the received image into a mask with an BW poster texture."""
    apply_filter(input, output, 'tetris 94,95 luminance', 'mask_poster')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def pixelate(input, output):
    """Transforms the received image into a mask with an pixelate texture."""
    apply_filter(input, output, 'tetris 18,132 luminance', 'mask_pixelate')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def tissue(input, output):
    """Transforms the received image into a mask with a tissue texture."""
    apply_filter(input, output, 'texturize_canvas 59,150,38 fx_paper 10,66 luminance', 'mask_tissue')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def sack(input, output):
    """Transforms the received image into a mask with a sack texture."""
    apply_filter(input, output, 'texturize_canvas 69,94,60 fx_paper 26,97 luminance', 'mask_sack')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def plasteredwall(input, output):
    """Transforms the received image into a mask with a plastered wall texture."""
    apply_filter(input, output, 'texturize_canvas 106,4,88 fx_paper 18,60 luminance', 'mask_plasteredwall')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def coatedpaper(input, output):
    """Transforms the received image into a mask with a coated paper texture."""
    apply_filter(input, output, 'texturize_canvas 65,5,0 luminance', 'mask_coatedpaper')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def burlap(input, output):
    """Transforms the received image into a mask with a burlap texture."""
    apply_filter(input, output, 'texturize_canvas 80,17,109 luminance', 'mask_burlap')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def charcoal(input, output):
    """Transforms the received image into a mask with a charcoal texture."""
    apply_filter(input, output, 'unsharp 49,104 luminance', 'mask_charcoal')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def sincitybw(input, output):
    """Transforms the received image into a mask with a Sin City texture."""
    apply_filter(input, output, 'unsharp 149,70 luminance', 'mask_sincitybw')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def detail(input, output):
    """Transforms the received image into a mask with a detailed texture."""
    apply_filter(input, output, 'unsharp 1,37 luminance', 'mask_detail')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def street(input, output):
    """Transforms the received image into a mask with a street portrait texture."""
    apply_filter(input, output, 'unsharp 2,103 luminance', 'mask_street')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def intensified(input, output):
    """Transforms the received image into a mask with an intensified texture."""
    apply_filter(input, output, 'unsharp 4,4 luminance', 'mask_street')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def contrasted(input, output):
    """Transforms the received image into a mask with an contrasted texture."""
    apply_filter(input, output, 'unsharp 5,145 luminance', 'mask_contrasted')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def nuanced(input, output):
    """Transforms the received image into a mask with a nuanced contrast texture."""
    apply_filter(input, output, 'unsharp 5,145 blur 5 luminance', 'mask_nuanced')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def trembling(input, output):
    """Transforms the received image into a mask with a trembling texture."""
    apply_filter(input, output, 'wave , fx_unsharp_richardsonlucy 12,108,91,40,141 luminance', 'mask_trembling')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def concentricglitch(input, output):
    """Transforms the received image into a mask with a concentric glitch texture."""
    apply_filter(input, output, 'wave , fx_unsharp_richardsonlucy 4,137,139,51,67 luminance', 'mask_concentricglitch')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def irregular(input, output):
    """Transforms the received image into a mask with a irregular texture."""
    apply_filter(input, output, 'wave , fx_unsharp_richardsonlucy 8,132,74,6,96 luminance', 'mask_irregular')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def brushstroke(input, output):
    """Transforms the received image into a mask with an brushstroke texture."""
    apply_filter(input, output, 'wave , fx_unsharp_richardsonlucy 13,38,137,78,11 luminance', 'mask_brushstroke')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def diagonaldoodle(input, output):
    """Transforms the received image into a mask with a diagonal doodle texture."""
    apply_filter(input, output, 'apply_gamma 1.0,2.0,0.3 fx_pencil_portraitbw 122,134,3,129,119,72,147,54 luminance', 'mask_diagonaldoodle')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def microlines(input, output):
    """Transforms the received image into a mask with a micro lines texture."""
    apply_filter(input, output, 'apply_gamma 1.2,1.5,0.3 fx_pencil_portraitbw 18,43,5,107,103,11,108,130 luminance', 'mask_microlines')

if __name__ == '__main__':
    colorama.init()  # Initialize colorama
    cli()
