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
















































//Funcionalidades Carrito
const btnCart = document.querySelector('.container-cart-icon');
const containerCartProducts = document.querySelector('.container-cart-products');

btnCart.addEventListener('click', () => {
    containerCartProducts.classList.toggle('hidden-cart');
});

const cartInfo = document.querySelector('.cart-product');
const rowProduct = document.querySelector('.row-product');

const productsList = document.querySelector('.container-items');

let allProducts = [];

const valorTotal = document.querySelector('.total-pagar');
const countProducts = document.querySelector('#contador-productos');
const cartEmpty = document.querySelector('.cart-empty');
const cartTotal = document.querySelector('.cart-total');

productsList.addEventListener('click', e => {
    if (e.target.classList.contains('btn-add-cart')) {
        const product = e.target.parentElement;

        const infoProduct = {
            quantity: 1,
            title: product.querySelector('h2').textContent,
            price: product.querySelector('p').textContent,
        };

        const exits = allProducts.some(
            product => product.title === infoProduct.title
        );

        if (exits) {
            const products = allProducts.map(product => {
                if (product.title === infoProduct.title) {
                    product.quantity++;
                    return product;
                } else {
                    return product;
                }
            });
            allProducts = [...products];
        } else {
            allProducts = [...allProducts, infoProduct];
        }

        showHTML();
    }
});

rowProduct.addEventListener('click', e => {
    if (e.target.classList.contains('icon-close')) {
        const product = e.target.parentElement;
        const title = product.querySelector('p').textContent;

        allProducts = allProducts.filter(
            product => product.title !== title
        );

        showHTML();
    }
});

rowProduct.addEventListener('click', e => {
    if (e.target.classList.contains('icon-add')) {
        const product = e.target.parentElement.parentElement;
        const title = product.querySelector('.titulo-producto-carrito').textContent;

        allProducts.forEach(item => {
            if (item.title === title) {
                item.quantity++;
            }
        });

        showHTML();
    }
});

rowProduct.addEventListener('click', e => {
    if (e.target.classList.contains('icon-remove')) {
        const product = e.target.parentElement.parentElement;
        const title = product.querySelector('.titulo-producto-carrito').textContent;

        allProducts.forEach(item => {
            if (item.title === title && item.quantity > 1) {
                item.quantity--;
            } else if (item.title === title && item.quantity === 1) {
                allProducts = allProducts.filter(
                    product => product.title !== title
                );
            }
        });

        showHTML();
    }
});


const showHTML = () => {
    if (!allProducts.length) {
        cartEmpty.classList.remove('hidden');
        rowProduct.classList.add('hidden');
        cartTotal.classList.add('hidden');
    } else {
        cartEmpty.classList.add('hidden');
        rowProduct.classList.remove('hidden');
        cartTotal.classList.remove('hidden');
    }

    rowProduct.innerHTML = '';

    let total = 0;
    let totalOfProducts = 0;

    allProducts.forEach(product => {
        const containerProduct = document.createElement('div');
        containerProduct.classList.add('cart-product');

        containerProduct.innerHTML = `
            <div class="info-cart-product">
                <button class="icon-remove">-</button>
                <span class="cantidad-producto-carrito">${product.quantity}</span>
                <button class="icon-add">+</button>
                <p class="titulo-producto-carrito">${product.title}</p>
                <span class="precio-producto-carrito">${product.price}</span>
            </div>
        `;

        rowProduct.append(containerProduct);

        total += parseInt(product.quantity) * parseInt(product.price.slice(1));
        totalOfProducts += product.quantity;
    });

    valorTotal.innerText = `$${total}`;
    countProducts.innerText = totalOfProducts;
};

const pagarButton = document.createElement('button');
pagarButton.innerText = 'Pagar';
pagarButton.classList.add('btn', 'btn-pagar');
pagarButton.addEventListener('click', function() {
    window.location.href = 'Pago';
});
containerCartProducts.appendChild(pagarButton);


















