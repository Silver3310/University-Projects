from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings
import os
from io import BytesIO
from PIL import Image
import re
import base64
import glob
import errno
import operator


class MainPage(TemplateView):
    """The main page for the application with a form to draw"""

    template_name = 'letter_recognition/main.html'


class RecognizeLetter(TemplateView):
    """Recognize an image by downloading it and comparing to others"""

    template_name = 'letter_recognition/main.html'

    def get(self, request):

        # Here we download the canvas image
        image_data = request.GET['image_data']
        image_width = int(request.GET['width'])
        image_height = int(request.GET['height'])
        image_data = re.sub("^data:image/png;base64,", "", image_data)
        image_data = base64.b64decode(image_data)
        image_data = BytesIO(image_data)
        im = Image.open(image_data)
        assert (image_width, image_height,) == im.size

        # unite two strings
        path = os.path.join(settings.STATICFILES_DIRS[0], 'img/patterns/*.png')
        # make paths for all png elements
        files = glob.glob(path)
        # a dict for our patterns
        images = dict()
        for name in files:
            try:
                # [:-4] is used to remove the file'sextension
                # .load() method returns a matrix of pixels
                images[os.path.basename(name)[:-4]] = Image.open(name).load()
            except IOError as exc:
                if exc.errno != errno.EISDIR:
                    raise

        # load the pixel values
        pix = im.load()

        # the dict of sums
        s = dict()

        for fname, fpix in images.items():
            s[fname] = 0
            for i in range(image_width):
                for j in range(image_height):
                    # pixels are represented in rgba format,
                    # so if the 2nd color is blue for both images, then
                    # they have the same pixels
                    if pix[i, j][2] > 0 and fpix[i, j][2] > 0:
                        s[fname] += 1

        # here we send the letter with a max value
        ctx = {
            "response": max(s.items(), key=operator.itemgetter(1))[0]
        }

        return render(
            request,
            self.template_name,
            ctx
        )
