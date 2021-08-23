"""Setup for iframe XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='smowlreg-id-xblock',
    version='70.3',
    description='SMOWL REG',
    packages=[
        'smowlreg',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'smowlreg = smowlreg:SmowlRegXBlock',
        ],
        "lms.djangoapp": [
            "smowlreg = smowlreg.apps:SmowlRegConfig",
        ],
        "cms.djangoapp": [
            "smowlreg = smowlreg.apps:SmowlRegConfig",
        ]
    },
    package_data=package_data("smowlreg", ["static", "templates", "public"]),
)
