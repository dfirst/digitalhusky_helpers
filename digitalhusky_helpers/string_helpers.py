import re
import unicodedata


all_chars = (unichr(i) for i in xrange(0x110000))
control_chars = ''.join(
    char for char in all_chars
    if unicodedata.category(char) == 'Cc' and char not in ['\r', '\t', '\n']
)
control_char_re = re.compile('[%s]' % re.escape(control_chars))


def sanitize_control_chars(raw_string):
    """
    Clean ASCII -- Non printable Characters
    """
    return control_char_re.sub('', raw_string)
