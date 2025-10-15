const button = document.getElementById('toggle-theme');
const html = document.documentElement;

button.addEventListener('click', () => {
    let theme = html.getAttribute('data-bs-theme');
    let new_theme = (theme == 'dark') ? 'light' : 'dark';
    html.setAttribute('data-bs-theme', new_theme);
});