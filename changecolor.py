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
def orange():
    """Changes the color of the received image to pastel orange."""

@click.group()
def cli():
    pass

cli.add_command(orange)
cli.add_command(pastelorange)

if __name__ == "__main__":
    cli()