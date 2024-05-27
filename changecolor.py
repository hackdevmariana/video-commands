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

            gmic.run(f'{input} {instruction} output {output}')

            output_path = Path(output)
            if output_path.is_file():
                click.echo(f"The image has been created{colorama.Fore.GREEN} successfully{colorama.Style.RESET_ALL}: {output}")
            else:
                click.echo(f"An{colorama.Fore.RED} error{colorama.Style.RESET_ALL} occurred creating the file {output}.")

        return wrapper
    return decorator

@process_image('orange', "balance_gamma 241,147,-121")
def orange():
    """Changes the color of the received image to orange."""

@process_image('pastelorange', "balance_gamma 250,178,124")
def pastelorange():
    """Changes the color of the received image to pastel orange."""

@process_image('luminousgreen', "balance_gamma -12,96,-237")
def luminousgreen():
    """Changes the color of the received image to luminous green."""

@process_image('pastelturquoise', "balance_gamma -17,165,127")
def pastelturquoise():
    """Changes the color of the received image to pastel turquoise."""

@process_image('indigo', "balance_gamma -19,106,128")
def indigo():
    """Changes the color of the received image to indigo."""

@process_image('pastelblue', "balance_gamma -21,202,231")
def pastelblue():
    """Changes the color of the received image to pastel blue."""

@process_image('blue', "balance_gamma -23,69,215")
def blue():
    """Changes the color of the received image to blue."""

@click.group()
def cli():
    pass

cli.add_command(orange)
cli.add_command(pastelorange)
cli.add_command(luminousgreen)
cli.add_command(pastelturquoise)
cli.add_command(pastelblue)
cli.add_command(blue)
cli.add_command(indigo)

if __name__ == "__main__":
    cli()
