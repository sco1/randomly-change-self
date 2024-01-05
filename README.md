# randomly-change-self
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

Change all instances of `self` to `this` in one randomly chosen scope.

Inspired by [David Beazley's toot](https://mastodon.social/@dabeaz/111703946510399408).

## Installation
Install from PyPi with your favorite `pip` invocation:

```bash
$ python3 -m pip install randomly-change-self
```

You can confirm proper installation via the `randomly-change-self` CLI:
<!-- [[[cog
import cog
from subprocess import PIPE, run
out = run(["randomly-change-self", "--help"], stdout=PIPE, encoding="ascii")
cog.out(
    f"```\n$ randomly-change-self --help\n{out.stdout.rstrip()}\n```"
)
]]] -->
```
$ randomly-change-self --help
usage: randomly-change-self [-h] [--consider-mercury-in-retrograde CONSIDER_MERCURY_IN_RETROGRADE] [filenames ...]

positional arguments:
  filenames

options:
  -h, --help            show this help message and exit
  --consider-mercury-in-retrograde CONSIDER_MERCURY_IN_RETROGRADE
```
<!-- [[[end]]] -->
