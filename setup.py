from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='StringMatching',
    version='0.0.1',
    description='A project for string matching algorithms.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pybitboo/StringMatching.git',
    author='yangdian',
    author_email='2406616734@qq.com',
    keywords='strmatch, stringmatching, sunday,horspool',
    packages=find_packages(),
    python_requires='>=3.6, <4',
)
