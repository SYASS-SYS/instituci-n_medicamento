API DE FARMACIA INSTITUCIONAL - FASTAPI

REQUISITOS
- Python instalado.
- Una base de datos PostgreSQL (por ejemplo, Neon).
- Visual Studio Code (opcional, recomendado).

1. ABRIR EL PROYECTO
Descomprime la carpeta y ábrela en Visual Studio Code.

2. CREAR EL ENTORNO VIRTUAL
Abre la terminal en la carpeta del proyecto y ejecuta:

    python -m venv venv

3. ACTIVAR EL ENTORNO VIRTUAL (Windows PowerShell)

    .\venv\Scripts\Activate.ps1

Si PowerShell bloquea la ejecución de scripts, ejecuta este comando:

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Luego vuelve a activar:

    .\venv\Scripts\Activate.ps1

4. INSTALAR DEPENDENCIAS

    pip install -r requirements.txt

5. CONFIGURAR LA BASE DE DATOS
- Renombra .env.example a .env.
- Abre .env y reemplaza el valor de DATABASE_URL por tu URL real de PostgreSQL/Neon.
- No compartas tu contraseña ni subas el archivo .env a internet.

6. INICIAR LA API

    uvicorn main:app --reload

7. PROBAR LA API
Abre en el navegador:

    http://127.0.0.1:8000/docs

Desde Swagger puedes probar:
- POST /medicamentos: registrar medicamento.
- GET /medicamentos: consultar todos.
- GET /medicamentos/categoria/{categoria}: filtrar por categoría.
- GET /medicamentos/{medicamento_id}: consultar por ID.
- PUT /medicamentos/{medicamento_id}: actualizar.
- DELETE /medicamentos/{medicamento_id}: eliminar.

IMPORTANTE
La ruta de categoría está declarada antes de la ruta por ID para evitar que
FastAPI interprete la palabra "categoria" como si fuera un ID.
