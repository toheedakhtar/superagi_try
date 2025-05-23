document.addEventListener("DOMContentLoaded", function() {
    const demoButton = document.querySelector('a[href="/api/request-demo"]');
    const serviceButton = document.querySelector('a[href="/api/request-service"]');

    demoButton.addEventListener('click', function(e) {
        e.preventDefault();
        // Implement functionality for demo request
        alert("Demo request initiated!");
    });

    serviceButton.addEventListener('click', function(e) {
        e.preventDefault();
        // Implement functionality for service request
        alert("Service request initiated!");
    });
});