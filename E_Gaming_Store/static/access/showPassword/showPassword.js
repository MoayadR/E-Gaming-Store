const showPassword = document.querySelector('#check');
const passwordInput = document.querySelector('#password');

showPassword.addEventListener('click' , ()=> {
    if (showPassword.checked)
    {
        passwordInput.type = "text";
    }
    else
    {
        passwordInput.type = "password";
    }
});

