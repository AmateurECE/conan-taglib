from conans import ConanFile, CMake, tools


class TaglibConan(ConanFile):
    name = "taglib"
    version = "1.11.1"
    license = "LGPL-2.1-only"
    author = "Ethan D. Twardy ethan.twardy@gmail.com"
    url = "https://github.com/taglib/taglib"
    description = """TagLib is a library for reading and editing the metadata
    of several popular audio formats. Currently it supports both ID3v1 and
    ID3v2 for MP3 files, Ogg Vorbis comments and ID3 tags in FLAC, MPC, Speex,
    WavPack, TrueAudio, WAV, AIFF, MP4, APE, DSF, DFF, and ASF files."""
    topics = ("audio", "codec", "flac", "mp3")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/taglib/taglib")
        self.run("git --git-dir=taglib/.git --work-tree=taglib checkout v{}"
                 .format(self.version))

    def build(self):
        cmake = CMake(self)
        # Uncomment for testing:
        # self.run("cmake -DBUILD_TESTS=ON taglib")
        cmake.configure(source_folder="taglib")
        cmake.build()
        # Uncomment for testing:
        # cmake.test()

    def package(self):
        self.copy("*.h", dst="include/taglib", src="taglib/taglib/",
                  keep_path=False)
        self.copy("*.tcc", dst="include/taglib", src="taglib/taglib/",
                  keep_path=False)
        self.copy("taglib_config.h", dst="include/taglib")
        self.copy("config.h", dst="include/taglib")
        self.copy("*tag.lib", dst="lib", src="taglib", keep_path=False)
        self.copy("*.dll", dst="bin", src="taglib", keep_path=False)
        self.copy("*.so", dst="lib", src="taglib", keep_path=False)
        self.copy("*.dylib", dst="lib", src="taglib", keep_path=False)
        self.copy("*.a", dst="lib", src="taglib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["tag"]

