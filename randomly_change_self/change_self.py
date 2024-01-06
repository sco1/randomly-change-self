import argparse
import json
import typing as t
from pathlib import Path
from urllib.request import urlopen


def is_mercury_in_retrograde() -> bool:  # noqa: D103
    """
    Determine if Mercury is currently in retrograde.

    Until the math can be implemented manually, this currently takes advantage of the Mercury
    Retrograde API. More info can be found at: https://mercuryretrogradeapi.com/about.html
    """
    with urlopen("https://mercuryretrogradeapi.com") as r:
        resp = json.loads(r.read())

    return resp["is_retrograde"]  # type: ignore[no-any-return]


def process_file(filepath: Path) -> None:
    """
    Change all instances of `self` to `this` in one randomly chosen scope.

    An attempt is made to keep things working after any changes are made. Hopefully I'm successful!
    """
    raise NotImplementedError


def main(argv: t.Optional[t.Sequence[str]] = None) -> None:  # noqa: D103
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", type=Path)
    parser.add_argument("--consider-mercury-in-retrograde", type=bool, default=False)
    args = parser.parse_args(argv)

    # If you're a watcher of the stars, don't change anything unless Mercury is in retrograde
    try:
        in_retrograde = is_mercury_in_retrograde()
    except Exception:
        print("Could not determine if Mercury is in retrograde, proceeding anyway!")
        in_retrograde = True

    if args.consider_mercury_in_retrograde and not in_retrograde:
        print("Mercury isn't in retrograde, aborting...")
        return

    for file in args.filenames:
        process_file(file)


if __name__ == "__main__":
    main()
