# Static Site Generator

A simple static site generator written in **Python**, inspired by tools like [Hugo](https://github.com/gohugoio/hugo).

The project focuses on **core backend and computer science fundamentals** such as file processing, parsing, and transformation pipelines.

The site generation process is handled directly in code and executed through shell scripts.

## Project Structure

```text
├── content/         # Markdown files (site content)
├── static/          # Static assets (CSS, images, etc.)
├── docs/            # Generated HTML output
├── src/             # Python source code
├── tests/           # Unit tests
├── scripts/         # Shell scripts
│   ├── main.sh      # Local build script
│   ├── build.sh     # Production build script (GitHub Pages)
│   └── test.sh      # Run tests
└── README.md
```

## Tech Stack

- Python
- Github Pages (deployment target)

## Features

- Converts Markdown content into static HTML pages
- Supports static assets such as CSS and images
- Simple and explicit execution flow via shell scripts
- Deployment to Github Pages

## Future Improvements

- Add a CLI to run and configure the generator more easily.
- Improve Markdown support (nested formatting and more edge cases).

## Running the Project

### Requirements
- [uv](https://docs.astral.sh/uv/) (package manager)
- Python 3.10+

### Setup

```bash
git clone <repo-url>
cd static-site-generator/

uv sync # Install all the packages
sh scripts/main.sh # Start the local server
```

You can now start editing files inside of `content/` and adding images inside `static/`.

### Deploying to Github Pages

1. Go to your repo's _settings_.
2. Navigate to _pages_.
3. Set _source_ to _deploy from branch_
4. Set the branch to _main_ and the folder to _docs/_

Now after making changes, you can run the following

```bash
sh scripts/build.sh
git push # Push changes to the repository
```

If you named the repository different, please make sure to edit the `build.sh` script as follows

```bash
# build.sh
python3 -m src.main "/<YOUR_REPO_NAME>/"
```
