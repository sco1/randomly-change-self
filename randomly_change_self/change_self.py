import argparse
import typing as t
from pathlib import Path


def is_mercury_in_retrograde() -> bool:  # noqa: D103
    raise NotImplementedError


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
    if args.consider_mercury_in_retrograde and not is_mercury_in_retrograde():
        return

    for file in args.filenames:
        process_file(file)


if __name__ == "__main__":
    main()
