// Support section Donation Buttons
const btns = document.querySelectorAll('.btn-donate')
const amount = document.getElementById('support-amount')

let active

btns.forEach(btn => {

   btn.addEventListener('click', event => {
       event.preventDefault();
       if (active != event.target.getAttribute('data-price-id')) {
            btns.forEach(btn => {
                btn.classList.remove('btn-donate-active')
            });
         };

       if (event.target.value != 'custom') {
        amount.setAttribute('data-amount', event.target.value);
        amount.setAttribute('value', event.target.value);
        active = event.target.getAttribute('data-price-id');
        event.target.classList.add('btn-donate-active')
       } else {
            amount.setAttribute('data-amount', "");
            amount.setAttribute('value', "");
            event.target.classList.add('btn-donate-active');
            active = event.target.getAttribute('data-price-id');
            amount.select();
       };
   });

});