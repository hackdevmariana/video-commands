#!/usr/bin/env python3

import os
from pathlib import Path
import sys


import click
import colorama
from moviepy.editor import VideoFileClip

def get_video_codec(video_file):
    try:
        clip = VideoFileClip(video_file)
        video_codec = clip.write_videofile(codec='copy').videofile.codec_name
        return video_codec
    except Exception as e:
        print(f"Error: {e}")
        return None


def crop_vertical(video_file, output_file):
    try:
        clip = VideoFileClip(video_file)
        cropped_clip = clip.crop(x1=656, y1=0, x2=656+609, y2=1080)

        video_codec = get_video_codec(video_file)
        if video_codec:
            cropped_clip.write_videofile(output_file, codec=video_codec)
        else:
            cropped_clip.write_videofile(output_file, codec='libx264')
        return output_file
    except Exception as e:
        print(f"Error: {e}")

@click.command()
@click.argument('input')
@click.argument('output', default='')
def cutshort(input, output):
    """Vertically crop a video to make a YouTube short"""

    if not output:
        output = f"{Path(input).stem}_vertical.mp4"
    crop_vertical(input, output)

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The video has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")


if __name__ == "__main__":
    cutshort()
