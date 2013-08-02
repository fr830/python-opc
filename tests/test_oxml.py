# -*- coding: utf-8 -*-
#
# test_oxml.py
#
# Copyright (C) 2013 Steve Canny scanny@cisco.com
#
# This module is part of python-pptx and is released under the MIT License:
# http://www.opensource.org/licenses/mit-license.php

"""Test suite for opc.oxml module."""

from opc.constants import RELATIONSHIP_TARGET_MODE as RTM

from .unitdata import a_Relationship


class DescribeCT_Relationship(object):

    def it_provides_read_access_to_xml_values(self):
        rel = a_Relationship().element
        assert rel.rId == 'rId9'
        assert rel.reltype == 'ReLtYpE'
        assert rel.target_ref == 'docProps/core.xml'
        assert rel.target_mode == RTM.INTERNAL