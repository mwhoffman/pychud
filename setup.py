from numpy.distutils.misc_util import Configuration
from numpy.distutils.core import setup


def configuration(parent_package='', top_path=None):
    config = Configuration(None, parent_package, top_path)
    config.add_extension('pychud', sources=['src/pychud.pyf', 'src/dchud.f', 'src/dchdd.f'], libraries=['blas'])
    return config


if __name__ == '__main__':
    setup(
        name='pychud',
        version='0.1',
        configuration=configuration)

