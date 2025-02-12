# Blender extension template

## Requirements

- [PDM](https://pdm-project.org/en/latest/#installation)

## Usage

## Installation

```shell
degit lokimckay/blender-extension-template
pdm install
```

## Developing

```
pdm run dev
```

Any changes made in external editors should automatically reflect in blender.

## Features

- Automatic hot-reloading in blender when changes are made
- Get if running in dev/prod environment in python via `env.py` file
- Optionally add a "dev.blend" file in the `scripts` directory to load that file when developing

## Relevant documentation

- [How to Create Extensions](https://docs.blender.org/manual/en/latest/advanced/extensions/getting_started.html)

## Troubleshooting

- Check if your extension is enabled in `Edit` -> `Preferences`
- Ensure extension names/ids match between `config.yml` and `blender_manifest.toml`
