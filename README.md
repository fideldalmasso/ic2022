Crear y activar entorno de conda (o bien usar venv)
```
conda create -n ic python=3.10
conda activate ic
```
Instalar dependencias
```
pip install -r requirements.txt
```
Usar VSC para correr el notebook. Para que use el entorno de conda, es necesario cambiar el intérprete que usa VSC. Para ello desde VSC: 

```Ctrl+P > Python:Select Interpreter > Python 3.10.4 ('ic')```