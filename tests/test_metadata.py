from __future__ import annotations

import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_plugin_id_matches_repository_suffix() -> None:
    plugin = tomllib.loads((ROOT / "plugin.toml").read_text(encoding="utf-8"))["plugin"]
    assert plugin["id"] == "suno_cn_music"
    assert ROOT.name == f"n.e.k.o_plugin_{plugin['id']}"


def test_default_api_key_is_not_committed() -> None:
    config = tomllib.loads((ROOT / "plugin.toml").read_text(encoding="utf-8"))
    assert config["suno"]["api_key"] == ""


def test_plugin_toml_has_no_suno_secret() -> None:
    content = (ROOT / "plugin.toml").read_text(encoding="utf-8")
    assert not re.search(r'sk-[A-Za-z0-9]{20,}', content)


if __name__ == "__main__":
    test_plugin_id_matches_repository_suffix()
    test_default_api_key_is_not_committed()
    test_plugin_toml_has_no_suno_secret()
