// Support section Donation Buttons
const btns = document.querySelectorAll('.btn-donate')
const amount = document.getElementById('support-amount')

btns.forEach(btn => {

   btn.addEventListener('click', event => {
       event.preventDefault();
       if (event.target.value != 'custom') {
        amount.setAttribute('data-amount', event.target.value);
        amount.setAttribute('value', event.target.value);
       } else {
            amount.setAttribute('data-amount', "");
            amount.setAttribute('value', "");
            amount.select();
       };
       console.log( event.target.value );
   });

});