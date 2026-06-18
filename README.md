
# 🖱️ Contador de Clics - Taller de integración continua

Este repositorio contiene una aplicación web ligera desarrollada en Flask (Python) con un enfoque principal en la implementación de prácticas de **Gestión de la Configuración del Software (SCM)** y un flujo completo de **Integración y Entrega Continua (CI/CD)**.

## 🚀 Tecnologías Utilizadas

* **Backend:** Python + Flask
* **Frontend:** HTML, JavaScript nativo (Fetch API)
* **Testing & Cobertura:** Pytest, pytest-cov
* **Análisis de Calidad (SAST):** SonarCloud
* **Integración Continua:** GitHub Actions
* **Entrega Continua (Despliegue):** Render
* **Notificaciones:** Discord Webhooks y Gmail

## ⚙️ Arquitectura del Pipeline Automático

El proyecto cuenta con un flujo automatizado que garantiza la calidad del código. Cada vez que se realiza un `push` a la rama `main`, se ejecutan las siguientes etapas:

1. **Clonado e Instalación:** GitHub Actions levanta un entorno virtual, clona el repositorio e instala las dependencias del archivo `requirements.txt`.
2. **Testing (CI):** Se ejecutan las pruebas unitarias utilizando Pytest.
3. **Cobertura y Calidad:** Se genera un archivo `coverage.xml` que es enviado automáticamente a SonarCloud. 
4. **Notificación:** El resultado de la ejecución del pipeline (éxito o fallo) se envía en tiempo real a un canal de Discord mediante un Webhook.
5. **Despliegue (CD):** Al detectar nuevos cambios en la rama principal, el servidor de Render construye y despliega la aplicación de forma automática, manteniéndola disponible en la nube.

![Herramientas utilizadas para el Entorno CI](img/ENTORNOCI.png)

## 🛠️ Ejecución en Entorno Local

Para correr este proyecto en tu propia máquina, seguí estos pasos:

1. Clonar el repositorio:
```bash
   git clone [https://github.com/belencost/contador_clics.git](https://github.com/belencost/contador_clics.git)

```

2. Moverse a la carpeta del proyecto:

```bash
   cd contador_clics

```

3. Instalar las dependencias necesarias:

```bash
   pip install -r requirements.txt

```

4. Ejecutar el servidor web:

```bash
   python src/app.py

```

5. Abrir el navegador en la dirección `http://127.0.0.1:5000`

## 🧪 Ejecución de Pruebas

```bash
pytest tests/

```

```

Realizado por María Belén Costantín 
Materia: Ingeniería y Calidad de Software
Año 2026