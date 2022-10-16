let username = document.getElementById('user');
let password = document.getElementById('pass');
let button = document.getElementById('post_button');

function setCookies() {
    let user = username.value;
    let pass = password.value;

    document.cookie = `username=${user}; path=/; `;
    document.cookie = `password=${pass}; path=/; `;
}

function getCookie(name) {
    let dc = document.cookie;
    let prefix = name + "=";
    let begin = dc.indexOf("; " + prefix);
    if (begin == -1) {
        begin = dc.indexOf(prefix);
        if (begin != 0) return null;
    }
    else
    {
        begin += 2;
        var end = document.cookie.indexOf(";", begin);
        if (end == -1) {
        end = dc.length;
        }
    }
    return decodeURI(dc.substring(begin + prefix.length, end));
} 

if (getCookie("username") !== "" && getCookie("password") !== "") {
    
    username.value = (getCookie("username").split(";")[0]);
    password.value = (getCookie("password").split(";")[0]);
    button.click();

}
