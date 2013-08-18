NAME = 'pychud'
VERSION = '0.1.dev1'
AUTHOR = 'Matthew W. Hoffman'
AUTHOR_EMAIL = 'mwh30@cam.ac.uk'


def setup_package(parent_package='', top_path=None):
    from numpy.distutils.core import setup
    from numpy.distutils.system_info import get_info
    from numpy.distutils.misc_util import Configuration

    try:
        extra_info = get_info('mkl', 2)
    except:
        extra_info = get_info('blas', 2)

    config = Configuration()
    config.add_extension(
        name='pychud',
        sources=['src/pychud.pyf', 'src/dchud.f', 'src/dchdd.f'],
        extra_info=extra_info,
        extra_link_args=['-Wl,-rpath,'+path for path in extra_info['library_dirs']],
        )

    # run the setup.
    setup(
        name=NAME,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        **config.todict()
        )


if __name__ == '__main__':
    setup_package()

