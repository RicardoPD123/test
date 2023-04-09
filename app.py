from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)
@app.route('/invitacion', methods=['POST'])
def registrar_invitacion():
    # Obtener los datos enviados desde el formulario
    nombre = request.form['nombre']
    correo = request.form['correo']
    telefono = request.form['telefono']
    cantidad = request.form['cantidad']
    mensaje = request.form['mensaje']
    
    # Conectar a la base de datos
    conexion = sqlite3.connect('baby_shower.sqlite')
    cursor = conexion.cursor()
    
    # Insertar los datos de la invitación en la tabla "invitaciones"
    cursor.execute('INSERT INTO invitaciones (nombre, correo, telefono, cantidad, mensaje) VALUES (?, ?, ?, ?, ?)', (nombre, correo, telefono, cantidad, mensaje))
    conexion.commit()
    
    # Cerrar la conexión a la base de datos
    conexion.close()
    
    # Responder con un mensaje de éxito en formato JSON
    return jsonify({'mensaje': 'Invitación registrada correctamente'})
if __name__ == '__main__':
    app.run(debug=True)
