project(
    'hiberlite',
    'c',
    'cpp',
    version: files('version.txt'),
    default_options: ['warning_level=3', 'cpp_std=c++17'],
)

# Add include folder with public headers
subdir('include')

# Add source folder with private headers and sources for the library
subdir('src')

# Add test folder with unit and integration tests
subdir('test')

# Add appd folder with applications and examples
subdir('apps')

pkg_mod = import('pkgconfig')
pkg_mod.generate(
    name: 'hiberlite',
    filebase: 'hiberlite',
    description: 'C++ ORM for SQLite',
    subdirs: 'hiberlite',
    libraries: hiberlite_lib,
    version: '0.1',
)
