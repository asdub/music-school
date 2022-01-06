window.addEventListener('keyup', (event) => { 
// Search for remote page
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    item = document.getElementsByClassName("remote-item");;
    for (i = 0; i < item.length; i++) {
        span = item[i].getElementsByTagName("span")[0];
        txtValue = span.textContent || span.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            item[i].style.opacity = "0";
            item[i].style.display = "";
            let k = i;
            let itm = item
            setTimeout(function(){
                itm[k].style.opacity = "1";
            }, 300);
        } else {
            item[i].style.opacity = "0";
            let k = i;
            let itm = item
            setTimeout(function(){
                itm[k].style.display = "none";
            }, 300);
        }
    }
});
