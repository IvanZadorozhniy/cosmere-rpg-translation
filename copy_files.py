import argparse
import os
from pathlib import Path
import json

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--path", help="Path for files in Foundry")


def ensure_folder_exists(folder_path):
    """Ensure that the folder exists; create it if it doesn't."""
    if not folder_path.exists():
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {folder_path}")


def copy_file(src, dst):

    ensure_folder_exists(dst.parent)

    if os.name == "nt":  # Windows
        cmd = f'copy "{src}" "{dst}"'
    else:  # Unix/Linux
        cmd = f'cp "{src}" "{dst}"'
    os.system(cmd)
    print(f"Copied {src} to {dst}")


COMPENDIUM_PATH = Path("compendium/cosmere-rpg-playtest")
ESM_PATH = Path("esm")
I18N_PATH = Path("i18n/systems")

MODULE_INFO = {
    "lang": "ru",
    "name": "cosmere-rpg",
    "path": "i18n/systems/cosmere-rpg.json",
}


def main(path):
    foundry_path = Path(path)
    ru_ru_path = foundry_path / "Data" / "modules" / "ru-ru"

    for dir in (COMPENDIUM_PATH, ESM_PATH, I18N_PATH):
        for file in list(dir.iterdir()):
            copy_file(file, ru_ru_path / file)

    with open(ru_ru_path / "module.json", "r") as file:
        module_json = json.load(file)

    module_json["languages"].append(MODULE_INFO)

    with open(ru_ru_path / "module.json", "w") as file:
        json.dump(module_json, file, indent=4, sort_keys=True)


if __name__ == "__main__":
    args = parser.parse_args()
    main(path=args.path)
