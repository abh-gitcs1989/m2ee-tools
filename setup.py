from setuptools import setup

setup(
    name             = "m2ee",
    version          = "0.5.9",
    description      = "Run and administer Mendix apps",
    author           = "mendix",
    url              = "https://github.com/mendix/m2ee-tools",
    packages         = ['m2ee'],
    package_dir      = {'m2ee': 'src/m2ee'},
    scripts          = ['src/m2ee.py'],
    install_requires = ['pyyaml', 'httplib2'],
)
