charla-celery
=============

Ficheros de ejemplo de la charla sobre Celery


Charla
------
La charla esta disponible en slideshare: [http://slideshare.com/albertoalcolea/celery](http://slideshare.com/albertoalcolea/celery)

Está dividida en dos partes:
 * Ejemplos básicos con celery (directorio test_celery)
 * Ejemplo de integracción con django (aplicación que aplica de forma asíncrona filtros a fotos)


Instalar dependencias
---------------------

### Celery usando redis como broker

    pip install celery[redis]

### Django

    pip install django

### Pillow para realizar el filtro sepia

    pip install pillow

### Flower para monitorizar el estado del broker y los workers. [Opcional]

    pip install flower


Autor
-----
Alberto Alcolea ([@albertoalcolea](https://twitter.com/albertoalcolea))
[http://albertoalcolea.com](http://albertoalcolea.com)