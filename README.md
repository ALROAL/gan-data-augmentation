# Generative modelling for data augmentation
The limited amount of data in the medical domain and the necessity of training samples for increased performance of deep learning models is a recurrent challenge. Newborn Solutions seeks to accelerate the validation of their non-invasive white blood cells counting medical device Neosonics with synthetic in vitro images acquisition, being their next move the digitization of the image generation process.

This work presents the design, implementation and evaluation of a continuous scalar conditional Generative Adversarial Network to perform a GAN-based data augmentation for an image regression model on in vitro meningitis and in vitro peritoneal dialysis ultrasound images. The proposed GAN architecture and training scheme is capable of dealing with the images specific resolution and continuous scalar conditioning. General GAN design guidelines were followed, but novel design choices were also introduced: 1) using a combination of varying kernel sizes along the transposed convolutional layers in the generator to achieve the desired image resolution and 2) projecting both the input noise and condition values to a disentangled intermediate latent space.

The experiments and evaluation showed that the continuous scalar conditional Generative Adversarial Network is capable of generating good visual quality and diverse images containing features with high resemblance to real ones. However, the image regression task proved to be challenging and the image regressor performance could not be improved consistently by means of a GAN-based data augmentation approach.

<p align="center">
<img src="https://i.imgur.com/BeJ7cw5.png" align="center">
</p>
