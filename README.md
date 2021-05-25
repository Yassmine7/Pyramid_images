# pyramid_images
Les pyramides d'images sont très utiles pour l'affichage des jeux de données raster et elles optimisent la réalisation de plusieurs processus tels que la corrélation d'images. En effet, il existe deux types de pyramides ; les pyramides gaussiennes et les pyramides laplaciennes.
Vous trouverez ci-joint les scripts utilisés pour :
-Créer une pyramide gaussiènne : gaussien_pyramid.py
-Créer une pyramide laplacienne pour une image de dimensions nxn : laplacien_pyramid_image_size_nxn
-Créer une pyramide gaussienne pour une image de dimensions nxm : laplacien_pyramid_image_size_nxm
vous trouverez aussi des images que vous pouvez tester, sinon vous pouvez utiliser vos propres images.
La pyramide de gauss est le résultat d’une convolution du niveau inférieur par un noyau gaussien. Dans les pyramides de Gauss, les images résultats sont modifiées en utilisant une moyenne de Gauss (flou Gaussien) ou bien convolution puis réduites. Chaque pixel contenant une moyenne locale qui correspond à un pixel voisin d'un niveau plus bas de la pyramide. Cette technique est utilisée surtout dans la synthèse de texture.
Les pyramides de Laplace sont très similaires aux pyramides de Gauss, mais sont calculées en sauvegardant la différence avec l'image floutée entre chaque niveau. Seul le plus petit niveau n'est pas une différence pour pouvoir reconstruire l'image en haute résolution utilisant les différences entre chaque niveau. Cette technique peut être utilisée en compression d'image.
