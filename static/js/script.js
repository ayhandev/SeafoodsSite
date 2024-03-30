const themeButton = document.getElementById('themeButton');
const body = document.body;

themeButton.addEventListener('click', () => {
    body.classList.toggle('dark-theme');
});


