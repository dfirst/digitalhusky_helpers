import re
import unicodedata


all_chars = (chr(i) for i in range(0x110000))
control_chars = ''.join(
    char for char in all_chars
    if unicodedata.category(char) == 'Cc' and char not in ['\r', '\t', '\n']
)
control_char_re = re.compile('[%s]' % re.escape(control_chars))


def sanitize_bytes_control_chars(raw_bytes):
    """
    Clean bytes object ASCII -- Non printable Characters
    """
    try:
        return control_char_re.sub(
            '', raw_bytes.decode('utf-8')).encode('utf-8')
    except UnicodeDecodeError:
        return control_char_re.sub(
            '', raw_bytes.decode('cp1252')).encode('utf-8')


def sanitize_str_control_chars(raw_string):
    """
    Clean str object ASCII -- Non printable Characters
    """
    return control_char_re.sub('', raw_string)
