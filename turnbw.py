from PIL import Image
#
# imagen_original = Image.open('imagen_color.jpg')
# imagen_bn = imagen_original.convert('L')
# imagen_bn.save('imagen_bn.jpg')
#
# img = Image.open('imagen.jpg')
# img_bw = img.convert('1')
# img_bw.save('imagen_bn.jpg')

# img = Image.open('imagen.jpg')
# umbral = 128
# img_bw = img.point(lambda p: 0 if p < umbral else 255)
# img_bw.save('imagen_bn.jpg')


# imagen_rgb = imagen_original.convert('RGB')
#
# # Aplicar una matriz de transformación para simular un filtro de fotografía
# # Esta matriz reduce los canales de color para dar un efecto único antes de la conversión a escala de grises
# matriz_filtro = (0.3, 0.3, 0.3, 0, 0,
# 0.59, 0.59, 0.59, 0, 0,
# 0.11, 0.11, 0.11, 0, 0)
# imagen_filtrada = imagen_rgb.convert('RGB', matriz_filtro)
#
# # Convertir la imagen filtrada a escala de grises
# imagen_bn = imagen_filtrada.convert('L')
#
# # Guardar la imagen en blanco y negro
# imagen_bn.save('imagen_bn_filtrada.jpg')

import gmic

# Cargar la imagen
# img = gmic.GmicImage(filename='imagen.jpg')
#
# # Convertir a escala de grises
# gmic.run('luminance', img)
#
# # Guardar la imagen
# img.save(filename='imagen_bn.jpg')


# Cargar la imagen
# img = gmic.GmicImage(filename='imagen.jpg')
#
# # Convertir a blanco y negro
# gmic.run('bw', img)
#
# # Guardar la imagen
# img.save(filename='imagen_bn.jpg')


# img = gmic.GmicImage(filename='imagen.jpg')
#
# # Aplicar el efecto blanco y negro
# gmic.run('fx_bw', img)
#
# # Guardar la imagen
# img.save(filename='imagen_bn.jpg')


# import gmic
# import numpy as np
# from matplotlib import pyplot as plt
#
# # Inicializar G'MIC y la lista para almacenar imágenes
# gmic_instance = gmic.Gmic()
# images = []
#
# # Ejecutar un comando G'MIC para cargar una imagen y convertirla a blanco y negro
# gmic_instance.run('sp lena fx_freaky_bw 90,20,0,0,0,0', images)
#
# # Convertir la imagen G'MIC a un array de NumPy y mostrarla
# numpy_image = images[0].to_numpy_helper(interleave=True, permute='yxzc', squeeze_shape=True, astype=np.uint8)
# plt.imshow(numpy_image, cmap='gray')
# plt.show()
