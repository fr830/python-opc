# -*- coding: utf-8 -*-
#
# phys_pkg.py
#
# Copyright (C) 2013 Steve Canny scanny@cisco.com
#
# This module is part of python-opc and is released under the MIT License:
# http://www.opensource.org/licenses/mit-license.php

"""
Provides a general interface to a *physical* OPC package, such as a zip file.
"""

from zipfile import ZipFile


class PhysPkgReader(object):
    """
    Factory for physical package reader objects.
    """
    def __new__(cls, pkg_file):
        return ZipPkgReader(pkg_file)


class ZipPkgReader(object):
    """
    Implements |PhysPkgReader| interface for a zip file OPC package.
    """
    _CONTENT_TYPES_MEMBERNAME = '[Content_Types].xml'

    def __init__(self, pkg_file):
        super(ZipPkgReader, self).__init__()
        self._zipf = ZipFile(pkg_file, 'r')

    def close(self):
        """
        Close the zip archive, releasing any resources it is using.
        """
        self._zipf.close()

    @property
    def content_types_xml(self):
        """
        Return the `[Content_Types].xml` blob from the zip package.
        """
        return self._zipf.read(self._CONTENT_TYPES_MEMBERNAME)

    def rels_xml_for(self, source_uri):
        """
        Return rels item XML for source with *source_uri* or None if no rels
        item is present.
        """
        try:
            rels_xml = self._zipf.read(source_uri.rels_uri.membername)
        except KeyError:
            rels_xml = None
        return rels_xml
