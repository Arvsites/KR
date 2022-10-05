function delCookies(params) {
    let user = "";
    let pass = "";

    document.cookie = `username=${user}; path=/; `;
    document.cookie = `password=${pass}; path=/; `;
}