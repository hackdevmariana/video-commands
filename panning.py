#!/usr/bin/env python3

import click
from PIL import Image
import imageio
import numpy as np

@click.command()
@click.argument('input_image', type=click.Path(exists=True))
@click.argument('output_video', type=click.Path())
@click.option('--duration', default=5, help='Duration of the video in seconds')
@click.option('--fps', default=30, help='Frames per second')
@click.option('--direction', type=click.Choice(['left', 'right', 'up', 'down']), default='right', help='Direction of the pan')
def create_panning_video(input_image, output_video, duration, fps, direction):
    """Creates a panning video from a single image."""
    # Load the image
    image = Image.open(input_image)
    image_width, image_height = image.size

    # Calculate the number of frames
    total_frames = duration * fps

    # Create a list to store the frames
    frames = []

    for frame_number in range(total_frames):
        # Calculate the offset based on the frame number and direction
        if direction in ['left', 'right']:
            max_offset = image_width - image_width // 2
            offset = int(max_offset * frame_number / total_frames)
            if direction == 'left':
                offset = -offset
            frame = image.crop((offset, 0, image_width + offset, image_height))
        elif direction in ['up', 'down']:
            max_offset = image_height - image_height // 2
            offset = int(max_offset * frame_number / total_frames)
            if direction == 'up':
                offset = -offset
            frame = image.crop((0, offset, image_width, image_height + offset))

        # Convert the frame to a numpy array and add it to the list
        frames.append(np.array(frame))

    # Save the frames as a video
    imageio.mimsave(output_video, frames, fps=fps)

    click.echo(f'Video saved to {output_video}')

if __name__ == '__main__':
    create_panning_video()
