let username = document.getElementById('user');
let password = document.getElementById('pass');

function setCookies(params) {
    alert("works");
    let user = username.value;
    let pass = password.value;

    document.cookie = `username=${user}; path=/; `;
    document.cookie = `password=${pass}; path=/; `;
}
