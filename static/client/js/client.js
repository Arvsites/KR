function delCookies(e){
  if (e.target.tagName === 'A'){
    console.log(e.target.href);
    e.preventDefault();          
         
      /*  реализуете свою логику  */

    window.location.href = e.target.href;
  }
}
