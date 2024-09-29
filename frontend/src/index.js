import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import App from './App';
import './styles/main.css'; // Importing global styles
import { loadStripe } from '@stripe/stripe-js';
import { Elements } from '@stripe/react-stripe-js';

// Load your publishable key from Stripe
const stripePromise = loadStripe(process.env.REACT_APP_STRIPE_PUBLISHABLE_KEY);

// Rendering the App component wrapped in Router and Elements for Stripe
ReactDOM.render(
  <Router>
    <Elements stripe={stripePromise}>
      <App />
    </Elements>
  </Router>,
  document.getElementById('root')
);