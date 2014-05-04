import datetime

def upload_file(f):
	filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	filepath = 'media/fotos/{0}'.format(filename)
	with open(filepath, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
	return filepath
