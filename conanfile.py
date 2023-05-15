import os
from conan import ConanFile
from conan.tools.meson import MesonToolchain, Meson
from conan.tools.cmake import cmake_layout
from conan.tools.build import check_min_cppstd
from conan.tools.files import load


class HiberliteConan(ConanFile):
    name = "hiberlite"
    license = "<Put the package license here>"
    author = "Jakob Widauer jakob@auterion.com"
    url = "https://github.com/jwidauer/hiberlite"
    description = "C++ ORM for SQLite"
    topics = "database", "sqlite", "orm", "cpp"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "build_coverage": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "build_coverage": False,
    }
    exports_sources = "*", "!build*", "!docs*"
    generators = "PkgConfigDeps"
    requires = [
        "sqlite3/3.41.2",
    ]

    def set_version(self):
        version_file = os.path.join(self.recipe_folder, "version.txt")
        self.version = load(self, version_file).rstrip()

    def layout(self):
        cmake_layout(self)

    def validate(self):
        check_min_cppstd(self, 17)

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def generate(self):
        tc = MesonToolchain(self)
        tc.project_options["b_coverage"] = self.options.build_coverage
        tc.generate()

    def build(self):
        meson = Meson(self)
        meson.configure()
        if not os.getenv("CONFIGURE_ONLY"):
            meson.build()

    def package(self):
        meson = Meson(self)
        meson.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
