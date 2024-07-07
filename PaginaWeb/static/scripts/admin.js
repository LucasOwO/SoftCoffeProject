function habil_aceptar(){
    if (val_nom()){
        document.getElementById("error_nombre").innerHTML = "";

        if(val_pre()){
            document.getElementById("error_precio").innerHTML = "";

            if(val_sto()){
                document.getElementById("error_stock").innerHTML = "";

                document.getElementById("btn_agregar").disabled = false;
            } else {
                document.getElementById("error_stock").innerHTML = "*";
                document.getElementById("btn_agregar").disabled = true;
            }
        } else {
            document.getElementById("error_precio").innerHTML = "*";
            document.getElementById("btn_agregar").disabled = true;
        }
    } else {
        document.getElementById("error_nombre").innerHTML = "*";
        document.getElementById("btn_agregar").disabled = true;
    }
}






/* funciones secundarias */

function validar_str_num(p1){
    let str = p1;
    str = str*1;
    
    if (isNaN(str)){
        return true;
    }
    return false;
}

function val_nom(){
    let nom = document.getElementById("txt_nombre").value;
    if(nom==""){
        return false;
    }

    if (validar_str_num(nom)){
        return true;
    } else {
        return false;
    }
}

function val_pre(){
    let pre = document.getElementById("txt_precio").value;
    if(pre==""){
        return false;
    }

    if (!validar_str_num(pre)){
        return true;
    } else {
        return false;
    }
}

function val_sto(){
    let sto = document.getElementById("txt_stock").value;
    if(sto==""){
        return false;
    }

    if (!validar_str_num(sto)){
        return true;
    } else {
        return false;
    }
}