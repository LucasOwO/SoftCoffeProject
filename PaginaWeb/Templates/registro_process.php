<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "mi_base_de_datos";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Obtener datos del formulario
$nombre = $_POST['nombre'];
$apellido = $_POST['apellido'];
$sexo = $_POST['sexo'];
$fecha_nacimiento = $_POST['fecha_nacimiento'];
$email = $_POST['email'];
$password = password_hash($_POST['password'], PASSWORD_DEFAULT);

// Insertar datos en la base de datos
$sql = "INSERT INTO usuarios (nombre, apellido, sexo, fecha_nacimiento, email, password) VALUES ('$nombre', '$apellido', '$sexo', '$fecha_nacimiento', '$email', '$password')";

if ($conn->query($sql) === TRUE) {
    echo "Registro exitoso";
    header("Location: login.html");
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
