# randomly-change-self
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/randomly-change-self/0.2.0?logo=python&logoColor=FFD43B)](https://pypi.org/project/randomly-change-self/)
[![PyPI](https://img.shields.io/pypi/v/randomly-change-self?logo=Python&logoColor=FFD43B)](https://pypi.org/project/randomly-change-self/)
[![PyPI - License](https://img.shields.io/pypi/l/randomly-change-self?color=magenta)](https://github.com/sco1/randomly-change-self/blob/master/LICENSE)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sco1/randomly-change-self/main.svg)](https://results.pre-commit.ci/latest/github/sco1/randomly-change-self/main)

Change all instances of `self` to `this` in one randomly chosen scope per file.

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
usage: randomly-change-self [-h] [--replace-with REPLACE_WITH] [--consider-mercury-in-retrograde CONSIDER_MERCURY_IN_RETROGRADE] [filenames ...]

positional arguments:
  filenames

options:
  -h, --help            show this help message and exit
  --replace-with REPLACE_WITH
  --consider-mercury-in-retrograde CONSIDER_MERCURY_IN_RETROGRADE
```
<!-- [[[end]]] -->

## Arguments
### `filenames`
A collection of filename(s) to process. While this isn't required, you should probably pass some filename(s) if you want something to happen.

### `replace-with`
Specify the string to replace `"self"` with. Defaults to `"this"`

It's assumed that this value is a valid Python identifier. No validation of this is done, we're all adults here.

### `consider-mercury-in-retrograde`
Set to `True` if you only want to make changes if Mercury is in retrograde.

**NOTE:** Because it turns out that astrophysics is a little challenging and I haven't done it since college, this is currently implemented as an API call to the [Mercury Retrograde API](https://mercuryretrogradeapi.com/about.html). This call should fail gracefully, and if an issue is encountered then your flag will be ignored and your code will get changed anyway.

## Pre-Commit
You can even use this as a [pre-commit](https://pre-commit.com/) hook. Wow!

```yaml
- repo: https://github.com/sco1/randomly-change-self
  rev: v0.2.0
  hooks:
  - id: randomly-change-self
    args: [--consider-mercury-in-retrograde=False]
```
