// server.js - Basic Express server setup for AgriSphere

const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to serve static files
app.use(express.static('frontend'));

// Basic route
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/frontend/index.html');
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});