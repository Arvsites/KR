function delCookies(params) {
    let user = " ";
    let pass = " ";

    document.cookie = `username=${user}; path=/; max-age=0;`;
    document.cookie = `password=${pass}; path=/; max-age=0;`;
    window.location.href = {% url 'client:logout' %};
}
