from setuptools import setup

setup(
    name="cli",
    py_modules=["cli"],
    entry_points={
        "console_scripts": [
            "cli = cli:main",
        ],
    },
)
