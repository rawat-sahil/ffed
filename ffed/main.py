import click

from ffed import EncoderEnum, add_dynamic_docstring, mutually_exclusive_options


def encode_decode_help_section():
    help_section = f"available algo: {', '.join([algo.name for algo in EncoderEnum])}\n"

    return help_section


def hash_help_section():
    return "something soemthing"


verbose_option = click.option(
    "-v", "--verbose", default=0, count=True, help="for verbosity"
)
stdin_option = click.option(
    "-in", "--stdin", default=False, is_flag=True, help="take input from stdin"
)
file_option = click.option("--file", type=str, help="take input from file")


@click.group()
def cli():
    pass


@cli.command()
@verbose_option
@stdin_option
@file_option
@click.option(
    "--algo", "algo", multiple=True, help="eg. --algo base64 or --algo base64,url"
)
@click.argument("string", required=False)
@add_dynamic_docstring(encode_decode_help_section)
@mutually_exclusive_options("stdin", "file", "string")
def encode(verbose, algo, **input_options):
    print("encode thing")
    print(verbose)


@cli.command()
@verbose_option
@stdin_option
@file_option
@click.option(
    "--algo", "algo", multiple=True, help="eg. --algo base64 or --algo base64,url"
)
@click.argument("string", required=False)
@add_dynamic_docstring(encode_decode_help_section)
@mutually_exclusive_options("stdin", "file", "string")
def decode():
    print("decode thing")


@cli.command()
@verbose_option
@stdin_option
@file_option
@click.argument("string", required=False)
@add_dynamic_docstring(hash_help_section)
@mutually_exclusive_options("stdin", "file", "string")
def hash():
    pass
