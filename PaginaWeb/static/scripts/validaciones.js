$(document).ready(function() {
    $('#registrationForm').submit(function(event) {
        // Prevenir el envío del formulario por defecto
        event.preventDefault();

        // Limpiar mensajes de error anteriores
        $('.error-message').hide();

        // Verificar los campos del formulario
        var nombre = $('#nombre').val();
        var apellido = $('#apellido').val();
        var sexo = $('#sexo').val();
        var fecha_nacimiento = $('#fecha_nacimiento').val();
        var email = $('#email').val();
        var password = $('#password').val();
        var confirm_password = $('#confirm_password').val();

        // Validar nombre
        if (nombre === '') {
            $('#nombreError').text('Ingrese su nombre').show();
        } else {
            $('#nombreError').hide();
        }

        // Validar apellido
        if (apellido === '') {
            $('#apellidoError').text('Ingrese su apellido').show();
        } else {
            $('#apellidoError').hide();
        }

        // Validar sexo
        if (sexo === '') {
            $('#sexoError').text('Seleccione su sexo').show();
        } else {
            $('#sexoError').hide();
        }

        // Validar fecha de nacimiento
        if (fecha_nacimiento === '') {
            $('#fechaNacimientoError').text('Ingrese su fecha de nacimiento').show();
        } else {
            $('#fechaNacimientoError').hide();
        }

        // Validar correo electrónico
        if (email === '') {
            $('#emailError').text('Ingrese su correo electrónico').show();
        } else {
            $('#emailError').hide();
        }

        // Validar contraseña
        if (password === '') {
            $('#passwordError').text('Ingrese su contraseña').show();
        } else {
            $('#passwordError').hide();
        }

        // Validar confirmación de contraseña
        if (confirm_password === '') {
            $('#confirmPasswordError').text('Confirme su contraseña').show();
        } else {
            $('#confirmPasswordError').hide();
        }

        // Validar que las contraseñas coincidan
        if (password !== confirm_password) {
            $('#confirmPasswordError').text('Las contraseñas no coinciden').show();
        } else {
            $('#confirmPasswordError').hide();
        }

        // Verificar si todos los campos están vacíos
        if (nombre === '' && apellido === '' && sexo === '' && fecha_nacimiento === '' && email === '' && password === '' && confirm_password === '') {
            $('#error-message').text('Por favor, completa todos los campos').show();
        } else {
            $('#error-message').hide();
        }
    });
});


$(document).ready(function() {
    $('#loginForm').submit(function(event) {
        // Prevenir el envío del formulario por defecto
        event.preventDefault();

        // Limpiar mensajes de error anteriores
        $('.error-message').hide();

        // Verificar los campos del formulario
        var email = $('#login_email').val();
        var password = $('#login_password').val();

        // Validar correo electrónico
        if (email === '') {
            $('#loginEmailError').text('Ingrese su correo electrónico').show();
        }

        // Validar contraseña
        if (password === '') {
            $('#loginPasswordError').text('Ingrese su contraseña').show();
        }

        // Agregar otras validaciones según sea necesario

        // Si todas las validaciones pasan, enviar el formulario
        if (email !== '' && password !== '') {
            this.submit();
        }
    });
});
