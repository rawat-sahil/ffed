# ffed (full-fledged encoder decoder)

## Installation

```shell
pip install ffed
```

## Usage

Subcommands available `encode`, `decode`, `hash`

```shell
# To get the help section
ffed --help

# To get the help section of specific sub command and list all the available algorithms
ffed encode --help

# Example encode
## taking input from command line argument
ffed encode --algo base64 {string to be encoded}

## taking input from a file
ffed encode --algo base64 --file {path to file}

## taking input from stdin
echo "foo bar" | ffed encode --algo base64

## encoding multiple times (comma separated multiple algorithms)
ffed encode --algo base64,url {string to be encoded}

## output to a file
ffed encode --algo base64  --out {path to the file}
```
