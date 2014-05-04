from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from filtros.forms import UploadFileForm
from filtros.tasks import apply_filter
from filtros.models import Foto
from utils import fileutils


def index(request):
	context = {
		'form': UploadFileForm(),
		'fotos': Foto.objects.all(),
	}
	return render(request, 'index.html', context)


def send(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			filepath = fileutils.upload_file(request.FILES['foto'])
			foto = Foto.objects.create(titulo=form.cleaned_data['titulo'], url=filepath)
			apply_filter.delay(filepath, foto.id)
			return HttpResponseRedirect(reverse('filtros:index'))
	else:
		form = UploadFileForm()

	context = {
		'form': form,
		'fotos': Foto.objects.all(),
	}
	return render(request, 'index.html', context)
