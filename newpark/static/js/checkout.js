// Stripe JS
const stripepk = Stripe('pk_test_51Ht94zJHD5anFmP1GC8ZTN5pbmVsmUbZXmtj173WVqxH788pLUpns3CSTJqhjo71PlRr9BukUs4c1fXeBw1TiSPG00DTxtJxOa');

// Create a Stripe client.
var stripe = stripepk;

// Create an instance of Elements.
var elements = stripe.elements();

// Custom styling can be passed to options when creating an Element.
// (Note that this demo uses a wider set of styles than the guide below.)
var styling = {
  base: {
    color: '#787878',
    backgroundColor: '#fafafa',
    fontFamily: '"Open Sans", sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '14px',
    '::placeholder': {
      color: '#787878'
    }
  },
  invalid: {
    color: '#fa755a',
    iconColor: '#fa755a'
  }
};

// Create an instance of the card Element.
var card = elements.create('card', { style: styling });

// Add an instance of the card Element into the `card-element` <div>.
card.mount('#card-element');

// Handle real-time validation errors from the card Element.
card.addEventListener('change', function (event) {
  var displayError = document.getElementById('card-errors');
  if (event.error) {
    displayError.classList.add('alert-error', 'alert-danger');
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
    displayError.classList.remove('alert-error', 'alert-danger');
  } 
});

// Handle form submission.
var form = document.getElementById('payment-form');
var loading = document.getElementById('loading-icon');
form.addEventListener('submit', function (event) {
  event.preventDefault();

  stripe.createToken(card).then(function (result) {
    if (result.error) {
      // Inform the user if there was an error.
      var errorElement = document.getElementById('card-errors');
      loading.classList.remove('visable'); 
      errorElement.textContent = result.error.message;
    } else {
      // Send the token to your server.
      loading.classList.add('visable'); 
      stripeTokenHandler(result.token);
    }
  });
});

// Submit the form with the token ID.
function stripeTokenHandler(token) {
  // Insert the token ID into the form so it gets submitted to the server
  var form = document.getElementById('payment-form');
  var hiddenInput = document.createElement('input');
  hiddenInput.setAttribute('type', 'hidden');
  hiddenInput.setAttribute('name', 'stripeToken');
  hiddenInput.setAttribute('value', token.id);
  form.appendChild(hiddenInput);

  // Submit the form
  form.submit();
}