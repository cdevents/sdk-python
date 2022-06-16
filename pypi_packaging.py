"""Packaging and release utilities."""

import codecs
import os

import pkg_resources


def _read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def _get_version(rel_path):
    for line in _read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


# FORMAT: 1.x.x
pypi_config = {
    "version_target": _get_version("cdevents/__init__.py"),
    "package_name": "cdevents",
}


def _createTag():
    from git import Repo

    # Get local pypi cloudevents version
    published_pypi_version = pkg_resources.get_distribution(pypi_config["package_name"]).version

    # Ensure pypi and local package versions match
    if pypi_config["version_target"] == published_pypi_version:
        # Create local git tag
        repo = Repo(os.getcwd())
        repo.create_tag(pypi_config["version_target"])

        # Push git tag to remote master
        origin = repo.remote()
        origin.push(pypi_config["version_target"])

    else:
        # PyPI publish likely failed
        print(
            f"Expected {pypi_config['package_name']}=={pypi_config['version_target']} "
            f"but found {pypi_config['package_name']}=={published_pypi_version}"
        )
        exit(1)


if __name__ == "__main__":
    _createTag()
