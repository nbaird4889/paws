from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dog, Visitors, Photo, Walker
from .forms import VisitorsForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.amazonaws.com/'
BUCKET = 'paws-atlanta'

# Define the home view
def home(request):
  return render(request, 'home.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', { 'dogs': dogs })

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  visitors_form = VisitorsForm()
  return render(request, 'dogs/detail.html', { 
    'dog': dog,
    'visitors_form': visitors_form
  })

def add_visitors(request, dog_id):
  form = VisitorsForm(request.POST)
  if form.is_valid():
    new_visitor = form.save(commit=False)
    new_visitor.dog_id = dog_id
    new_visitor.save()
  return redirect('detail', dog_id=dog_id)

class DogCreate(CreateView):
  model = Dog
  fields = '__all__'


class DogUpdate(UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age', 'size', 'image']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'


def add_photo(request, dog_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to dog_id or dog (if you have a dog object)
            photo = Photo(url=url, dog_id=dog_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', dog_id=dog_id)

class WalkerList(ListView):
    model = Walker

class WalkerDetail(DetailView):
    model = Walker

class WalkerCreate(CreateView):
    model = Walker
    fields = '__all__'


class WalkerUpdate(UpdateView):
  model = Walker
  fields = '__all__'

class WalkerDelete(DeleteView):
  model = Walker
  success_url = '/walkers/'