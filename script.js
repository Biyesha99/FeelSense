// script.js

// Get references to HTML elements
const form = document.querySelector('form');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const messageInput = document.getElementById('message');

// Event listener for form submission
form.addEventListener('submit', (e) => {
    e.preventDefault(); // Prevent the default form submission

    // Get input values
    const name = nameInput.value;
    const email = emailInput.value;
    const message = messageInput.value;

    // Do something with the data (e.g., send it to the backend)

    // Show an alert to indicate successful submission
    alert('Message submitted successfully!');

    // Clear the form fields
    nameInput.value = '';
    emailInput.value = '';
    messageInput.value = '';
});