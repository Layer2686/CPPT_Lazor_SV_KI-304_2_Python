"""Перевірки аргументів CLI."""

import pytest

from kzp_lab06.cli import main


def test_help(capsys):
    """Довідка завершується успішно й описує обидва шляхи."""
    with pytest.raises(SystemExit) as result:
        main(["--help"])

    assert result.value.code == 0
    assert "INPUT OUTPUT" in capsys.readouterr().out


def test_missing_paths(capsys):
    """Відсутність обов’язкових шляхів дає помилку аргументів."""
    with pytest.raises(SystemExit) as result:
        main([])

    assert result.value.code == 2
    assert "error:" in capsys.readouterr().err
