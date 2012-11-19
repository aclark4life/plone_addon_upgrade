from setuptools import find_packages
from setuptools import setup

setup(
    entry_points={
        'z3c.autoinclude.plugin': 'target=plone',
    },
    name='plone_addon_upgrade',
    packages=find_packages(),
)
