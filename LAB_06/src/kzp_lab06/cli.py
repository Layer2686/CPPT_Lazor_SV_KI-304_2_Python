"""Точка входу командного рядка для LAB_06."""

from argparse import ArgumentParser
from importlib.metadata import version
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    """Обробити аргументи командного рядка."""
    parser = ArgumentParser(prog="kzp-lab06", description="Аналіз CSV метеостанції")
    parser.add_argument("--version", action="version", version=version("kzp-lab06"))
    parser.add_argument("input", type=Path, metavar="INPUT", help="вхідний CSV-файл")
    parser.add_argument("output", type=Path, metavar="OUTPUT", help="вихідний звіт")
    parser.parse_args(argv)

    parser.exit(1, "Обробка CSV з’явиться після реалізації завантаження та аналізу.\n")


if __name__ == "__main__":
    raise SystemExit(main())
