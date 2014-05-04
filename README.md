charla-celery
=============

Ficheros de ejemplo de la charla sobre Celery


Charla
------
La charla esta disponible en slideshare: [http://www.slideshare.net/albertoalcolea/celery-34264576](http://www.slideshare.net/albertoalcolea/celery-34264576)

Está dividida en dos partes:
 * Ejemplos básicos con celery (directorio (test_celery)[https://github.com/albertoalcolea/charla-celery/tree/master/test_celery])
 * Ejemplo de integracción con django (aplicación que aplica de forma asíncrona filtros a fotos)


Instalar dependencias
---------------------
 * Celery usando redis como broker

    pip install celery[redis]

 * Django

    pip install django

 * Pillow para realizar el filtro sepia

    pip install pillow

 * Flower para monitorizar el estado del broker y los workers. [Opcional]

    pip install flower


Uso
---
 * Lanzar un worker

   celery worker -A nombre_modulo --loglevel=info

 * Monitorizar estado con flower

   celery flower --broker='redis://'


Autor
-----
Alberto Alcolea ([@albertoalcolea](https://twitter.com/albertoalcolea))
[http://albertoalcolea.com](http://albertoalcolea.com)