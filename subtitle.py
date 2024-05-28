#!/usr/bin/env python3

from pathlib import Path

import click
import colorama
from moviepy.editor import VideoFileClip


@click.group()
def cli():
    pass

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def toaudio(input, output):
    """Extract audio from a video."""

    if not output:
        output = f"{Path(input).stem}.wav"

    video = VideoFileClip(input)
    video.audio.write_audiofile(output)

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The image has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


if __name__ == "__main__":
    cli()
