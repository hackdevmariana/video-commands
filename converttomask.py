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

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def washink(input, output):
    """Transforms the received image into a mask with a wash ink texture."""
    apply_filter(input, output, 'apply_gamma 1.3,0.3,0.6 fx_pencil_portraitbw 25,144,35,54,82,8,85,40 luminance', 'mask_washink')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def dottedoutline(input, output):
    """Transforms the received image into a mask with a dotted outline texture."""
    apply_filter(input, output, 'apply_gamma 1.5,0.7,0.9 fx_pencil_portraitbw 6,146,7,138,125,89,118,109 luminance', 'mask_dottedoutline')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def diagonalstrokes(input, output):
    """Transforms the received image into a mask with a diagonal strokes texture."""
    apply_filter(input, output, 'apply_gamma 1.7,0.9,0.1 fx_pencil_portraitbw 87,139,6,59,18,66,56,89 luminance', 'mask_diagonalstrokes')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def verticalstrokes(input, output):
    """Transforms the received image into a mask with a vertical strokes texture."""
    apply_filter(input, output, 'apply_gamma 1.8,0.2,1.4 fx_pencil_portraitbw 103,88,5,113,0,113,41,28 luminance', 'mask_verticalstrokes')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def fallingstrokes(input, output):
    """Transforms the received image into a mask with a falling strokes texture."""
    apply_filter(input, output, 'apply_gamma 1.8,1.0,2.0 fx_pencil_portraitbw 113,76,4,87,54,96,121,82 luminance', 'mask_fallingstrokes')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def treetrunk(input, output):
    """Transforms the received image into a mask with a tree trunk texture."""
    apply_filter(input, output, 'apply_gamma 1.8,1.5,0.9 fx_pencil_portraitbw 130,88,0,52,91,107,21,57 luminance', 'mask_treetrunk')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def aquarelle(input, output):
    """Transforms the received image into a mask with a aquarelle texture."""
    apply_filter(input, output, 'apply_gamma 1.9,1.2,0.6 fx_pencil_portraitbw 138,98,14,120,62,13,12,147 luminance', 'mask_aquarelle')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def onlylight(input, output):
    """Transforms the received image into a mask with a only light texture."""
    apply_filter(input, output, 'apply_gamma 0.1,0.4,0.5 fx_pencil_portraitbw 7,20,26,59,26,59,113,39 luminance', 'mask_onlylight')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def waxgray(input, output):
    """Transforms the received image into a mask with a wax gray texture."""
    apply_filter(input, output, 'apply_gamma 0.3,0.4,1.9 fx_pencil_portraitbw 34,126,112,63,32,147,29,82 luminance', 'mask_waxgray')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def waxpaint(input, output):
    """Transforms the received image into a mask with a wax paint texture."""
    apply_filter(input, output, 'apply_gamma 0.4,0.5,0.2 fx_pencil_portraitbw 38,83,26,72,108,118,50,94 luminance', 'mask_waxpaint')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def hair(input, output):
    """Transforms the received image into a mask with a hair texture."""
    apply_filter(input, output, 'apply_gamma 0.4,1.7,1.8 fx_pencil_portraitbw 86,52,7,149,43,61,92,100 luminance', 'mask_hair')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def sketch(input, output):
    """Transforms the received image into a mask with a sketch texture."""
    apply_filter(input, output, 'apply_gamma 0.8,1.7,0.5 fx_pencil_portraitbw 43,93,7,138,52,53,133,124 luminance', 'mask_sketch')


