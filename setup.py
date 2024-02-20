from setuptools import setup

from mamba_json_formatter import get_version


setup(
    name='mamba-json-formatter',
    version=get_version(),
    license='MIT/X11',
    author='Quique Porta',
    author_email='quiqueporta@gmail.com',
    description='JSON formatter for mamba',
    long_description=open('README.md').read(),
    url='https://github.com/quiqueporta/mamba-json-formatter',
    download_url='https://github.com/quiqueporta/mamba-json-formatter/releases',
    keywords=['python', 'testing'],
    packages=['mamba_json_formatter'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    install_requires=['mamba'],
)