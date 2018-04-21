from unittest import TestCase
from convert_hex_to_base64 import convert_hex_to_base64
from fixed_xor import fixed_xor


class TestSet1(TestCase):

    def test_convert_hex_to_base64(self):
        assert convert_hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    def test_fixed_xor(self):
        print fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")