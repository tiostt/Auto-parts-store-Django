const audio = document.querySelector('#audio');
const btnka = document.querySelector('#btnka');

btnka.addEventListener('click', () => {
    audio.paused ? audio.play() : audio.pause();
});


const selectElement = document.getElementById('order-by-select');
const applyButton = document.getElementById('apply-button');

applyButton.addEventListener('click', () => {
    // Получаем выбранное значение
    const selectedValue = selectElement.value;

    // Выбираем соответствующую опцию 
    const options = selectElement.querySelectorAll('option');
    options.forEach(option => {
        if (option.value === selectedValue) {
            option.selected = true;
        }
    });
});