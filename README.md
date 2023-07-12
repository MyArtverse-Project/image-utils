# MyFursona Image Utilities

This repository contains Python scripts for advanced image manipulation for generating images and files of your fluffy creatures!

## Directory structure

| Folder      | Description                                                                                    | Libraries                   |
| ----------- | ---------------------------------------------------------------------------------------------- | --------------------------- |
| `cards`     | Generating a character's info that's printable for cards both in image and SVGs                | Pillow, Qt5                 |
| `photoshop` | For creating Adobe Photoshop file to scaffold a canvas for ref sheets and a character's avatar | [psd-tools][psdlib], Pillow |

Procreate, MediBang, still WIP!

## Contributing

Requires Python 3.8 and up.

Clone/fork the repo, start a virtual environment

```sh
virtualenv venv
```

Install its dependencies

```sh
pip install -r requirements.txt
```

## License

GPL-2.0

[psdlib]: https://github.com/psd-tools/psd-tools
