import argparse
import ast
import json
import random
from collections import abc
from pathlib import Path
from urllib.request import urlopen

import tokenize_rt

AST_DEF_NODES = ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef
AST_FUNCTION_TYPES = ast.FunctionDef | ast.AsyncFunctionDef


class FunctionVisitor(ast.NodeVisitor):
    """An ast.NodeVisitor instance for walking the AST and describing all contained methods."""

    AST_FUNC_TYPES = (ast.FunctionDef, ast.AsyncFunctionDef)

    def __init__(self) -> None:
        self.method_definitions: dict[AST_DEF_NODES, set[tokenize_rt.Offset]] = {}
        self._context: list[AST_DEF_NODES] = []

    def switch_context(self, node: AST_DEF_NODES) -> None:
        """
        Utilize a context switcher as a generic function visitor in order to track function context.

        Without keeping track of context, it's challenging to reliably differentiate class methods
        from "regular" functions, especially in the case of nested classes.
        """
        if isinstance(node, self.AST_FUNC_TYPES):
            # Check for non-empty context first to prevent IndexErrors for non-nested nodes
            if self._context:
                if isinstance(self._context[-1], ast.ClassDef):
                    self.method_definitions[node] = set()

        self._context.append(node)
        self.generic_visit(node)
        self._context.pop()

    def visit_arg(self, node: ast.arg) -> None:
        """Visit function argument nodes & add any `self` instances to its method definition."""
        if node.arg == "self":
            self.method_definitions[self._context[-1]].add(
                tokenize_rt.Offset(node.lineno, node.col_offset)
            )

    def visit_Name(self, node: ast.Name) -> None:
        """Visit `Name` nodes & add any `self` instances to its method definition."""
        if node.id == "self":
            self.method_definitions[self._context[-1]].add(
                tokenize_rt.Offset(node.lineno, node.col_offset)
            )

    visit_FunctionDef = switch_context
    visit_AsyncFunctionDef = switch_context
    visit_ClassDef = switch_context


def _process_src(src: str, replace_with: str = "this") -> str:
    tokens = tokenize_rt.src_to_tokens(src)

    fv = FunctionVisitor()
    fv.visit(ast.parse(src))

    # Short-circuit if we have no class definitions
    if not fv.method_definitions:
        return tokenize_rt.tokens_to_src(tokens)  # type: ignore[no-any-return]

    selfs = random.choice(list(fv.method_definitions.values()))

    new_tokens = []
    for tok in tokens:
        if tok.offset in selfs:
            new_tokens.append(tok._replace(src=replace_with))
        else:
            new_tokens.append(tok)

    return tokenize_rt.tokens_to_src(new_tokens)  # type: ignore[no-any-return]


def process_file(filepath: Path) -> None:
    """
    Change all instances of `self` to `this` in one randomly chosen scope.

    An attempt is made to keep things working after any changes are made. Hopefully I'm successful!
    """
    src = filepath.read_text()
    filepath.write_text(_process_src(src))


def is_mercury_in_retrograde() -> bool:  # noqa: D103
    """
    Determine if Mercury is currently in retrograde.

    Until the math can be implemented manually, this currently takes advantage of the Mercury
    Retrograde API. More info can be found at: https://mercuryretrogradeapi.com/about.html
    """
    with urlopen("https://mercuryretrogradeapi.com") as r:
        resp = json.loads(r.read())

    return resp["is_retrograde"]  # type: ignore[no-any-return]


def main(argv: abc.Sequence[str] | None = None) -> None:  # noqa: D103
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
