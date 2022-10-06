let exit = document.getElementById("exit_button");
exit.addEventListener('click', delCookies, false)

function delCookies(evt) {
    alert(document.cookie);
    evt.preventDefault();
         
    document.cookie = `username=${user}; path=/; max-age=0;`;
    document.cookie = `password=${pass}; path=/; max-age=0;`;
      
    window.location.href = evt.target.href;
    }
}
