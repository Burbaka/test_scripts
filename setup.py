from setuptools import setup

setup(
    name='myscript',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'user_log_files=junk_scripts:user_log_files:generate_log_files'
        ]
    },

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # This will prevent accidental uploads to PyPi
        'Private :: Do Not Upload'
    ]
)
