from datetime import datetime, date
from doctest import REPORTING_FLAGS
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, send_file, send_from_directory
from .models.entities.User import User
from .models.entities.Equipo import Equipo
from .models.entities.PruebaEquipo import PruebaEquipo
from .models.ModelUser import ModelUser
from .models.ModelEquipo import ModelEquipo
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from emqu import db1, root_pathApp
import json
import requests
import os
import pandas as pd
import xlrd

import matplotlib.pyplot as plt
from io import BytesIO
import base64

import ping3

bp = Blueprint('system', __name__, url_prefix='/system')

fecha_hoy = datetime.today()

carpeta_proyecto = "C:\\backups_wewire_system\\backups_wewire_system\\"    

@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'],1) #el fullname no lo indico porque por defecto esta vacio
        logged_user = ModelUser.login(db1, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                datos = {
                    'opcion_seleccionada' : "",
                }
                return render_template('index.html',datos=datos)
            else:
                flash("Password inválido...")
                return render_template('equipos/login.html')
        else:
            flash("Usuario no encontrado...")
            return render_template('equipos/login.html')
    else:
        return render_template('equipos/login.html')

# SECCION DE EQUIPOS
@bp.route('/crudEquipos', methods=['get','post'])
@login_required
def crudEquipos():
    data_equipos = ModelEquipo.get_all(db1)
    datos = {
        'titulo':'Gestión de Equipos',
        'hoy':fecha_hoy,
        'equipos':data_equipos,
        'equipo':None
    }
    return render_template('equipos/crud_equipos.html', datos=datos)

@bp.route('/registroEquipos', methods=['GET','POST'])
@bp.route('/editarEquipo/registroEquipos', methods=['GET','POST'])
@login_required
def registroEquipos():
    #equipo = request.form['nombreEquipo']
    #data = {"descripcion_proceso_produccion":equipo}
    if request.form['tipoOperacion'] == "0":
        equipo = Equipo('NULL', request.form['nombreEquipo'], request.form['ipv4'])
        ModelEquipo.insertEquipo(db1, equipo)
        flash("Registro guardado correctamente.")
        return redirect(url_for('system.crudEquipos'))
    else:
        equipo = Equipo(request.form['idEquipo'], request.form['nombreEquipo'], request.form['ipv4'])
        ModelEquipo.updateEquipo(db1, equipo)
        flash("Registro actualizado correctamente.")
        return redirect(url_for('system.crudEquipos'))

@bp.route('/eliminaEquipo/<idEquipo>', methods=['GET'])
@login_required
def eliminaEquipo(idEquipo):
    try:
        ModelEquipo.deleteEquipo(db1, idEquipo)
        flash("Equipo eliminado exitosamente...")
    except Exception as e:
        print(e)
        flash("Error al borrar el equipo, existen pruebas con este equipo...")

    return redirect(url_for('system.crudEquipos'))

@bp.route('/editarEquipo/<idEquipo>', methods=['GET'])
@login_required
def editarEquipo(idEquipo):
    equipo = ModelEquipo.get_by_id(db1, idEquipo)
    if equipo is not None:
        data_equipos = ModelEquipo.get_all(db1)
        datos = {
            'titulo':'Configuración de Equipos',
            'hoy':fecha_hoy,
            'equipos':data_equipos,
            'equipo':equipo
        }
        return render_template('equipos/crud_equipos.html', datos=datos)
    else:
        return redirect(url_for('system.crudEquipos'))
# SECCION DE EQUIPOS

# SECCION DE PRUEBAS
# Entrada.- Lista de tuplas con los equipos dados de alta
# retorno.- Lista de objetos a insertar
def ping_general(hosts):
    pruebasEquipos = []
    try:
        for host in hosts:
            if host is not None:
                idEquipo = host[0]
                ip = host[2]
                latency = ping3.ping(ip)
                pruebasEquipos.append((idEquipo,str(latency)))
    except Exception as e:
        print(f"Error {str(e)}")
    return pruebasEquipos

# Entrada.- ip del equipo a evaluar
# retorno.- resuktado de la evaluacion
def ping_host(host):
    try:
        latency = ping3.ping(host)
        return latency
    except Exception as e:
        print(f"Error {str(e)}")
        return None

#ping_host("8.8.8.8")
#ping_host("18.8.8.8")

@bp.route('/pruebaLatenciaIndividual/<idEquipo>', methods=['GET'])
@login_required
def pruebaLatenciaIndividual(idEquipo):
    data_equipos = ModelEquipo.get_all(db1)
    equipo = ModelEquipo.get_by_id(db1, idEquipo)
    pruebas_exitosas = 0
    pruebas_fallidas = 0
    if equipo is not None:
        if ping_host(equipo[2]) == None:
            pruebas_fallidas += 1
        else:
            pruebas_exitosas += 1
    datos = {
        'titulo':'Ejecución y Estadísticas',
        'hoy':fecha_hoy,
        'equipos':data_equipos,
        'equipo':None,
        'total_equipos_evaluados':1,
        'pruebas_exitosas':pruebas_exitosas,
        'pruebas_fallidas':pruebas_fallidas,
        'mensajePrueba':'Prueba de latencia del Equipo: ' + equipo[1] + ", IP: " + equipo[2]
    }
    data_equipos = ModelEquipo.get_all(db1)
    return render_template('ejecucion_estadisticas/equipos_estadisticos.html', datos=datos)

@bp.route('/pruebaGeneral')
@login_required
def pruebaGeneral():
    data_equipos = ModelEquipo.get_all(db1)
    pruebas = ping_general(data_equipos)
    pruebas_exitosas = 0
    pruebas_fallidas = 0
    for prueba in pruebas:
        if prueba[1] == 'None':
            pruebas_fallidas += 1
        else:
            pruebas_exitosas += 1

    # Guarda en BD
    if len(pruebas) > 0:
        ModelEquipo.insertPruebas(db1, pruebas)
    data_equipos = ModelEquipo.get_all(db1)
    datos = {
        'titulo':'Ejecución y Estadísticas',
        'hoy':fecha_hoy,
        'equipos':data_equipos,
        'equipo':None,
        'total_equipos_evaluados':len(data_equipos),
        'pruebas_exitosas':pruebas_exitosas,
        'pruebas_fallidas':pruebas_fallidas,
        'mensajePrueba':'Prueba general de latencia'
    }
    return render_template('ejecucion_estadisticas/equipos_estadisticos.html', datos=datos)


@bp.route('/servicios')
@login_required
def servicios():
    data_equipos = ModelEquipo.get_all(db1)
    data_pruebas = ModelEquipo.get_allPruebas(db1)
    print(data_pruebas)
    pruebas_exitosas = 0
    pruebas_fallidas = 0
    for prueba in data_pruebas:
        if prueba[2] == 'None':
            pruebas_fallidas += 1
        else:
            pruebas_exitosas += 1
    datos = {
        'titulo':'Ejecución y Estadísticas',
        'hoy':fecha_hoy,
        'equipos':data_equipos,
        'equipo':None,
        'total_equipos_evaluados':len(data_pruebas),
        'pruebas_exitosas':pruebas_exitosas,
        'pruebas_fallidas':pruebas_fallidas,
        'mensajePrueba':'Resultados de todas las pruebas de latencia'
    }
    return render_template('ejecucion_estadisticas/equipos_estadisticos.html', datos=datos)
# FIN SECCION DE PRUEBAS

@bp.route('/logout')
def logout():
    logout_user()
    datos = {
        'titulo':'Panel de Asistencias',
    }    
    return render_template('equipos/login.html', datos=datos)
