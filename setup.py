from distutils.core import setup
from py2exe import freeze

freeze(
    console=["main.py"],
    windows=[],
    data_files=None,
    zipfile=None,
    options={},
    version_info={}
)