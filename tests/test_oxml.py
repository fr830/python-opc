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
from opc.oxml import CT_Default, CT_Override

from .unitdata import a_Default, an_Override, a_Relationship, a_Types


class DescribeCT_Default(object):

    def it_provides_read_access_to_xml_values(self):
        default = a_Default().element
        assert default.extension == 'xml'
        assert default.content_type == 'application/xml'


class DescribeCT_Override(object):

    def it_provides_read_access_to_xml_values(self):
        override = an_Override().element
        assert override.partname == '/part/name.xml'
        assert override.content_type == 'app/vnd.type'


class DescribeCT_Relationship(object):

    def it_provides_read_access_to_xml_values(self):
        rel = a_Relationship().element
        assert rel.rId == 'rId9'
        assert rel.reltype == 'ReLtYpE'
        assert rel.target_ref == 'docProps/core.xml'
        assert rel.target_mode == RTM.INTERNAL


class DescribeCT_Types(object):

    def it_provides_access_to_default_child_elements(self):
        types = a_Types().element
        assert len(types.defaults) == 2
        for default in types.defaults:
            assert isinstance(default, CT_Default)

    def it_provides_access_to_override_child_elements(self):
        types = a_Types().element
        assert len(types.overrides) == 3
        for override in types.overrides:
            assert isinstance(override, CT_Override)

    def it_should_have_empty_list_on_no_matching_elements(self):
        types = a_Types().empty().element
        assert types.defaults == []
        assert types.overrides == []
