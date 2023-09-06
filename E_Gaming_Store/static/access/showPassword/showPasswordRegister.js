const showPassword = document.querySelector('#check');
const passwordInput1 = document.querySelector('#id_password1');
const passwordInput2 = document.querySelector('#id_password2');

showPassword.addEventListener('click' , ()=> {
    if (showPassword.checked)
    {
        passwordInput1.type = "text";
        passwordInput2.type = "text";
    }
    else
    {
        passwordInput1.type = "password";
        passwordInput2.type = "password";
    }
});

