document.getElementById('recommend-button').addEventListener('click', function() {
    const word = document.getElementById('word-input').value;
    
    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title: word })
    })
    .then(response => response.json())
    .then(data => {
        const movieGallery = document.getElementById('movie-gallery');
        movieGallery.innerHTML = '';

        data.forEach(movie => {
            const movieElement = document.createElement('div');
            movieElement.className = 'movie';
            movieElement.innerHTML = `
                <img src="${movie.poster || 'https://via.placeholder.com/200x300'}" alt="${movie.title}">
                <h2>${movie.title}</h2>
            `;
            movieGallery.appendChild(movieElement);
        });
    })
    .catch(error => console.error('Error fetching recommendations:', error));
});
