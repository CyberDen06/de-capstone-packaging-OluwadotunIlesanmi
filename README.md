# Omnicart Pipeline

A data pipeline for analyzing seller performance in e-commerce systems.

## Features

- Fetches product and user data from e-commerce APIs
- Enriches data with computed metrics
````markdown
# Omnicart Pipeline

A small, focused data pipeline and CLI for enriching and analyzing e-commerce product and seller data.

This project ingests product and user data, enriches product rows with user (seller) information,
computes per-item revenue metrics, and produces reports useful for seller performance analysis.

## Installation

Install the published package from PyPI:

```bash
pip install omnicart-pipeline
```

If you're installing from source for development:

```bash
git clone https://github.com/yourusername/omnicart-pipeline.git
cd omnicart-pipeline
pip install -e .
```

## Usage

Run the command-line tool. The entry point provided by the package is `omnicart-pipeline`.

Basic usage:

```bash
# Run the pipeline with default config
omnicart-pipeline

# Use a custom config file and write JSON report
omnicart-pipeline --config pipeline.cfg --output report.json

# Show help
omnicart-pipeline --help
```

Notes for Windows PowerShell users: invoke the command the same way; if you installed the package into a virtual environment,
activate it first.

### Python API (programmatic)

You can also run the pipeline from Python:

```python
from omnicart_pipeline.pipeline import Pipeline

pipeline = Pipeline(config_path="pipeline.cfg")
pipeline.run(output_file="report.json")
```

## Configuration (.cfg files)

The pipeline accepts a configuration file in standard INI format (extension `.cfg` or `.ini`). A minimal example:

```ini
[api]
base_url = https://api.example.com
limit = 100

[output]
format = json
path = report.json
```

How this project packages and loads `.cfg` files (the package-data challenge):

- Packaging: include default config files in package data so installations from PyPI contain them. In `pyproject.toml` or
   `setup.cfg` we add the config file path under `package_data` (or use `include_package_data = True` with MANIFEST.in).

- Runtime access: use `importlib.resources` (Python 3.7+) to access bundled config files in a safe, cross-platform way. That avoids fragile file-system assumptions when the package is installed as a wheel.

   Example pattern used in the codebase:

   1. If the user passes `--config` / `--config-path`, read that file directly using `configparser`.
   2. Otherwise, attempt to load the built-in default config with `importlib.resources.files("omnicart_pipeline").joinpath("default.cfg")`.
   3. Fall back to reasonable defaults hard-coded in the pipeline if neither is available.

- This approach meets package distribution constraints (config shipped as package data) and runtime constraints (works when installed as wheel or editable install).

## Example: reading a config in code

```python
import configparser
from importlib import resources

config = configparser.ConfigParser()
if user_config_path:
      config.read(user_config_path)
else:
      # load bundled default
      with resources.open_text("omnicart_pipeline", "default.cfg") as fh:
            config.read_file(fh)
```

## What I changed / solution summary

- Provide a single CLI entrypoint `omnicart-pipeline` for easy user runs.
- Include packaged configuration files and use `importlib.resources` for reliable access.
- Accept a user-supplied config path to override defaults at runtime.

## Troubleshooting & notes

- If `omnicart-pipeline` is not found after installation, ensure your Python `scripts`/`bin` directory is on PATH, or activate the virtualenv where it was installed.
- To include additional config templates in packaging, add them to `package_data` in `pyproject.toml` or `setup.cfg` and update `MANIFEST.in` for source distributions.

## License

MIT
````