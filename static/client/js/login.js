let username = document.getElementById('user');
let password = document.getElementById('pass');
alert("works");

function setCookies(params) {
    let user = username.value;
    let pass = password.value;

    document.cookie = `username=${user}; path=/; `;
    document.cookie = `password=${pass}; path=/; `;
}