@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def silver(input, output):
    """Transforms the received image into a mask with a silver texture."""
    apply_filter(input, output, 'apply_gamma 0.5,1.9,1.1 structuretensors gt luminance', 'mask_silver')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def iron(input, output):
    """Transforms the received image into a mask with an iron texture."""
    apply_filter(input, output, 'apply_gamma 0.6,0.9,1.8 structuretensors lt luminance', 'mask_iron')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def ironmaiden(input, output):
    """Transforms the received image into a mask with an iron maiden texture."""
    apply_filter(input, output, 'apply_gamma 0.6,1.4,0.8 structuretensors xor luminance', 'mask_ironmaiden')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def whiteboard(input, output):
    """Transforms the received image into a mask with a whiteboard texture."""
    apply_filter(input, output, 'fx_pencil_portraitbw 33,40,73,77,44,136 structuretensors mod luminance', 'mask_whiteboard')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def diagonalscraping(input, output):
    """Transforms the received image into a mask with a diagonal scraping texture."""
    apply_filter(input, output, 'fx_pencil_portraitbw 63,122,3,142,139,93,2,124 structuretensors abs luminance', 'mask_diagonalscraping')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def scratchedsilver(input, output):
    """Transforms the received image into a mask with a scratched silver texture."""
    apply_filter(input, output, 'fx_pencil_portraitbw 83,21,0,115,4,3,66,53 structuretensors bsr luminance', 'mask_scratchedsilver')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def chalk(input, output):
    """Transforms the received image into a mask with a chalk texture."""
    apply_filter(input, output, 'fx_pencil_portraitbw 103,1,61,6,69,71,6,33 structuretensors mul luminance', 'mask_chalk')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def shell(input, output):
    """Transforms the received image into a mask with a shell texture."""
    apply_filter(input, output, 'fx_pencil_portraitbw 13,44,146,10,142,69,71,26 structuretensors sqrt luminance', 'mask_shell')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def greasepencil(input, output):
    """Transforms the received image into a mask with a grease pencil texture."""
    apply_filter(input, output, 'balance_gamma 65.2 sketchbw 56,11', 'mask_greasepencil')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def airbrushedoutline(input, output):
    """Transforms the received image into a mask with a airbrushed outline texture."""
    apply_filter(input, output, 'blend 77 sketchbw 73,93.4', 'mask_airbrushedoutline')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darling(input, output):
    """Transforms the received image into a mask with a darling texture."""
    apply_filter(input, output, 'cracks 61,94.1,48.7,91.7,57.2 fx_pen_drawing 48.6,98,41,36 luminance', 'mask_darling')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def uniformareas(input, output):
    """Transforms the received image into a mask with an uniform areas texture."""
    apply_filter(input, output, 'cracks 85,21,49,58.3,93.4 cartoon 8.3,95 luminance', 'mask_uniformareas')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def spectrum(input, output):
    """Transforms the received image into a mask with a spectrum texture."""
    apply_filter(input, output, 'cracks 110,4,125,28,0 fx_pen_drawing 105,136,25 luminance', 'mask_spectrum')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def gosh(input, output):
    """Transforms the received image into a mask with a gosh texture."""
    apply_filter(input, output, 'cracks 112,65,88,145,100 fx_pen_drawing 131,1,114 luminance', 'mask_gosh')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def spook(input, output):
    """Transforms the received image into a mask with a spook texture."""
    apply_filter(input, output, 'cracks 133,20,37,116,141 fx_pen_drawing 55,55,92 luminance', 'mask_spook')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def greyspook(input, output):
    """Transforms the received image into a mask with a grey spook texture."""
    apply_filter(input, output, 'cracks 135,33,34,116,43 fx_pen_drawing 25,68,138 luminance', 'mask_greyspook')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def mild(input, output):
    """Transforms the received image into a mask with a mild texture."""
    apply_filter(input, output, 'cracks 135,53,35,124,11 fx_pen_drawing 84,99,45 luminance', 'mask_mild')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def stencil(input, output):
    """Transforms the received image into a mask with a stencil texture."""
    apply_filter(input, output, 'cracks 137,113,36,123,93 fx_pen_drawing 8,31,103 luminance', 'mask_stencil')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def bogey(input, output):
    """Transforms the received image into a mask with a bogey texture."""
    apply_filter(input, output, 'cracks 140,93,5,131,105 fx_pen_drawing 31,1,79 luminance', 'mask_bogey')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def silky(input, output):
    """Transforms the received image into a mask with a silky texture."""
    apply_filter(input, output, 'cracks 0,135,73,88,62 fx_pen_drawing 41,18,112 luminance', 'mask_silky')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def sharp(input, output):
    """Transforms the received image into a mask with a sharp texture."""
    apply_filter(input, output, 'cracks 4,71,112,73,50 fx_pen_drawing 7,34,28 luminance', 'mask_sharp')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def spider(input, output):
    """Transforms the received image into a mask with a spider web texture."""
    apply_filter(input, output, 'cracks 12,144,135,30,34 fx_pen_drawing 36,66,39 luminance', 'mask_spider')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def spiderweb(input, output):
    """Transforms the received image into a mask with a spider web texture."""
    apply_filter(input, output, 'cracks 14,37,62,42,77 fx_pen_drawing 38,79,46 luminance', 'mask_spiderweb')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def cobweb(input, output):
    """Transforms the received image into a mask with a spider web texture."""
    apply_filter(input, output, 'cracks 15,45,21,12,43 fx_pen_drawing 147,75,111 luminance', 'mask_cobweb')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def neuronal(input, output):
    """Transforms the received image into a mask with a neuronal texture."""
    apply_filter(input, output, 'cracks 29,123,78,123,66 fx_pen_drawing 134,2,61 luminance', 'mask_neuronal')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def scrapedcoating(input, output):
    """Transforms the received image into a mask with a scraped coating texture."""
    apply_filter(input, output, 'cracks 35,5,129,127,22 fx_pen_drawing 117,70,75 luminance', 'mask_scrapedcoating')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def granite(input, output):
    """Transforms the received image into a mask with a granite texture."""
    apply_filter(input, output, 'cracks 35,76,118,94,134 fx_pen_drawing 87,84,36 luminance', 'mask_granite')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def slippery(input, output):
    """Transforms the received image into a mask with a slippery texture."""
    apply_filter(input, output, 'cracks 48,105,81,34,45 fx_pen_drawing 150,14,138 luminance', 'mask_slippery')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def splashes(input, output):
    """Transforms the received image into a mask with a splashes texture."""
    apply_filter(input, output, 'cracks 49,141,18,43,111 fx_pen_drawing 114,130,4 luminance', 'mask_splashes')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def dripping(input, output):
    """Transforms the received image into a mask with a dripping texture."""
    apply_filter(input, output, 'cracks 50,93,3,54,139 fx_pen_drawing 66,147,82 luminance', 'mask_dripping')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def scratches(input, output):
    """Transforms the received image into a mask with a scratches texture."""
    apply_filter(input, output, 'cracks 63,58,13,141,81 fx_pen_drawing 33,23,85 luminance', 'mask_scratches')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def stenciled(input, output):
    """Transforms the received image into a mask with a stenciled texture."""
    apply_filter(input, output, 'cracks 74,103,88,41,145 fx_pen_drawing 38,27,112 luminance', 'mask_stenciled')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def dottedgray(input, output):
    """Transforms the received image into a mask with a dotted gray texture."""
    apply_filter(input, output, 'cracks 77,9,143,74,81 fx_pen_drawing 142,46,148 luminance', 'mask_dottedgray')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def diffuseoutline(input, output):
    """Transforms the received image into a mask with a diffuse outline texture."""
    apply_filter(input, output, 'dog 33,24,93,150,20,11 whirls 55,100,72,85,70,10,6,119,121 luminance', 'mask_diffuseoutline')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def blurredoutline(input, output):
    """Transforms the received image into a mask with a blurred outline texture."""
    apply_filter(input, output, 'dog 39,29,91,108,110,108 whirls 17,52,18,50,147,9,101,140,126 luminance', 'mask_blurredoutline')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def gaussianoutline(input, output):
    """Transforms the received image into a mask with a gaussian outline texture."""
    apply_filter(input, output, 'dog 39,88,112,115,35,146 whirls 6,41,22,21,124,139,87,74,38 luminance', 'mask_gaussianoutline')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def spray(input, output):
    """Transforms the received image into a mask with a spray outline texture."""
    apply_filter(input, output, 'dog 43,33,121,69,118,58 whirls 15,145,0,10,74,129,84,41,132 luminance', 'mask_sprayutline')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def contrastedgaussian(input, output):
    """Transforms the received image into a mask with a contrasted gaussian outline texture."""
    apply_filter(input, output, 'dog 43,49,17,28,147,113 whirls 87,77,108,15,3,26,134,80,42 luminance', 'mask_contrastedgaussian')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def barbwire(input, output):
    """Transforms the received image into a mask with a barbwire outline texture."""
    apply_filter(input, output, 'dog 47,118,119,111,108,1 whirls 71,16,2,63,76,74,57,113,104 luminance', 'mask_barbwire')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def waterylines(input, output):
    """Transforms the received image into a mask with a watery lines texture."""
    apply_filter(input, output, 'dog 53,46,53,66,147,48 whirls 89,62,8,92,58,78,85,19,13 luminance', 'mask_waterylines')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def contourandwaves(input, output):
    """Transforms the received image into a mask with contour and waves texture."""
    apply_filter(input, output, 'dog 55,58,47,147,79,90 whirls 5,12,0,47,93,103,137,57,63 luminance', 'mask_contourandwaves')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkoutline(input, output):
    """Transforms the received image into a mask with a dark image and black outline."""
    apply_filter(input, output, 'dog 56,18,63 luminance', 'mask_darkoutline')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def gaussianoutline(input, output):
    """Transforms the received image into a mask with a dark image and black outline."""
    apply_filter(input, output, 'dog 117,2,49 luminance', 'mask_gaussianoutline')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darksilhouette(input, output):
    """Transforms the received image into a mask with a dark image with silhouette and black outline."""
    apply_filter(input, output, 'dog 64,22,32 luminance', 'mask_darksilhouette')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def gaussiansilhouette(input, output):
    """Transforms the received image into a mask with a dark image with gaussian silhouettes and black outline."""
    apply_filter(input, output, 'dog 108,4,44 luminance', 'mask_gaussiansilhouette')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkshapes(input, output):
    """Transforms the received image into a mask with a dark image with shapes and black outline."""
    apply_filter(input, output, 'dog 95,16,73 luminance', 'mask_darkshapes')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def gaussianshapes(input, output):
    """Transforms the received image into a mask with a dark image with shapes and black outline."""
    apply_filter(input, output, 'dog 97,10,86 luminance', 'mask_gaussianshapes')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def sketchedoutline(input, output):
    """Transforms the received image into a mask with sketched outline texture."""
    apply_filter(input, output, 'dog 108,4,44,105,56,69 whirls 52,134,80,57,74,38,54,67,45 luminance', 'mask_sketchedoutline')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def densespiderweb(input, output):
    """Transforms the received image into a mask with dense spider web texture."""
    apply_filter(input, output, 'cracks 27,146,5,71,67 fx_pen_drawing 65,59,89 luminance', 'mask_densespiderweb')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def eyeline(input, output):
    """Transforms the received image into a mask with a dark image with eyeline outline texture."""
    apply_filter(input, output, 'dog 3,89,50 luminance', 'mask_eyeline')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def paperandcharcoal(input, output):
    """Transforms the received image into a mask with paper and charcoal texture."""
    apply_filter(input, output, 'dog 9,103,145,12,132,33 whirls 125,71,1,2,42,3,131,18,85 luminance', 'mask_paperandcharcoal')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def carvedtrunk(input, output):
    """Transforms the received image into a mask with carved trunk texture."""
    apply_filter(input, output, 'stencil 2,141,31,59,23 drawing , luminance', 'mask_carvedtrunk')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def sparkles(input, output):
    """Transforms the received image into a mask with sparkles texture."""
    apply_filter(input, output, 'unsharp 6,52,33 blur 2 luminance', 'mask_sparkles')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def burned(input, output):
    """Transforms the received image into a mask with burned texture."""
    apply_filter(input, output, 'unsharp 36,17,9 luminance', 'mask_burned')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def excesslight(input, output):
    """Transforms the received image into a mask with excess light texture."""
    apply_filter(input, output, 'unsharp 73,55,91 luminance', 'mask_excesslight')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def oldfanzine(input, output):
    """Transforms the received image into a mask with old fanzine texture."""
    apply_filter(input, output, 'unsharp 126,107,4 luminance', 'mask_oldfanzine')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def glitchwave(input, output):
    """Transforms the received image into a mask with glitch wave texture."""
    apply_filter(input, output, 'wave 14,1,33,81,20 luminance', 'mask_glitchwave')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def overflow(input, output):
    """Transforms the received image into a mask with overflow outline texture."""
    apply_filter(input, output, 'fx_sponge 37,24,3 fx_unsharp_richardsonlucy 20,2,14,3,46 luminance', 'mask_overflow')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def stainededges(input, output):
    """Transforms the received image into a mask with stained edges texture."""
    apply_filter(input, output, 'fx_sponge 41,20,5 fx_unsharp_richardsonlucy 6,43,43,20,12 luminance', 'mask_stainededges')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def contrastededges(input, output):
    """Transforms the received image into a mask with contrasted edges texture."""
    apply_filter(input, output, 'fx_sponge 5,21,22 fx_unsharp_richardsonlucy 10,28,22,37,50 luminance', 'mask_contrastededges')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def raccoon(input, output):
    """Transforms the received image into a mask with a raccoon texture."""
    apply_filter(input, output, 'fx_vector_painting 9 luminance', 'mask_raccoon')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def drawnraccoon(input, output):
    """Transforms the received image into a mask with a drawn raccoon texture."""
    apply_filter(input, output, 'fx_vector_painting 9 drawing , luminance', 'mask_drawnraccoon')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkendetails(input, output):
    """Transforms the received image into a mask with a darken details texture."""
    apply_filter(input, output, 'fx_deblur 20,70,144,75,150,25,126,69,2 luminance', 'mask_darkendetails')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def spectruminblack(input, output):
    """Transforms the received image into a mask with a spectrum in black texture."""
    apply_filter(input, output, 'fx_deblur 76,131,67,8,2,13,130,70,144,137,99 luminance', 'mask_spectruminblack')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def flattened(input, output):
    """Transforms the received image into a mask with a flattened texture."""
    apply_filter(input, output, 'fx_deblur 148,101,63,9,121,25,57,40,88 luminance', 'mask_flattened')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def waxedoutline(input, output):
    """Transforms the received image into a mask with a waxed outline texture."""
    apply_filter(input, output, 'fx_deblur 16,69,128,95,123,29,109,88,1 drawing , luminance', 'mask_waxedoutline')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def waxedcontrast(input, output):
    """Transforms the received image into a mask with a waxed contrast texture."""
    apply_filter(input, output, 'fx_deblur 20,70,144,75,150,25,126,69,2 drawing , luminance', 'mask_waxedcontrast')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def waxeddetails(input, output):
    """Transforms the received image into a mask with a waxed details texture."""
    apply_filter(input, output, 'fx_deblur 83,119,1,41,45,4,84,32,28 drawing , luminance', 'mask_waxeddetails')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def hazywax(input, output):
    """Transforms the received image into a mask with a hazy wax texture."""
    apply_filter(input, output, 'fx_deblur 129,105,79,6,82,17,7,69,80 drawing , luminance', 'mask_hazywax')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def cleardetails(input, output):
    """Transforms the received image into a mask with a clear details texture."""
    apply_filter(input, output, 'fx_deblur 148,101,63,9,121,28,57,40,88 drawing , luminance', 'mask_cleardetails')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def graylava(input, output):
    """Transforms the received image into a mask with a gray lava texture."""
    apply_filter(input, output, 'fx_lava 9,30,145,30,55,96,29,102,4 drawing , luminance', 'mask_graylava')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def graybrushstrokes(input, output):
    """Transforms the received image into a mask with a gray brush strokes texture."""
    apply_filter(input, output, 'fx_lava 9,30,145,30,55,96,29,102,4 luminance', 'mask_graybrushstrokes')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def leopard(input, output):
    """Transforms the received image into a mask with a leopard spots texture."""
    apply_filter(input, output, 'fx_lava 11,100,54,54,130,6,19,31,35 drawing , luminance', 'mask_leopard')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def scraper(input, output):
    """Transforms the received image into a mask with a scraped wall texture."""
    apply_filter(input, output, 'fx_lava 11,100,54,54,130,6,19,31,35 luminance', 'mask_scraper')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def inkbrushstrokes(input, output):
    """Transforms the received image into a mask with a ink brush strokes texture."""
    apply_filter(input, output, 'fx_painting 18,6,24 drawing , luminance', 'mask_inkbrushstrokes')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def childish(input, output):
    """Transforms the received image into a mask with a childish texture."""
    apply_filter(input, output, 'fx_painting 53,5,61 drawing , luminance', 'mask_childish')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def tracer(input, output):
    """Transforms the received image into a mask with a tracer texture."""
    apply_filter(input, output, 'fx_painting 78,0,36 drawing , luminance', 'mask_tracer')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def alice(input, output):
    """Transforms the received image into a mask with a Alice in wonderland texture."""
    apply_filter(input, output, 'fx_painting 95,19,124,61,112,78 fx_lava 11,103,95,104,73,101,137,91,83 drawing , luminance', 'mask_alice')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def indelible(input, output):
    """Transforms the received image into a mask with a indelible marker texture."""
    apply_filter(input, output, 'fx_painting 104,1,15 drawing , luminance', 'mask_indelible')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def catrina(input, output):
    """Transforms the received image into a mask with a catrina skull texture."""
    apply_filter(input, output, 'fx_painting 126,3,21 drawing , luminance', 'mask_catrina')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def skull(input, output):
    """Transforms the received image into a mask with a skull texture."""
    apply_filter(input, output, 'fx_painting 130,2,88 drawing , luminance', 'mask_skull')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def enhancemedia(input, output):
    """Transforms the received image into a mask with a enhance the media texture."""
    apply_filter(input, output, 'fx_whirls 9,94,67,83,36,55,76,132,55,35 luminance', 'mask_enhancemedia')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def gothic(input, output):
    """Transforms the received image into a mask with a gothic texture."""
    apply_filter(input, output, 'fx_whirls 13,90,4,4,20,12,144,76,71,51 luminance', 'mask_gothic')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def offoutline(input, output):
    """Transforms the received image into a mask with contours and muted colors texture."""
    apply_filter(input, output, 'fx_whirls 16,15,106,23,12,96,132,123,96,76 luminance', 'mask_offoutline')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def graypencil(input, output):
    """Transforms the received image into a mask with a gray pencil texture."""
    apply_filter(input, output, 'fx_whirls 93,55,60,104,9,28,16,4,107,51 luminance', 'mask_graypencil')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def wornmarker(input, output):
    """Transforms the received image into a mask with a worn marker texture."""
    apply_filter(input, output, 'fx_whirls 83,15,150,43,25,119,106,105,124,106 luminance', 'mask_wornmarker')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def strongcontrast(input, output):
    """Transforms the received image into a mask with a strong contrast texture."""
    apply_filter(input, output, 'fx_whirls 81,80,69,141,8,2,96,83,120,124 luminance', 'mask_strongcontrast')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def onlymidtones(input, output):
    """Transforms the received image into a mask with a texture with only midtones."""
    apply_filter(input, output, 'fx_whirls 51,79,101,28,36,49,85,31,87,118 luminance', 'mask_onlymidtones')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def loosesketch(input, output):
    """Transforms the received image into a mask with a loose sketch texture."""
    apply_filter(input, output, 'fx_whirls 35,99,110,143,26,148,12,46,17,13 luminance', 'mask_loosesketch')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def geometricsketch(input, output):
    """Transforms the received image into a mask with a geometric sketch texture."""
    apply_filter(input, output, 'fx_whirls 13,90,4,4,20,12,144,76,71,51 luminance', 'mask_geometricsketch')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def gothan(input, output):
    """Transforms the received image into a mask with a Gothan texture."""
    apply_filter(input, output, 'fx_painting 150,1,109 drawing , luminance', 'mask_gothan')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def multilineripple(input, output):
    """Transforms the received image into a mask with a multiline ripple texture."""
    apply_filter(input, output, 'pencilbw 41,12,50 fx_freaky_details 133,22,105,5,73,127,22,64,75 drawing , luminance', 'mask_multilineripple')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def predator(input, output):
    """Transforms the received image into a mask with a predator hair texture."""
    apply_filter(input, output, 'pencilbw 45,4,7 fx_freaky_details 10,13,91,25,83,145,142,37,95 drawing , luminance', 'mask_predator')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def cave(input, output):
    """Transforms the received image into a mask with a cave picture texture."""
    apply_filter(input, output, 'pencilbw 48,133,75,129 unsharp 21,31 drawing , luminance', 'mask_cave')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def bullfighting(input, output):
    """Transforms the received image into a mask with a bullfighting poster texture."""
    apply_filter(input, output, 'normalize_local 35,3 drawing , luminance', 'mask_bullfighting')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def batman(input, output):
    """Transforms the received image into a mask with a Batman comic texture."""
    apply_filter(input, output, 'normalize_local 39,26 drawing , luminance', 'mask_batman')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def cape(input, output):
    """Transforms the received image into a mask with a Batman comic texture."""
    apply_filter(input, output, 'normalize_local 43,12 drawing , luminance', 'mask_cape')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def brokenwax(input, output):
    """Transforms the received image into a mask with a broken wax texture."""
    apply_filter(input, output, 'normalize_local 45,4 drawing , luminance', 'mask_brokenwax')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def chiaroscuro(input, output):
    """Transforms the received image into a mask with a chiaroscuro texture."""
    apply_filter(input, output, 'normalize_local 92,11 drawing , luminance', 'mask_chiaroscuro')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def barbecue(input, output):
    """Transforms the received image into a mask with a barbecue texture."""
    apply_filter(input, output, 'pencilbw 2,118,121,79 unsharp 80,76 drawing , luminance', 'mask_barbecue')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def watercolor(input, output):
    """Transforms the received image into a mask with a watercolor texture."""
    apply_filter(input, output, 'pencilbw 10,13,91,25 unsharp 45,4 drawing , luminance', 'mask_watercolor')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def rorschach(input, output):
    """Transforms the received image into a mask with a Rorschach test texture."""
    apply_filter(input, output, 'pencilbw 10,111,73,137 unsharp 22,94 drawing , luminance', 'mask_rorschach')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def aura(input, output):
    """Transforms the received image into a mask with a aura texture."""
    apply_filter(input, output, 'pencilbw 15,65 drawing , luminance', 'mask_aura')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def grates(input, output):
    """Transforms the received image into a mask with a grates texture."""
    apply_filter(input, output, 'pencilbw 17,99 drawing , luminance', 'mask_grates')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def maritime(input, output):
    """Transforms the received image into a mask with a maritime texture."""
    apply_filter(input, output, 'pencilbw 21,93,93 fx_freaky_details 39,20,139,8,128,133,141,133,111 drawing , luminance', 'mask_maritime')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def diffuseshapes(input, output):
    """Transforms the received image into a mask with a diffuse shapes texture."""
    apply_filter(input, output, 'pencilbw 24,87,33,65 unsharp 69,10 drawing , luminance', 'mask_diffuseshapes')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def outlineongray(input, output):
    """Transforms the received image into a mask with a outline on gray texture."""
    apply_filter(input, output, 'pencilbw 31,5,48 dog 150,0,13,66,59,84 drawing , luminance', 'mask_outlineongray')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def embossedtiles(input, output):
    """Transforms the received image into a mask with a embossed tiles texture."""
    apply_filter(input, output, 'pencilbw 31,145,45 fx_freaky_details 57,122,64,13,15,92,49,1,101 drawing , luminance', 'mask_embossedtiles')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def stainedtiles(input, output):
    """Transforms the received image into a mask with a stained tiles texture."""
    apply_filter(input, output, 'pencilbw 36,41,70 fx_freaky_details 19,25,52,34,91,10,146,30,87 drawing , luminance', 'mask_stainedtiles')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def oldphoto(input, output):
    """Transforms the received image into a mask with a old photo texture."""
    apply_filter(input, output, 'pencilbw 49,79,100 fx_freaky_details 108,70,22,14,114,50,47,110 drawing , luminance', 'mask_oldphoto')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def glasstiles(input, output):
    """Transforms the received image into a mask with a glass tiles texture."""
    apply_filter(input, output, 'pencilbw 59,7,135 fx_freaky_details 106,10,32,14,89,36,30,116,145 drawing , luminance', 'mask_glasstiles')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def drips(input, output):
    """Transforms the received image into a mask with a drips texture."""
    apply_filter(input, output, 'pencilbw 64,72,115 unsharp 9,52 drawing , luminance', 'mask_drips')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def beech(input, output):
    """Transforms the received image into a mask with a beech wood texture."""
    apply_filter(input, output, 'pencilbw 85,36,150,52 unsharp 47,3 drawing , luminance', 'mask_beech')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def cherry(input, output):
    """Transforms the received image into a mask with a cherry wood texture."""
    apply_filter(input, output, 'pencilbw 87,42 drawing , luminance', 'mask_cherry')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def woodknot(input, output):
    """Transforms the received image into a mask with a wood knot texture."""
    apply_filter(input, output, 'pencilbw 92,11 drawing , luminance', 'mask_woodknot')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def radiance(input, output):
    """Transforms the received image into a mask with a radiance texture."""
    apply_filter(input, output, 'pencilbw 97,13,3,15 unsharp 17,99 drawing , luminance', 'mask_radiance')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def zebra(input, output):
    """Transforms the received image into a mask with a zebra texture."""
    apply_filter(input, output, 'pencilbw 116,73,55,27 unsharp 15,121 drawing , luminance', 'mask_zebra')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def scrapedwood(input, output):
    """Transforms the received image into a mask with a scraped wood texture."""
    apply_filter(input, output, 'pencilbw 130,5 drawing , luminance', 'mask_scrapedwood')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def stripped(input, output):
    """Transforms the received image into a mask with a stripped wood texture."""
    apply_filter(input, output, 'pencilbw 144,106,61,66 unsharp 28,76 drawing , luminance', 'mask_stripped')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def candles(input, output):
    """Transforms the received image into a mask with a candles texture."""
    apply_filter(input, output, 'pixelize 15,65,18,92,94,74,77,98 fire_edges 11 luminance', 'mask_candles')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def flaming(input, output):
    """Transforms the received image into a mask with a flaming texture."""
    apply_filter(input, output, 'pixelize 142,33,122,99,29,127,116,72 fire_edges 1 luminance', 'mask_flaming')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def phantasmagoric(input, output):
    """Transforms the received image into a mask with a phantasmagoric texture."""
    apply_filter(input, output, 'stencilbw 15,150 pencilbw 10,103,83 luminance', 'mask_phantasmagoric')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def messyhair(input, output):
    """Transforms the received image into a mask with a messy hair texture."""
    apply_filter(input, output, 'stencilbw 19,124 fx_pencil_portraitbw 65,71,17,28,4,1,73 drawing , luminance', 'mask_messyhair')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def impressed(input, output):
    """Transforms the received image into a mask with a impressed in wood texture."""
    apply_filter(input, output, 'stencilbw 26,135 pencilbw 3,128,102 luminance', 'mask_impressed')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def diagonalshading(input, output):
    """Transforms the received image into a mask with a diagonal shading texture."""
    apply_filter(input, output, 'stencilbw 37,8 fx_pencil_portraitbw 61,52,0,68,1,2,43 drawing , luminance', 'mask_diagonalshading')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def diagonalzebra(input, output):
    """Transforms the received image into a mask with a diagonal zebra texture."""
    apply_filter(input, output, 'stencilbw 44,87 fx_pencil_portraitbw 130,12,7,140,10,101,93 drawing , luminance', 'mask_diagonalzebra')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def lightcontour(input, output):
    """Transforms the received image into a mask with a light contour texture."""
    apply_filter(input, output, 'stencilbw 52,53 pencilbw 18,143,76 luminance blur 3', 'mask_lightcontour')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def shadeddoodle(input, output):
    """Transforms the received image into a mask with a shaded doodle texture."""
    apply_filter(input, output, 'stencilbw 76,0 fx_pencil_portraitbw 126,60,0,119,56,59,74 drawing , luminance', 'mask_shadeddoodle')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def doodle(input, output):
    """Transforms the received image into a mask with a doodle texture."""
    apply_filter(input, output, 'stencilbw 88,4 fx_pencil_portraitbw 48,129,12,110,41,24,133 drawing , pencilbw 0,1', 'mask_doodle')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def around(input, output):
    """Transforms the received image into a mask with a clear around the contour texture."""
    apply_filter(input, output, 'pencilbw 17,36,113 dog 26,8,113,36,68,18 luminance', 'mask_around')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def contouronclear(input, output):
    """Transforms the received image into a mask with a contour on clear texture."""
    apply_filter(input, output, 'pencilbw 18,71,85 dog 12,150,101,23,68,110 luminance', 'mask_contouronclear')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def glaze(input, output):
    """Transforms the received image into a mask with a glaze texture."""
    apply_filter(input, output, 'pencilbw 68,47,108 fx_freaky_details 73,29,136,18,79,144,0,95 drawing , luminance', 'mask_glaze')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def darkcomic(input, output):
    """Transforms the received image into a mask with a dark comic texture."""
    apply_filter(input, output, 'stencilbw 15,51 pencilbw 2,105,52 luminance', 'mask_darkcomic')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def stainedwall(input, output):
    """Transforms the received image into a mask with a stained wall texture."""
    apply_filter(input, output, 'stencilbw 16,100 pencilbw 21,64,141 luminance', 'mask_stainedwall')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def dirtyeraser(input, output):
    """Transforms the received image into a mask with a dirty eraser texture."""
    apply_filter(input, output, 'stencilbw 58,3 pencilbw 13,14,0 luminance', 'mask_dirtyeraser')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def skeleton(input, output):
    """Transforms the received image into a mask with a skeleton texture."""
    apply_filter(input, output, 'fx_unsharp_richardsonlucy 17,72,80,51,84 pencilbw 5,74,53,9,76,113,141,133,76 drawing , luminance', 'mask_skeleton')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def trooper(input, output):
    """Transforms the received image into a mask with a trooper texture."""
    apply_filter(input, output, 'fx_unsharp_richardsonlucy 25,86,34,118,17 pencilbw 5,97,99,80,24,116,132,23,47 drawing , luminance', 'mask_trooper')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def oilpainting(input, output):
    """Transforms the received image into a mask with a oil painting texture."""
    apply_filter(input, output, 'fx_unsharp_richardsonlucy 77,11,52,83,131 pencilbw 6,18,103,102,1,21,0,95,54 drawing , luminance', 'mask_oilpainting')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def turpentine(input, output):
    """Transforms the received image into a mask with a oil painting with turpentine texture."""
    apply_filter(input, output, 'fx_unsharp_richardsonlucy 82,23,78,149,148 pencilbw 0,64,116,110,85,74,87,6,77 drawing , luminance', 'mask_turpentine')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def jocker(input, output):
    """Transforms the received image into a mask with a Jocker comic texture."""
    apply_filter(input, output, 'fx_unsharp_richardsonlucy 144,55,85,76,108 pencilbw 3,68,82,18,110,37,75,18,127 drawing , luminance', 'mask_jocker')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def crossstitch(input, output):
    """Transforms the received image into a mask with a cross-stitch texture."""
    apply_filter(input, output, 'hardsketchbw 10,82,90 luminance', 'mask_crossstitch')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def coffeestains(input, output):
    """Transforms the received image into a mask with a coffee stains texture."""
    apply_filter(input, output, 'hardsketchbw 11,14,66 pencilbw 24,101,31 luminance', 'mask_coffeestains')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def embroidery(input, output):
    """Transforms the received image into a mask with a embroidery texture."""
    apply_filter(input, output, 'hardsketchbw 11,14,66,5,72,55 luminance', 'mask_embroidery')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def topstitching(input, output):
    """Transforms the received image into a mask with a topstitching texture."""
    apply_filter(input, output, 'hardsketchbw 13,36,49 luminance', 'mask_topstitching')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def sewing(input, output):
    """Transforms the received image into a mask with a sewing texture."""
    apply_filter(input, output, 'hardsketchbw 19,96,4 luminance', 'mask_sewing')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def diffusetea(input, output):
    """Transforms the received image into a mask with a diffuse tea stains texture."""
    apply_filter(input, output, 'hardsketchbw 31,84,124 pencilbw 28,23,17 luminance blur 15', 'mask_diffusetea')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def crazydoodles(input, output):
    """Transforms the received image into a mask with a crazy doodles texture."""
    apply_filter(input, output, 'hardsketchbw 38,36,23,2,78,60 drawing , luminance', 'mask_crazydoodles')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def nightmare(input, output):
    """Transforms the received image into a mask with a nightmare texture."""
    apply_filter(input, output, 'hardsketchbw 58,3,13,14,0,72 pencilbw 32,141,77 luminance', 'mask_nightmare')

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def oldgame(input, output):
    """Transforms the received image into a mask with a old game texture."""
    apply_filter(input, output, 'hardsketchbw 85,53,20,12,115,92 drawing , luminance', 'mask_oldgame')

if __name__ == '__main__':
    colorama.init()  # Initialize colorama
    cli()
