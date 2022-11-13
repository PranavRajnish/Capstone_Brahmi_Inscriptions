from importlib.metadata import requires
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.conf import settings
import os
import cv2
from .pipeline import run_pipeline, load_model_60
from .forms import ImageInfoForm
from .models import ImageInfo
import shutil
import zipfile
from io import BytesIO
from django.core.files.storage import default_storage
current_image_name = ""
# Create your views here.

def make_archive(source, destination):
        base = os.path.basename(destination)
        name = base.split('.')[0]
        format = base.split('.')[1]
        archive_from = os.path.dirname(source)
        archive_to = os.path.basename(source.strip(os.sep))
        print(source, destination, archive_from, archive_to)
        shutil.make_archive(name, format, archive_from, archive_to)
        shutil.move('%s.%s'%(name,format), destination)

def get_all_file_paths(directory):
  
    # initializing empty file paths list
    file_paths = []
  
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    # returning all file paths
    return file_paths  

def index(request):

    global current_image_name
    if request.method == 'POST':
        print('------------------------------------------------')
        print("Post Request!")
        image_form = ImageInfoForm(request.POST, request.FILES)

        if image_form.is_valid():
            image_name_new = image_form.cleaned_data.get("image_name")
            image_new = image_form.cleaned_data.get("image")
            obj = ImageInfo.objects.create(image_name = image_name_new, image= image_new)
            obj.save()

            current_image_name = image_name_new

            intial_path = obj.image.path
            dir_path = 'C:\\MyStuff\\PES\\Capstone_Application\\capstone_application\\media\\images\\' + image_name_new
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            new_path = dir_path + '\\original.jpg'
            os.rename(intial_path, new_path)

            #obj.image.save(os.path.join(settings.MEDIA_ROOT, "images", image_name_new, "original.jpg"), image_new)
            model_60 = settings.MODEL_60
            if model_60 == None:
                print("NULL MODEL!!")
                image_form = ImageInfoForm()
                return render(request, 'basic_app/home.html', {'form':image_form})

            run_pipeline(new_path, dir_path, model_60)
            obj.image = 'images/'+image_name_new+'/original.jpg'
            obj.cc_image = 'images/'+image_name_new+'/cc.jpg'
            obj.save()

            #result_path = os.path.join(settings.MEDIA_ROOT, 'results', image_name_new + "_results")
            #result_path = settings.MEDIA_ROOT / 'results' / (image_name_new + "_results")
            result_path = 'C:\\MyStuff\\PES\\Capstone_Application\\capstone_application\\media\\image_results\\' + image_name_new +"_results"
            
            file_paths = get_all_file_paths(dir_path)
            print('Following files will be zipped:')
            for file in file_paths:
                    print(file)
            
            s = BytesIO()

            # The zip compressor
            zf = zipfile.ZipFile(s, "w")

            for fpath in file_paths:
                # Calculate path for file in zip
                fdir, fname = os.path.split(fpath)
                zip_path = os.path.join(fname)

                # Add file, at correct path
                zf.write(fpath, zip_path)

            # Must close zip for all contents to be written
            zf.close()

            resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
            # ..and correct content-disposition
            resp['Content-Disposition'] = 'attachment; filename=%s' % image_name_new


            #s.seek(0)
            # To store it we can use a InMemoryUploadedFile
            #inMemory = InMemoryUploadedFile(s, None, "my_zip_%s" % image_name_new, 'tmp/'+image_name_new, s.len, None)
            
            with default_storage.open('tmp/'+image_name_new + '.zip', 'wb') as destination:
                print(type(destination))
                destination.write(s.getbuffer())

            s.close()
            '''
            resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
            # ..and correct content-disposition
            resp['Content-Disposition'] = 'attachment; filename=%s' % image_name_new
            '''
            #obj.update_result('C:\\MyStuff\\PES\\Capstone_Application\\capstone_application\\media\\tmp\\' + image_name_new +'.zip')
            obj.result = 'tmp/' + image_name_new + '.zip'
            obj.save()
            return HttpResponseRedirect(reverse('basic_app:results'))
            

        #print('------------------------------------------------')
            

    else: 
        image_form = ImageInfoForm()
        return render(request, 'basic_app/home.html', {'form':image_form})

def results(request):

    global current_image_name
    print("current image: " + current_image_name)
    context_dict = {}
    imageInfo = ImageInfo.objects.filter(image_name=current_image_name)
    context_dict['image_infos'] = imageInfo

    #print("in view")
    #print(imageInfo.image_name)
    #print(imageInfo.image.url)
    #print('-----------------------')
    return render(request, 'basic_app/results.html', context=context_dict)

def info(request):
    return render(request, 'basic_app/info.html')

def about(request):
    return render(request, 'basic_app/about.html')
