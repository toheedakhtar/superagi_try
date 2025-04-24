window.onload = function() {
    fetch('/api/about-content')
        .then(response => response.json())
        .then(data => {
            document.getElementById('vision-content').textContent = data.vision;
            document.getElementById('mission-content').textContent = data.mission;
            document.getElementById('director-content').textContent = data.director;
        });
};
