# Extract info from BMP image array.
import struct

# BMP of a smiley face
File1_Table = bytes([
0x42,0x4D,0xCA,0x07,0x00,0x00,0x00,0x00,0x00,0x00,0x8A,0x00,0x00,0x00,0x7C,0x00,
0x00,0x00,0x20,0x00,0x00,0x00,0x1D,0x00,0x00,0x00,0x01,0x00,0x10,0x00,0x03,0x00,
0x00,0x00,0x40,0x07,0x00,0x00,0x13,0x0B,0x00,0x00,0x13,0x0B,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xF8,0x00,0x00,0xE0,0x07,0x00,0x00,0x1F,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x42,0x47,0x52,0x73,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x02,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x08,0x20,0x08,0x40,0x10,0x40,0x10,0x20,0x08,0x00,0x08,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x80,0x20,
0x60,0x49,0x40,0x62,0xE0,0x82,0x60,0x93,0x80,0x93,0x80,0x93,0x60,0x93,0xE0,0x7A,
0x40,0x62,0x60,0x41,0x80,0x20,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x40,0x18,0xA0,0x51,0x00,0x83,
0x20,0xA4,0xA0,0xB4,0xE0,0xBC,0x00,0xC5,0x20,0xC5,0x20,0xC5,0x00,0xC5,0xE0,0xBC,
0xA0,0xB4,0x20,0xA4,0x00,0x83,0xA0,0x51,0x40,0x10,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x39,0xA0,0x7A,0x20,0xA4,0x20,0xC5,
0x82,0xCD,0x09,0xDE,0x8E,0xE6,0x11,0xEF,0x32,0xF7,0x12,0xEF,0x12,0xEF,0xAF,0xE6,
0x2A,0xDE,0xA4,0xCD,0x20,0xC5,0x20,0xA4,0xA0,0x7A,0xE0,0x30,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x40,0x41,0x60,0x8B,0xA0,0xB4,0x82,0xCD,0x6A,0xDE,
0xF6,0xE6,0x9C,0xF7,0xBD,0xF7,0xDE,0xFF,0xDE,0xFF,0xDE,0xF7,0xDE,0xFF,0xBE,0xF7,
0x9C,0xF7,0x38,0xEF,0x4B,0xDE,0x62,0xCD,0xA0,0xB4,0x40,0x8B,0x40,0x41,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x40,0x41,0x60,0x93,0xE0,0xBC,0xC7,0xD5,0xB3,0xE6,0x5C,0xEF,
0xDF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xDF,0xFF,0xFF,0xFF,0xFF,0xFF,
0xFF,0xFF,0xDF,0xFF,0x5C,0xEF,0xB4,0xDE,0x87,0xCD,0xE0,0xBC,0x60,0x93,0x20,0x39,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0xE0,0x30,0x20,0x8B,0xC0,0xBC,0xA7,0xD5,0x96,0xDE,0x3C,0xE7,0x9D,0xEF,
0xDF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xDF,0xFF,0xFF,0xFF,0xFF,0xFF,
0xFF,0xFF,0xDF,0xFF,0x9D,0xEF,0x3C,0xE7,0x76,0xD6,0x88,0xCD,0xC0,0xBC,0x20,0x83,
0xC0,0x28,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x60,0x6A,0x80,0xB4,0x67,0xC5,0x35,0xCE,0xFB,0xDE,0x3C,0xE7,0x9D,0xEF,
0xDF,0xFF,0xFF,0xFF,0xBE,0xF7,0xFF,0xFF,0xBE,0xF7,0x7D,0xEF,0xFF,0xFF,0xBE,0xF7,
0xDF,0xFF,0xDF,0xFF,0x7D,0xEF,0x3C,0xE7,0xDB,0xDE,0x35,0xCE,0x47,0xC5,0x80,0xB4,
0x60,0x6A,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x40,0x41,0xA0,0x9B,0x01,0xBD,0xD2,0xC5,0x99,0xCE,0xFB,0xDE,0x3C,0xE7,0x5D,0xEF,
0x7D,0xEF,0xDF,0xFF,0xBE,0xF7,0xFF,0xFF,0xFF,0xFF,0xDE,0xF7,0xFF,0xFF,0xBE,0xF7,
0xDE,0xF7,0x9E,0xF7,0x3C,0xE7,0x3C,0xE7,0xDB,0xDE,0x79,0xCE,0xB1,0xC5,0x01,0xC5,
0xA0,0x9B,0x20,0x39,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x20,0x10,
0x60,0x72,0xA0,0xB4,0x2B,0xC5,0xF7,0xC5,0x9A,0xD6,0xDB,0xDE,0xFB,0xDE,0x7D,0xEF,
0xDE,0xF7,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xDF,0xFF,0xFF,0xFF,0xDF,0xFF,
0xFF,0xFF,0xDF,0xFF,0x7D,0xEF,0xFB,0xDE,0xBA,0xD6,0x79,0xCE,0xF7,0xBD,0x4B,0xC5,
0xA0,0xB4,0x60,0x6A,0x20,0x08,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xC0,0x30,
0x80,0x93,0xE4,0xBC,0x52,0xB5,0x18,0xC6,0x59,0xCE,0xDB,0xDE,0x3C,0xE7,0x9D,0xEF,
0xDF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xDF,0xFF,0xFF,0xFF,0xDF,0xFF,
0xFF,0xFF,0xDF,0xFF,0x7D,0xEF,0x3C,0xE7,0xDB,0xDE,0x59,0xCE,0xF7,0xBD,0x52,0xB5,
0x04,0xBD,0x60,0x93,0xC0,0x28,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x60,0x49,
0x20,0xA4,0xE8,0xBC,0x54,0xAD,0x18,0xC6,0x99,0xCE,0xFB,0xDE,0x3C,0xE7,0x9D,0xEF,
0xDF,0xFF,0xDF,0xFF,0x9D,0xEF,0x9D,0xEF,0x3C,0xE7,0xFB,0xDE,0x7D,0xEF,0x7D,0xEF,
0xBE,0xF7,0xDF,0xF7,0x9D,0xEF,0x3C,0xE7,0xDB,0xDE,0x79,0xCE,0xF7,0xBD,0x54,0xAD,
0x09,0xBD,0x20,0xA4,0x60,0x41,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xE0,0x59,
0x60,0xAC,0xAB,0xB4,0x55,0xAD,0x18,0xC6,0x9A,0xD6,0xFB,0xDE,0x3C,0xE7,0x5C,0xE7,
0xDA,0xDE,0x56,0xD6,0x70,0xC5,0xAE,0xCD,0xCC,0xCD,0xEC,0xCD,0xED,0xD5,0xAE,0xCD,
0xF3,0xCD,0x78,0xD6,0xFB,0xDE,0x3C,0xE7,0xDB,0xDE,0x99,0xCE,0x17,0xBE,0x55,0xAD,
0xCC,0xB4,0x60,0xB4,0xE0,0x59,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x40,0x62,
0x80,0xB4,0x8C,0xAC,0x55,0xAD,0x18,0xC6,0x9A,0xD6,0xBA,0xD6,0x37,0xCE,0x91,0xC5,
0xA8,0xD5,0x64,0xEE,0x05,0xF7,0x68,0xFF,0xAC,0xFF,0xAC,0xFF,0x8A,0xFF,0x46,0xFF,
0xC2,0xF6,0x25,0xE6,0xAD,0xD5,0xF5,0xC5,0x9A,0xD6,0x99,0xCE,0x18,0xC6,0x75,0xAD,
0xAE,0xA4,0x81,0xB4,0x20,0x62,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x60,0x6A,
0x80,0xB4,0x6D,0xA4,0x55,0xA5,0x18,0xC6,0x17,0xC6,0x51,0xBD,0x87,0xD5,0x83,0xF6,
0xE3,0xFE,0x03,0xFF,0x26,0xFF,0x69,0xFF,0x8A,0xFF,0x8B,0xFF,0x69,0xFF,0x46,0xFF,
0x03,0xFF,0xE0,0xFE,0xC0,0xF6,0xE5,0xDD,0x50,0xBD,0x17,0xC6,0x17,0xBE,0x75,0xAD,
0x90,0x9C,0x81,0xB4,0x40,0x6A,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x40,0x62,
0x80,0xB4,0x4B,0xA4,0xB2,0x94,0x33,0xAD,0xEC,0xBC,0x06,0xE6,0xC6,0xF6,0xE6,0xFE,
0x05,0xFF,0x05,0xFF,0x27,0xFF,0x48,0xFF,0x69,0xFF,0x69,0xFF,0x48,0xFF,0x26,0xFF,
0x04,0xFF,0xE2,0xFE,0xC2,0xFE,0xA2,0xF6,0xE2,0xE5,0xEC,0xBC,0x75,0xB5,0x34,0xA5,
0x6F,0x94,0x81,0xB4,0x40,0x62,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x5A,
0x60,0xAC,0x86,0xB4,0x4C,0xA4,0xE8,0xBC,0x69,0xE6,0xC9,0xF6,0xE9,0xF6,0x08,0xFF,
0x08,0xFF,0x08,0xFF,0x28,0xFF,0x28,0xFF,0x49,0xFF,0x49,0xFF,0x28,0xFF,0x26,0xFF,
0x05,0xFF,0xE5,0xFE,0xE5,0xFE,0xC4,0xF6,0x84,0xF6,0xE3,0xDD,0xCB,0xB4,0x91,0x94,
0x6D,0xA4,0x60,0xB4,0xE0,0x59,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x80,0x49,
0x20,0xAC,0x00,0xC5,0x20,0xCD,0x4A,0xE6,0xCC,0xEE,0x0A,0xD6,0x27,0xBD,0x0B,0xF7,
0x2B,0xFF,0x2A,0xFF,0x2A,0xFF,0x2A,0xFF,0x2A,0xFF,0x29,0xFF,0x29,0xFF,0x08,0xFF,
0x08,0xFF,0x08,0xFF,0xE7,0xFE,0xC7,0xF6,0x44,0xC5,0xC4,0xAC,0xC4,0xDD,0xC7,0xBC,
0xC5,0xBC,0x20,0xAC,0x60,0x49,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xE0,0x30,
0x80,0x93,0xE0,0xBC,0x41,0xCD,0x8D,0xE6,0xEF,0xEE,0xEC,0xCD,0x82,0x39,0x47,0x9C,
0x4B,0xDE,0xAC,0xEE,0x2A,0xD6,0x07,0xB5,0xAB,0xE6,0x2C,0xFF,0xEB,0xF6,0xC6,0xAC,
0xC8,0xD5,0x89,0xE6,0x48,0xDE,0xC5,0xAC,0xA1,0x41,0x65,0xA4,0x27,0xDE,0x60,0xCD,
0x00,0xC5,0x60,0x93,0xE0,0x30,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x20,0x08,
0xA0,0x7A,0x80,0xB4,0x21,0xC5,0x8F,0xE6,0x11,0xEF,0xB0,0xE6,0x27,0x73,0x01,0x00,
0xE3,0x41,0x65,0x52,0xC4,0x41,0xE8,0x8B,0x0E,0xF7,0x4E,0xFF,0x2E,0xFF,0xE9,0xB4,
0xC4,0x41,0x64,0x52,0x03,0x4A,0x01,0x00,0xA2,0x41,0xEA,0xD5,0x09,0xDE,0x40,0xCD,
0xA0,0xB4,0x80,0x72,0x20,0x08,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x40,0x41,0xC0,0xA3,0xE0,0xBC,0x4F,0xDE,0x34,0xEF,0x34,0xF7,0x51,0xD6,0xCA,0x83,
0xA9,0x5A,0x0A,0x63,0x8C,0x9C,0xF1,0xEE,0x71,0xFF,0x51,0xFF,0x51,0xFF,0x10,0xF7,
0x0C,0xB5,0x0A,0x6B,0xA9,0x5A,0x48,0x73,0xAC,0xC5,0xAE,0xEE,0xC9,0xD5,0x00,0xC5,
0xC0,0xA3,0x40,0x39,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x80,0x72,0x80,0xB4,0xAC,0xCD,0x36,0xEF,0x56,0xF7,0x76,0xF7,0x35,0xEF,
0xB3,0xE6,0xD3,0xE6,0x54,0xF7,0x74,0xFF,0x74,0xFF,0x74,0xFF,0x73,0xFF,0x73,0xFF,
0x52,0xF7,0xD1,0xE6,0x91,0xDE,0xD1,0xE6,0xF1,0xEE,0xB0,0xE6,0x67,0xCD,0x80,0xB4,
0x80,0x72,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x31,0x40,0x93,0xC6,0xBC,0xB5,0xE6,0x79,0xF7,0x79,0xF7,0x98,0xF7,
0x98,0xF7,0x98,0xFF,0x97,0xFF,0x97,0xFF,0x97,0xFF,0x96,0xFF,0x96,0xFF,0x76,0xFF,
0x75,0xFF,0x75,0xF7,0x55,0xF7,0x34,0xF7,0x14,0xEF,0x2F,0xDE,0xC2,0xBC,0x40,0x8B,
0xE0,0x30,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x60,0x41,0x80,0x9B,0x09,0xBD,0xF7,0xE6,0xBB,0xF7,0xBB,0xF7,
0xBB,0xFF,0xBA,0xFF,0xBA,0xFF,0xBA,0xFF,0xB9,0xFF,0x99,0xFF,0x99,0xFF,0x98,0xF7,
0x98,0xF7,0x78,0xF7,0x57,0xF7,0x57,0xF7,0x72,0xDE,0xE5,0xBC,0x80,0x9B,0x60,0x41,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x80,0x49,0x80,0x93,0x0A,0xBD,0xF8,0xE6,0xBD,0xF7,
0xDD,0xFF,0xDD,0xFF,0xDD,0xFF,0xDC,0xFF,0xDC,0xFF,0xBC,0xFF,0xBB,0xFF,0xBB,0xFF,
0xBB,0xF7,0x9A,0xF7,0x59,0xF7,0x73,0xDE,0xC7,0xBC,0x80,0x93,0x60,0x49,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x40,0x39,0xE0,0x82,0x67,0xB4,0xD1,0xCD,
0x3A,0xEF,0xDE,0xFF,0xFF,0xFF,0xFF,0xFF,0xFE,0xFF,0xFE,0xFF,0xDE,0xFF,0xDE,0xFF,
0xBD,0xF7,0xD7,0xE6,0x8E,0xCD,0x44,0xAC,0xE0,0x82,0x20,0x39,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x40,0x10,0x00,0x62,0x40,0x93,
0x22,0xAC,0x2C,0xBD,0x34,0xD6,0xD8,0xE6,0xF9,0xE6,0xF9,0xE6,0xB8,0xE6,0x14,0xD6,
0x0A,0xBD,0x22,0xAC,0x40,0x93,0x00,0x62,0x40,0x10,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xC0,0x28,
0xA0,0x51,0x60,0x6A,0x00,0x8B,0x80,0x9B,0xC0,0xA3,0xC0,0xA3,0x80,0x9B,0x00,0x8B,
0x60,0x6A,0xA0,0x49,0xC0,0x20,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])

