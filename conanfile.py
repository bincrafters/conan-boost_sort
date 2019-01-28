#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostSortConan(base.BoostBaseConan):
    name = "boost_sort"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_sort"
    lib_short_names = ["sort"]
    header_only_libs = ["sort"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_range",
        "boost_serialization",
        "boost_static_assert",
        "boost_type_traits"
    ]
