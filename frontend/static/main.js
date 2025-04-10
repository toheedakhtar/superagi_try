window.onload = function() {
    fetch('/api/about-content')
        .then(response => response.json())
        .then(data => {
            document.getElementById('about-content').textContent = data.content;
        });
};
