from django.shortcuts import render
from .forms import ImageUploadForm
from .services import classificate


def main_view(request):
	info = ""
	classification_result = None
	if request.method == "POST":
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save()
			obj.result = classificate(obj.image)
			obj.save()
			classification_result = obj
		else:
			info = form.errors
	return render(request, "main.html", {"form": ImageUploadForm(), "info": info, "classification_result": classification_result})