# BMP header structure
BMP_HEADER_SIZE = 14
BITMAP_INFO_HEADER_SIZE = 40

def processBMP():
    
    header = File1_Table[:BMP_HEADER_SIZE]
    bfType = header[0:2].decode('ascii')
    bfSize = struct.unpack('<I', header[2:6])[0]
    bfReserved1 = struct.unpack('<H', header[6:8])[0]
    bfReserved2 = struct.unpack('<H', header[8:10])[0]
    bfOffBits = struct.unpack('<I', header[10:14])[0]

    bitmapInfoHeader = File1_Table[BMP_HEADER_SIZE:BMP_HEADER_SIZE+BITMAP_INFO_HEADER_SIZE]
    biSize = struct.unpack('<I', bitmapInfoHeader[0:4])[0]
    biWidth = struct.unpack('<I', bitmapInfoHeader[4:8])[0]
    biHeight = struct.unpack('<I', bitmapInfoHeader[8:12])[0]
    biPlanes = struct.unpack('<H', bitmapInfoHeader[12:14])[0]
    biBitCount = struct.unpack('<H', bitmapInfoHeader[14:16])[0]
    biCompression = struct.unpack('<I', bitmapInfoHeader[16:20])[0]
    biSizeImage = struct.unpack('<I', bitmapInfoHeader[20:24])[0]
    biXPelsPerMeter = struct.unpack('<I', bitmapInfoHeader[24:28])[0]
    biYPelsPerMeter = struct.unpack('<I', bitmapInfoHeader[28:32])[0]
    biClrUsed = struct.unpack('<I', bitmapInfoHeader[32:36])[0]
    biClrImportant = struct.unpack('<I', bitmapInfoHeader[36:40])[0]

    # Calculations
    dataOffset = BMP_HEADER_SIZE + BITMAP_INFO_HEADER_SIZE
    dataEndOffset = dataOffset + biSizeImage
    imageSize = biSizeImage
    
    # Check if its RGB565 or RGB888
    if biBitCount == 16:
        colorDepth = "RGB565"
    elif biBitCount == 24:
        colorDepth = "RGB888"
    else:
        colorDepth = "Unknown"

    # Print the image properties
    print("BMP Header:")
    print("  bfType:", bfType)
    print("  bfSize:", bfSize)
    print("  bfReserved1:", bfReserved1)
    print("  bfReserved2:", bfReserved2)
    print("  bfOffBits:", bfOffBits)
    print("\n\rBitmap Info Header:")
    print("  biSize:", biSize)
    print("  biWidth:", biWidth)
    print("  biHeight:", biHeight)
    print("  biPlanes:", biPlanes)
    print("  biBitCount:", biBitCount)
    print("  biCompression:", biCompression)
    print("  biSizeImage:", biSizeImage)
    print("  biXPelsPerMeter:", biXPelsPerMeter)
    print("  biYPelsPerMeter:", biYPelsPerMeter)
    print("  biClrUsed:", biClrUsed)
    print("  biClrImportant:", biClrImportant)
    print("\n\rBitmap Extra Info:")
    print("  Data Offset:", dataOffset)
    print("  Data End Offset:", dataEndOffset)
    print("  Image Size:", imageSize)
    print("  Color Depth:", colorDepth)

processBMP()

"""
The offset values:
Signature ("BM") - Offset: 0 bytes
File Size - Offset: 2 bytes
Reserved - Offset: 6 bytes
Data Offset - Offset: 10 bytes
Size of Bitmap Info Header (biSize) - Offset: 14 bytes
Width (biWidth) - Offset: 18 bytes
Height (biHeight) - Offset: 22 bytes
Number of Color Planes (biPlanes) - Offset: 26 bytes
Color Depth (biBitCount) - Offset: 28 bytes
Compression Method (biCompression) - Offset: 30 bytes
Size of Image Data (biSizeImage) - Offset: 34 bytes
Horizontal Resolution (biXPelsPerMeter) - Offset: 38 bytes
Vertical Resolution (biYPelsPerMeter) - Offset: 42 bytes
Number of Used Colors (biClrUsed) - Offset: 46 bytes
Number of Important Colors (biClrImportant) - Offset: 50 bytes
"""
