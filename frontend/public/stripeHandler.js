// Create an instance of Stripe
var stripe = Stripe('pk_test_51Q0q6400WnorE2VjJPCCK4CqM9K5HPrxZizWBXXuAvOB9PFwE9gmdZU94otE3JhKwFP9EBJU80cRYYeDbd6MQ2nF009HD9Fxoo');

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

document.getElementById('checkoutButton').addEventListener('click', function () {
    fetch(`${API_URL}/create-checkout-session`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            product_name: 'Sample Product',
            amount: 5000,
            quantity: 1,
        }),
    })
    .then(function (response) {
        return response.json();
    })
    .then(function (session) {
        return stripe.redirectToCheckout({ sessionId: session.id });
    })
    .then(function (result) {
        if (result.error) {
            alert(result.error.message);
        }
    })
    .catch(function (error) {
        console.error('Error:', error);
    });
});
