let workingHref = document.getElementById("hidden_button");

function delCookies() {
    let user = " ";
    let pass = " ";
        
    document.cookie = `username=${user}; path=/; max-age=0;`;
    document.cookie = `password=${pass}; path=/; max-age=0;`;
      
    window.location.href = workingHref.href;
}
