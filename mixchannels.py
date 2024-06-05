#!/usr/bin/env python3

from pathlib import Path

import click
import colorama
import gmic



def process_image(command_name, instruction):
    def decorator(func):
        @click.command(name=command_name)
        @click.argument('input', type=click.Path(exists=True))
        @click.option('--output', '-o', default='', help='Output file path')
        def wrapper(input, output):
            if not output:
                output = f"{Path(input).stem}_{command_name}.png"

            gmic.run(f'{input} mix_channels ({instruction}) output {output}')

            output_path = Path(output)
            if output_path.is_file():
                click.echo(f"The image has been created{colorama.Fore.GREEN} successfully{colorama.Style.RESET_ALL}: {output}")
            else:
                click.echo(f"An{colorama.Fore.RED} error{colorama.Style.RESET_ALL} occurred creating the file {output}.")

        return wrapper
    return decorator

@process_image('darkblue', "0,0,0;0,0,0;0,1,0")
def darkblue():
    """Mixes the channels giving a dark blue tone to the image."""

@process_image('green', "0,0,0;0,1,0;0,0,0")
def green():
    """Mixes the channels giving a green tone to the image."""

@process_image('turquoise', "0,0,0;0,0,1;0,0,1")
def turquoise():
    """Mixes the channels giving a turquoise tone to the image."""

@process_image('sea', "0,0,0;0,0,1;0,1,0")
def sea():
    """Mixes the channels giving a sea tone to the image."""

@process_image('greenishandblue', "0,0,0;0,0,1;1,0,0")
def greenishandblue():
    """Mixes the channels giving a greenish and blue tone to the image."""

@process_image('luminousgreen', "0,0,0;1,0,0;0,0,0")
def luminousgreen():
    """Mixes the channels giving a luminous green tone to the image."""

@process_image('greenteal', "0,0,0;1,0,0;0,0,1")
def greenteal():
    """Mixes the channels giving a green and teal tone to the image."""

@process_image('darkred', "0,0,1;0,0,0;0,0,0")
def darkred():
    """Mixes the channels giving a dark red tone to the image."""

@process_image('purple', "0,0,1;0,0,0;0,0,1")
def purple():
    """Mixes the channels giving a purple tone to the image."""

@process_image('lilacblue', "0,0,1;0,0,0;1,0,0")
def lilacblue():
    """Mixes the channels giving a lilac and blue tone to the image."""

@process_image('paleyellow', "0,0,1;0,0,1;0,0,0")
def paleyellow():
    """Mixes the channels giving a pale yellow tone to the image."""

@process_image('palepurplegrey', "0,0,1;0,0,1;0,1,0")
def palepurplegrey():
    """Mixes the channels giving a pale purple and grey tone to the image."""

@process_image('purplegrey', "0,0,1;0,0,1;1,0,0")
def purplegrey():
    """Mixes the channels giving a purple and grey tone to the image."""


@click.group()
def cli():
    pass


cli.add_command(darkblue)
cli.add_command(green)
cli.add_command(turquoise)
cli.add_command(sea)
cli.add_command(greenishandblue)
cli.add_command(luminousgreen)
cli.add_command(greenteal)
cli.add_command(darkred)
cli.add_command(purple)
cli.add_command(lilacblue)
cli.add_command(paleyellow)
cli.add_command(palepurplegrey)
cli.add_command(purplegrey)



if __name__ == "__main__":
    cli()
