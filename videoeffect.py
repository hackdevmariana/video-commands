#!/usr/bin/env python3

from pathlib import Path

import click
import colorama
import cv2
import numpy as np
import os
from PIL import Image, ImageFilter

from moviepy.editor import *
from video_commands_lib import random_filename

def extract_audio(video_file, output_duration):
    audio_file = random_filename(suffix='.mp3')
    video_clip = VideoFileClip(video_file)
    audio_clip = video_clip.audio

    # Recortar el audio para que tenga la misma duración que el vídeo
    audio_clip = audio_clip.subclip(0.01, output_duration)
    audio_clip.write_audiofile(audio_file)

    video_clip.close()
    return audio_file


def get_duration(video_path):
    video_clip = VideoFileClip(video_path)
    duration = video_clip.duration
    video_clip.close()
    return duration

def combine_video_with_audio(video_file, audio_file, output_file):

    videoclip = VideoFileClip(video_file)
    audioclip = AudioFileClip(audio_file)

    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(output_file)


def get_fps(video_path):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    return fps

def overlay_videos(original_video, modified_video, output_file):
    print("En overlay_videos")
    print(original_video, modified_video, output_file)
    original_clip = VideoFileClip(original_video)
    modified_clip = VideoFileClip(modified_video)

    # Superponer el vídeo modificado al vídeo original
    final_clip = concatenate_videoclips([original_clip, modified_clip.set_duration(original_clip.duration)])

    # Guardar el resultado en un nuevo archivo
    final_clip.write_videofile(output_file)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
@click.option('--color', type=int, default=2, help='Blur intensity')
def uniformbackground(input, output, color):
    """Applies blur effect to the received video."""

    if not output:
        output = f"{Path(input).stem}_uniformbackground.mp4"

    output_duration = get_duration(input)
    audio = extract_audio(input, output_duration)
    video = random_filename(suffix='.mp4')

    reader = imageio.get_reader(input)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(video, fps=fps)

    for frame in reader:
        # Convertir el fotograma a formato de imagen PIL
        pil_frame = Image.fromarray(frame)
        modified_frame = pil_frame.filter(ImageFilter.CONTOUR)
        modified_frame_np = np.array(blurred_frame)
        writer.append_data(blurred_frame_np)

    writer.close()

    # overlay_videos(input, output, output)
    combine_video_with_audio(video_file=video, audio_file=audio, output_file=output)

    # os.remove(audio)

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The video has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='', help='Output file path')
def contour(input, output):
    """Applies contour effect to the received video."""

    if not output:
        output = f"{Path(input).stem}_blurred.mp4"

    output_duration = get_duration(input)
    audio = extract_audio(input, output_duration)
    video = random_filename(suffix='.mp4')

    reader = imageio.get_reader(input)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(video, fps=fps)

    for frame in reader:
        # Convertir el fotograma a formato de imagen PIL
        pil_frame = Image.fromarray(frame)

        # Aplicar el efecto de desenfoque con Pillow
        blurred_frame = pil_frame.filter(ImageFilter.CONTOUR)

        # Convertir el fotograma desenfocado de vuelta a formato numpy
        blurred_frame_np = np.array(blurred_frame)

        # Escribir el fotograma desenfocado en el video de salida
        writer.append_data(blurred_frame_np)

    writer.close()

    # overlay_videos(input, output, output)
    combine_video_with_audio(video_file=video, audio_file=audio, output_file=output)

    # os.remove(audio)

    output_path = Path(output)
    if output_path.is_file():
        click.echo(f"The video has been created{ colorama.Fore.GREEN } successfully{ colorama.Style.RESET_ALL }: {output}")
    else:
        click.echo(f"An{ colorama.Fore.RED } error{ colorama.Style.RESET_ALL } occurred creating the file {output}.")

if __name__ == '__main__':
    cli()
