# https://py.checkio.org/blog/design-patterns-part-1/

class ImageOpener(object):
    @staticmethod
    def open(filename):
        raise NotImplementedError()


class PNGImageOpener(ImageOpener):
    @staticmethod
    def open(filename):
        print('PNG: open with Paint')


class JPEGImageOpener(ImageOpener):
    @staticmethod
    def open(filename):
        print('JPG/JPEG: open with ImageViewer')


class SVGImageOpener(ImageOpener):
    @staticmethod
    def open(filename):
        print('SVG: open with Illustrator')


class UnknownImageOpener(ImageOpener):
    @staticmethod
    def open(filename):
        print("You don't hame program for %s extension" %filename.split('.')[-1].upper())


class Image(object):
    @classmethod
    def open_file(cls, filename):
        ext = filename.split('.')[-1]
        if ext == 'png':
            opener = PNGImageOpener
        elif ext in ('jpg', 'jpeg'):
            opener = JPEGImageOpener
        elif ext == 'svg':
            opener = SVGImageOpener
        else:
            opener = UnknownImageOpener
        bytearray = opener.open(filename)
        return cls(bytearray, filename)

    def __init__(self, byterange, filename):
        self._byterange = byterange
        self._filename = filename


Image.open_file('picture.png')
Image.open_file('picture.jpg')
Image.open_file('picture.svg')
Image.open_file('picture.raw')
