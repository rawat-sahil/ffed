import pytest
from click.testing import CliRunner

from ffed import __version__
from ffed.custom_exceptions import MutuallyExclusiveOptionsException
from ffed.main import decode, encode, hash


def test_version():
    assert __version__ == "0.1.0"


@pytest.fixture
def cli_runner():
    return CliRunner()


def test_no_input_provided(cli_runner):
    subcommands = [encode, decode, hash]

    for subcommand in subcommands:
        with pytest.raises(MutuallyExclusiveOptionsException):
            result = cli_runner.invoke(subcommand, ["--algo", "base64"])

            if result.exception:
                raise result.exception


def test_encode_decode(cli_runner):
    """
    Keep in mind when comparing the result with the output of command line tools don't for chaining of algo don't forget
    to remove \n from intermediate outputs
    """
    base_parameter = ["--algo", "base64,base64"]

    # test input from arguments
    plain_text = "Hello World"
    encoded_text = "U0dWc2JHOGdWMjl5YkdRPQ=="
    result = cli_runner.invoke(encode, base_parameter + [plain_text])
    assert result.exit_code == 0
    assert result.output == "U0dWc2JHOGdWMjl5YkdRPQ==\n"
    result = cli_runner.invoke(decode, base_parameter + [encoded_text])
    assert result.exit_code == 0
    assert result.output == plain_text + "\n"

    # test input from file
    result = cli_runner.invoke(encode, base_parameter + ["--file", "tests/plain_text"])
    assert result.exit_code == 0
    assert (
        result.output
        == "Wm1seWMzUWdiR2x1WlFwelpXTnZibVFnYkdsdVpRcDBhR2x5WkNCc2FXNWxDZz09\n"
    )
    result = cli_runner.invoke(
        decode, base_parameter + ["--file", "tests/encoded_text"]
    )
    assert result.exit_code == 0
    assert result.output == "first line\nsecond line\nthird line\n"


def test_hash(cli_runner):
    plain_text = "Hello World"
    base_parameter = ["--algo", "md5,md5"]

    # test input from argument
    result = cli_runner.invoke(hash, base_parameter + [plain_text])
    assert result.exit_code == 0
    assert result.output == "3935a6184c654e7a05a4e42c1fb17def\n"

    # test input from file
    result = cli_runner.invoke(hash, base_parameter + ["--file", "tests/plain_text"])
    assert result.exit_code == 0
    assert result.output == "8ea0cb0822ee3991f630e45c321a6fa2\n"
    pass
