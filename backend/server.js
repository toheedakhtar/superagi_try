const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON
app.use(express.json());

// Endpoint for demo requests
app.post('/api/request-demo', (req, res) => {
    // Handle demo request logic
    res.send('Demo request received');
});

// Endpoint for service requests
app.post('/api/request-service', (req, res) => {
    // Handle service request logic
    res.send('Service request received');
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});