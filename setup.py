NAME = 'pychud'
VERSION = '0.1.dev1'
AUTHOR = 'Matthew W. Hoffman'
AUTHOR_EMAIL = 'mwh30@cam.ac.uk'


def setup_package(parent_package='', top_path=None):
    from numpy.distutils.core import setup
    from numpy.distutils.system_info import get_info, NotFoundError
    from numpy.distutils.misc_util import Configuration

    sources = ['src/pychud.pyf', 'src/dchud.f', 'src/dchdd.f']
    extra_info = {}
    extra_link_args = []

    try:
        # try to build against the MKL.
        extra_info = get_info('mkl', 2)
        extra_link_args = ['-Wl,-rpath,'+path for path in extra_info['library_dirs']],
        print 'Linking against the MKL'

    except NotFoundError:
        try:
            # With no MKL found we'll try to link against whatever version of
            # BLAS is installed system-wide.
            extra_info = get_info('blas', 2)
            extra_link_args = ['-Wl,-rpath,'+path for path in extra_info['library_dirs']],
            print 'Linking against BLAS'

        except NotFoundError:
            # Found nothing. So we'll build the necessary linear algebra
            # functions ourselves.
            sources += ['src/ddot.f', 'src/dnrm2.f', 'src/drotg.f']
            print 'No BLAS found. Building BLAS functions manually'

    config = Configuration()
    config.add_extension(
        name='pychud',
        sources=sources,
        extra_info=extra_info,
        extra_link_args=extra_link_args
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

