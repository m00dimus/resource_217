#!/usr/bin/env python
#// ------------------------------------
#// Title: test_string.py
#// Description: Test examples for
#//    resource_string.py
#// Author: Jeffrey Wilson
#// Email: m00dimus@gmail.com
#// Version: 0.2-20160115 (python 3.4.3)
#// ------------------------------------

import sys
sys.path.append("../")

import unittest
import resource_string as test

class TestString(unittest.TestCase):
    def test_001_isvowel(self):
        """ Test if vowel is a vowel """

        testlist=['a','e','i','o','u']
        for val in testlist:
            got=test.isvowel(val)
            self.assertTrue(got)

    def test_001_isvowel_upper(self):
        """ Test if vowel is a vowel """

        testlist=['a','e','i','o','u']
        for val in testlist:
            got=test.isvowel(val.upper())
            self.assertTrue(got)

    def test_001_isnotvowel(self):
        """ Test if not a vowel is a vowel """

        testlist=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
        for val in testlist:
            got=test.isvowel(val)
            self.assertFalse(got)

    def test_001_isnotvowel_upper(self):
        """ Test if not a vowel is a vowel """

        testlist=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
        for val in testlist:
            got=test.isvowel(val.upper())
            self.assertFalse(got)

    def test_001_invalid_vowel(self):
        """ Test for invalid inputs """
        testlist=['1',1,3.14,'!','abc',(1,2,'a')]
        for val in testlist:
            got=test.isvowel(val)
            self.assertFalse(got)

    def test_001_isconsonant(self):
        """ Test if consonant is a consonant """

        testlist=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
        for val in testlist:
            got=test.isconsonant(val)
            self.assertTrue(got)

    def test_001_isconsonant_upper(self):
        """ Test if consonant is a consonant """

        testlist=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
        for val in testlist:
            got=test.isconsonant(val.upper())
            self.assertTrue(got)

    def test_001_isnotconsonant(self):
        """ Test if not a consonant is a consonant """

        testlist=['a','e','i','o','u']
        for val in testlist:
            got=test.isconsonant(val)
            self.assertFalse(got)

    def test_001_isnotconsonant_upper(self):
        """ Test if not a consonant is a consonant """

        testlist=['a','e','i','o','u']
        for val in testlist:
            got=test.isconsonant(val.upper())
            self.assertFalse(got)

    def test_001_invalid_consonant(self):
        """ Test for invalid inputs """
        testlist=['1',1,3.14,'!','abc',(1,2,'a')]
        for val in testlist:
            got=test.isconsonant(val)
            self.assertFalse(got)

    def test_001_suppressleadingzeros(self):
        """ Test to suppress leading zeros """

        val='01'
        want='1'
        got=test.suppressleadingzeros(val)
        self.assertEqual(got,want)

    def test_001_suppressleadingzeros_blank(self):
        """ Test to suppress leading zeros for blank input"""

        val=''
        want=''
        got=test.suppressleadingzeros(val)
        self.assertEqual(got,want)

    def test_001_suppressleadingzeros_allzeros(self):
        """ Test to suppress leading zeros for all zeros """

        val='0000'
        want=''
        got=test.suppressleadingzeros(val)
        self.assertEqual(got,want)

    def test_001_suppressleadingzeros_return(self):
        """ Test to suppress leading zeros for no changes"""

        val='1234'
        want='1234'
        got=test.suppressleadingzeros(val)
        self.assertEqual(got,want)

    def test_001_suppressleadingzeros_float(self):
        """ Test to suppress leading zeros in float value as string"""

        val='03.145'
        want='3.145'
        got=test.suppressleadingzeros(val)
        self.assertEqual(got,want)

    def test_001_suppressleadingzeros_more(self):
        """ Test to suppress one or more leading zeros """

        val='0001'
        want='1'
        got=test.suppressleadingzeros(val)
        self.assertEqual(got,want)

        val='000000000001'
        want='1'
        got=test.suppressleadingzeros(val)
        self.assertEqual(got,want)

    def test_001_suppressleadingzeros_string(self):
        """ Test to suppress leading zeros """

        val='one 01 two'
        want='one 1 two'
        got=test.suppressleadingzeros(val)
        self.assertEqual(got,want)

    def test_001_suppressleadingzeros_more(self):
        """ Test to suppress one or more leading zeros """

        val='one 0001 two'
        want='one 1 two'
        got=test.suppressleadingzeros(val)
        self.assertEqual(got,want)

        val='one 000000000001 two'
        want='one 1 two'
        got=test.suppressleadingzeros(val)
        self.assertEqual(got,want)

    def test_001_suppressleadingzeros_multiple(self):
        """ Test to suppress one or more leading zeros with multiple occurances"""

        val='one 0001 two 0002 three 3'
        want='one 1 two 2 three 3'
        got=test.suppressleadingzeros(val)
        self.assertEqual(got,want)

    def test_001_spacing(self):
        """ Test for standard spacing for string with only single spaces """

        val='The quick brown fox jumps over the lazy dog.'
        want='The quick brown fox jumps over the lazy dog.'
        got=test.stringspacing(val)
        self.assertEqual(got,want)

    def test_001_spacing_indent(self):
        """ Test for standard spacing for string with single spaces and leading indentation """

        val='    The quick brown fox jumps over the lazy dog.'
        want='The quick brown fox jumps over the lazy dog.'
        got=test.stringspacing(val)
        self.assertEqual(got,want)

    def test_001_spacing_multiline(self):
        """ Test for standard spacing for string with only single spaces """

        val='The quick brown fox\njumps over the lazy dog.'
        want='The quick brown fox\njumps over the lazy dog.'
        got=test.stringspacing(val)
        self.assertEqual(got,want)

    def test_001_spacing_unexpected(self):
        """ Test for standard spacing for string with unexpected double spaces """

        val='The quick brown  fox jumps over  the lazy dog.'
        want='The quick brown fox jumps over the lazy dog.'
        got=test.stringspacing(val)
        self.assertEqual(got,want)

    def test_001_spacing_unexpected_triple(self):
        """ Test for standard spacing for string with unexpected triple space """

        val='The quick brown   fox jumps over the lazy dog.'
        want='The quick brown fox jumps over the lazy dog.'
        got=test.stringspacing(val)
        self.assertEqual(got,want)

    def test_001_spacing_singledouble(self):
        """ Test for standard spacing for string to double spacing """

        val='The quick brown fox jumps over the lazy dog.'
        want='The  quick  brown  fox  jumps  over  the  lazy  dog.'
        got=test.stringspacing(val,doublespace=True)
        self.assertEqual(got,want)

    def test_001_spacing_double(self):
        """ Test for standard double spacing for string """

        val='The  quick  brown  fox  jumps  over  the  lazy  dog.'
        want='The  quick  brown  fox  jumps  over  the  lazy  dog.'
        got=test.stringspacing(val,doublespace=True)
        self.assertEqual(got,want)

    def test_001_spacing_double_indent(self):
        """ Test for standard double spacing for string with single spaces and leading indentation """

        val='    The quick brown fox jumps over the lazy dog.'
        want='The  quick  brown  fox  jumps  over  the  lazy  dog.'
        got=test.stringspacing(val,doublespace=True)
        self.assertEqual(got,want)

    def test_001_spacing_double_multiline(self):
        """ Test for standard spacing for string with only single spaces """

        val='The quick brown fox\njumps over the lazy dog.'
        want='The  quick  brown  fox\njumps  over  the  lazy  dog.'
        got=test.stringspacing(val,doublespace=True)
        self.assertEqual(got,want)

if __name__ == '__main__':
    unittest.main(verbosity=1)
