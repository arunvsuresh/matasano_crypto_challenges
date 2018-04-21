from unittest import TestCase
from convert_hex_to_base64 import convert_hex_to_base64

class TestSet1(TestCase):

    def test_convert_hex_to_base64(self):
        assert convert_hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
