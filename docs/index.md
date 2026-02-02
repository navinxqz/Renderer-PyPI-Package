# Renderer PyPI Package

[![PyPI version](https://badge.fury.io/py/renderer-pypi.svg)](https://pypi.org/project/renderer-pypi/)
[![Python versions](https://img.shields.io/pypi/pyversions/renderer-pypi)](https://pypi.org/project/renderer-pypi/)
[![License](https://img.shields.io/pypi/l/renderer-pypi)](https://pypi.org/project/renderer-pypi/)

A lightweight Python package for rendering YouTube videos and web pages directly in Jupyter notebooks, Colab, and other Python environments for seamless visualization and reference.

## Features

- **YouTube Video Embedding**: Easily embed YouTube videos with customizable dimensions.
- **Web Page Rendering**: Render web pages for quick previews.
- **Notebook Integration**: Optimized for Jupyter and Colab environments.
- **Error Handling**: Robust validation and logging for reliable operation.
- **PyPI Distribution**: Simple installation via pip.

## Installation

Install the package from PyPI:

```bash
pip install renderer-pypi
```

### Requirements

- Python >= 3.8
- Dependencies: `requests`, `py-youtube`, `ensure`

## Quick Start

### Rendering a Web Page

```python
from renderer_pypi.web import render_web_page

# Render a web page
render_web_page("https://www.linkedin.com/in/md-nawshin-navin/", width=700, height=500)
```

### Example Output

The function renders the web page directly in your notebook for easy reference.

## API Reference

### `render_web_page(url, width="100%", height="600")`

Renders a web page in the notebook.

- **Parameters**:
  - `url` (str): URL of the web page to render.
  - `width` (str): Width of the web page display (default: "100%").
  - `height` (str): Height of the web page display (default: "600").

- **Raises**: `InvalidURLException` if the URL is invalid or video is not embeddable.

## Contributing

We welcome contributions! Please see our [Contributing Guide](contributing.md) for details.

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## Support

- **Issues**: Report bugs or request features on [GitHub Issues](https://github.com/navinxqz/Renderer-PyPI-Package/issues).
- **Discussions**: Join the conversation on [GitHub Discussions](https://github.com/navinxqz/Renderer-PyPI-Package/discussions).

## Changelog

See [CHANGELOG.md](changelog.md) for version history.
