import colorama, rich, os, msvcrt, random, time
from colorama import Fore, Style; from os import system; from rich import print
code = open('code.txt', 'rw')
name = open('name.txt', 'rw')
rut  = open('rut.txt', 'rw')
propuesta = open('propuesta.txt', 'rw')
rutUser = ""
dvRut = ""
nameUser = ""
password = ""
def registro():
  rutUser = input("Ingrese su rut (sin dígito verificador).\n- ")
  dvRut = input("Ingrese su sin dígito verificador.\n- ")
  nameUser = input("Ingrese su nombre.\n- ")
  password = input("Ingrese una contraseña.\n- ")
  def userCheck():
    for line in rut:
      if rutUser == line:
        print("[red]El rut ya existe. Intnte iniciar sesión.[/red]")
def iniciarSesion():
  rutUser = input("Ingrese su rut (sin dígito verificador).\n- ")
  dvRut = input("Ingrese su sin dígito verificador.\n- ")
  password = input("Ingrese una contraseña.\n- ")