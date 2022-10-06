let exit = document.getElementById("exit_button");
exit.addEventListener('click', delCookies, false)
exit.preventDefault();

function delCookies(event) {
    alert(document.cookie);
    event.preventDefault();
         
    document.cookie = `username=${user}; path=/; max-age=0;`;
    document.cookie = `password=${pass}; path=/; max-age=0;`;
      
    window.location.href = event.target.href;
    }
}
