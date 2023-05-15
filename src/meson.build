hiberlite_deps = [
    dependency('sqlite3'),
]

sources = [
    'BeanLoader.cpp',
    'BeanUpdater.cpp',
    'ChildKiller.cpp',
    'CppModel.cpp',
    'Database.cpp',
    'ModelExtractor.cpp',
    'Registry.cpp',
    'shared_res.cpp',
    'SQLiteStmt.cpp',
    'Visitor.cpp',
]

# These arguments are only used to build the shared library
# not the executables that use the library.
lib_args = [
    '-DBUILDING_HIBERLITE',
]

hiberlite_lib = library(
    'hiberlite',
    sources,
    include_directories: inc_dir,
    dependencies: hiberlite_deps,
    install: true,
    cpp_args: lib_args,
    gnu_symbol_visibility: 'hidden',
)

# Make this library usable as a Meson subproject.
hiberlite_dep = declare_dependency(
    include_directories: inc_dir,
    link_with: hiberlite_lib,
    dependencies: hiberlite_deps,
)

