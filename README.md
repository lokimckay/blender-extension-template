# Blender extension template

Allows you to develop blender extensions with hot-reloading directly from commandline instead of relying on the VS Code extension which seems to be the standard method.

## Requirements

- Python 3.1+
- [PDM](https://pdm-project.org/en/latest/#installation)

## Usage

## Installation

```shell
npx degit lokimckay/blender-extension-template my_blender_extension
cd my_blender_extension
pdm install
```

## Developing

```shell
pdm dev
```

Blender will launch automatically.

Any changes made in external editors should be reflected immediately in blender.

## Features

- Automatic hot-reloading in blender when changes are made
- Get if running in dev/prod environment in python via `env.py` file
- Optionally add a "dev.blend" file in the `scripts` directory to load that file when developing

## Relevant documentation

- [How to Create Extensions](https://docs.blender.org/manual/en/latest/advanced/extensions/getting_started.html)

## Troubleshooting

- Check if your extension is enabled in `Edit` -> `Preferences`
- Ensure extension names/ids match between `config.yml` and `blender_manifest.toml`
