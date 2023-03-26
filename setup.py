import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ffAlive",
    version="1.0.8",
    author="Tim Green",
    author_email="the.green.timtam@gmail.com",
    description="FFMPEG with Progress Bars",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thegreentimtam/ffAlive",
    packages=setuptools.find_packages(),
    install_requires  = ['alive_progress', 'ffmpeg_progress_yield'],
    license = 'MIT'
)
