#!/usr/bin/env python3
from os import path

import click

import video_commands_lib as vlc

@click.command()
@click.argument('image_src')
@click.argument('image_dst', default='')
def vectorize(image_src, image_dst):
    """Remove background from image"""
    if not image_src:
        click.echo('You need to indicate an image to vectorize.')
    else:
        try:
            source = Path(image_src)
            if source.is_file():
                output = vlc.tint_image(image_src, image_dst, normalized_color, mode)
                output_path = Path(image_src).parent / output
                if output_path.is_file():
                    click.echo(f"The file { output_path } has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }.")
                else:
                    click.echo(f"Error: {colorama.Fore.RED}Something went wrong{colorama.Style.RESET_ALL} when creating the file {output_path}.")
                    click.echo(f"Please check that { image_src } is an image file.")
            else:
                click.echo(f"Error: {colorama.Fore.RED}The file {image_src} does not exist. Check the path.{colorama.Style.RESET_ALL}")

        except ImportError:
            click.echo('The "PILLOW" or "potrace" module is not installed. Please install it first: ')
            click.echo('\tpip install pillow')
            click.echo('\tpip install potrace')

if __name__ == '__main__':
    vectorize()
