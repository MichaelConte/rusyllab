import io
import setuptools

with io.open("README.md", mode="r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="rusyllab",
    version="0.0.4",
    author="MichaelConte",
    description="Simple Python package for breaking Russian words into syllables",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    url="https://github.com/MichaelConte/rusyllab",
    packages=setuptools.find_packages(),
)
