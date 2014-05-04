from PIL import Image, ImageOps


def open_image(filename):
	""" grab a PIL image from the given location
	"""
	image = Image.open(filename)
	image.load()
	return image

def save_image(image, filename, quality=95):
	""" save the PIL image to disk
	"""
	image.save(filename, 'JPEG', quality=quality)

def make_linear_ramp(white):
	""" generate a palette in a format acceptable for `putpalette`, which
		expects [r,g,b,r,g,b,...]
	"""
	ramp = []
	r, g, b = white
	for i in range(255):
		ramp.extend((r*i/255, g*i/255, b*i/255))
	return ramp

def apply_sepia_filter(image):
	""" Apply a sepia-tone filter to the given PIL Image
		Based on code at: http://effbot.org/zone/pil-sepia.htm
	"""
	# make sepia ramp (tweak color as necessary)
	sepia = make_linear_ramp((255, 240, 192))

	# convert to grayscale
	orig_mode = image.mode
	if orig_mode != 'L':
		image = image.convert('L')

	# optional: apply contrast enhancement here, e.g.
	image = ImageOps.autocontrast(image)

	# apply sepia palette
	image.putpalette(sepia)

	# convert back to its original mode
	if orig_mode != 'L':
		image = image.convert(orig_mode)

	return image


def filter(in_path, out_path):
	# Mock long task
	import time
	time.sleep(7)

	image = open_image(in_path)
	save_image(apply_sepia_filter(image), out_path)
