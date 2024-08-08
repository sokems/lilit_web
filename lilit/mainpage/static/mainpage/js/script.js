document.addEventListener('DOMContentLoaded', function () {
    const accordions = document.querySelectorAll('.accordion-title');

    accordions.forEach(accordion => {
        accordion.addEventListener('click', function () {
            const content = this.nextElementSibling;

            console.log('Accordion clicked'); // Для проверки

            if (content.style.display === 'block') {
                content.style.display = 'none';
            } else {
                document.querySelectorAll('.accordion-content').forEach(content => {
                    content.style.display = 'none';
                });
                content.style.display = 'block';
            }
        });
    });
});

