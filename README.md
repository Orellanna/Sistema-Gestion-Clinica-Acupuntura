
### Sistema para la Gestion de la clínica Terapia-Holistica Acupuntura.

<p align="center">
  <img src="static/img/logo.jpg" alt="ClinicaAcupuntura" width="200" height="200">
</p>

## Cuenta con los siguientes modulos


1. ### Gestion de Pacientes
    > 📌 Permite agregar, modificar, eliminar y consultar la informacion de los Pacientes.

    > 📌 Permite ver la lista de pacientes registrados.

2. ### Gestion de Consultas
    > 📌 Permite agregar, modificar, eliminar y consultar cada consulta creada.

    > 📌 Permite consultar el historial de las consultas por paciente.


3. ### Gestion de Citas
    > 📌 Permite crear una cita para un paciente.


4. ### Gestion de Inspecciones de puntos acupunturales
    > 📌 Permite crear, editar, consultar o eliminar cada inspeccion ingresada

    > 📌 Permite ver el historial de inspecciones ingresadas por consulta.

5. ### Gestion de Pagos

    > 📌 Permite crear un pago para una consulta en especifico

    > 📌 Permite ver el historial de pagos realizados.

6. ### Gestion de Inventario
    > 📌 Permite crear, editar, consultar o eliminar los distintos suministros en Inventario

6. ### Modulo de Administracion

    ## Gestion de Usuarios
    > 📌 Permite al Admininistrador crear, editar, consultar o eliminar los distintos Usuarios que tienen acceso al sistema.


## Tecnologias Utilizadas

<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white">
<img src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white">

## 🚀 Proceso de Instalacion

Para instalar seguir los pasos:

1. Clonar el Repositorio en la carpeta donde alojaran el proyecto.

`git clone https://github.com/Orellanna/Sistema-Gestion-Clinica-Acupuntura.git`

2. Crear un entorno virtual fuera de la carpeta del proyecto:

`python -m venv env`

`env\Scripts\activate`

3. Con el entorno virtual activado instalar las librerias:

`pip install django`

`pip install psycopg2-binary`

4. Luego Realizar las migraciones:

    ubicarse en:

    .\AppClinicaAcupuntura

    y ejecutar los comandos:

`py manage.py migrate`

5. luego correr la aplicacion:

`py manage.py runserver`
