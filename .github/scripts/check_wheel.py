"""Перевірити встановлення й запуск wheel у чистому середовищі."""

import os
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path


def main() -> None:
    """Встановити wheel і перевірити обидві точки входу поза проєктом."""
    with Path("pyproject.toml").open("rb") as source:
        project = tomllib.load(source)["project"]

    wheels = list(Path("dist").resolve().glob("*.whl"))
    if len(wheels) != 1:
        raise SystemExit(f"Очікувався один wheel у dist/, знайдено {len(wheels)}")
    (wheel,) = wheels
    ((script, entry_point),) = project["scripts"].items()
    module, _ = entry_point.split(":")
    with tempfile.TemporaryDirectory() as directory:
        environment = Path(directory)
        subprocess.run([sys.executable, "-m", "venv", environment], check=True)
        bin_dir = environment / ("Scripts" if os.name == "nt" else "bin")
        python = bin_dir / ("python.exe" if os.name == "nt" else "python")
        command = bin_dir / (f"{script}.exe" if os.name == "nt" else script)
        subprocess.run(
            [python, "-m", "pip", "install", "--no-deps", wheel],
            cwd=environment,
            check=True,
        )
        for invocation in ([python, "-m", module], [command]):
            result = subprocess.run(
                [*invocation, "--version"],
                cwd=environment,
                capture_output=True,
                text=True,
                check=True,
            )
            if result.stdout.strip() != project["version"]:
                raise SystemExit(f"Неочікувана версія: {result.stdout!r}")

            result = subprocess.run(invocation, cwd=environment, capture_output=True)
            if result.returncode != 2:
                raise SystemExit(f"Очікувався код 2, отримано {result.returncode}")


if __name__ == "__main__":
    main()
