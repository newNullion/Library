const button = document.getElementById('dropdownButton');
const menu = document.getElementById('dropdownMenu');

button.addEventListener('click', (event) => {
    event.stopPropagation();
    menu.classList.toggle('hidden');
});

document.addEventListener('click', () => {
    menu.classList.add('hidden');
});

menu.addEventListener('click', (event) => {
    event.stopPropagation();
});
