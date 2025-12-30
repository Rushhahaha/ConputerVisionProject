#Requirements
- python 3.6
- tensorflow 1.13.1
- PIL, numpy, scipy
- tqdm

#Training 
1) Download Places365 to use it as a content dataset: [Places365-Standard high-res train mages (105GB)](http://data.csail.mit.edu/places/places365/train_large_places365standard.tar).  
2) Download a couple of artists images from Google
We recommend taking first collection of Cezanne and Van Gogh images. 
Place them in folders `./data/art_images/cezanne_vangogh/cezanne` and 
`./data/art_images/cezanne_vangogh/vangogh` respectively.
3) To start training run in terminal `bash launch_multistep_training.sh`. 


