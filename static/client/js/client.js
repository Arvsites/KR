let workingHref = document.getElementById("hidden_button");
console.log("works")

function delCookies() {
    alert(workingHref.href);
         
    document.cookie = `username=${user}; path=/; max-age=0;`;
    document.cookie = `password=${pass}; path=/; max-age=0;`;
      
    //window.location.href = event.target.href;
}
