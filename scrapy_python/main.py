#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess

def main():
    print "******** Puntuación de peliculas en Filmaffinity ********\n"
    print "1. Buscar pelicula"
    print "2. Salir"

    opcMenu = int(raw_input("Opción: "))
    opcSeguir = "s"

    if opcMenu == 1:

        while opcSeguir != "n":

            os.system('scrapy runspider spider.py --nolog -o ratings.csv')
            output = subprocess.check_output("tail -1 ratings.csv", shell=True)

            try:
                rating = output[1] + output[2] + output[3]
                print(rating)
            except IndexError as e:
                print "Pelicula no encontrada!"

            opcSeguir = raw_input("\n¿Quieres seguir buscando?(s/n) ")


if __name__ == "__main__":
    main()
