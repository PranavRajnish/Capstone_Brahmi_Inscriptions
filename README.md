# Brief

A research-oriented project to Improve the Readability of Brahmi Stone Inscriptions. This includes inscriptions present in rock, estampages, documents, and handwritten manuscripts.
The Brahmi script is an ancient script that is a precursor to many South Asian scripts and languages.
The goal of the project is to help researchers, students, and epigraphers easily study and store ancient Brahmi inscriptions. This would facilitate the preservation of an ancient culture.
Consists of an end-to-end model for pre-processing, denoising, segmentation, and optical character recognition. 

# Techniques and Methodologies

### Pre-processing and Denoising
We use a Connected Components algorithm along with Otsu's threshold to get rid of any unwanted noise present in the image and to binarize it.

### Segmentation 
We use contouring for the line segmentation and histogram-based methods, along with some additional modifications like thinning of characters, for the character segmentation module.

### Optical Character Recognition
We use the InceptionResetv2 architecture for our OCR model to recognize the multitude of different Brahmi characters. We also use skeletonization and pruning as pre-processing when testing to standardize the characters and better match our dataset.

### Dataset
A dataset of 60,000 handwritten Brahmi characters, about 200 of each character, was provided by our gracious guide.

### Application
Web application built using the Django framework. Users can input a Brahmi document and the model will try to segment and recognize it.

### Technologies and Libraries Used
Python
OpenCV
TensorFlow
Keras
Numpy
Pillow
Matplotlib
Google Colab
 
