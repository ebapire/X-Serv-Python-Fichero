#!/usr/bin/python
# -*- coding: utf-8 -*-


fich = open("/etc/passwd", "r")
lista_usuarios = fich.readlines()
for linea in lista_usuarios:
    lista = linea.split(':')
    print lista[0], lista[-1],

print "la lista tiene ", len(lista_usuarios), "usuarios"

fich.close
