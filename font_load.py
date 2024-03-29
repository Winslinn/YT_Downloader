from ctypes import windll, byref, create_string_buffer

def load(font_list: list):
    if len(font_list) > 0:
        for font_path in font_list:
            pathbuf = create_string_buffer(255, font_path)
            windll.gdi32.AddFontResourceExA(byref(pathbuf))