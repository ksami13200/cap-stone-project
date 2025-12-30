document.addEventListener('DOMContentLoaded', function () {
    console.log('Our Plants website loaded!');

    // Example: Highlight active navigation link
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav ul li a');

    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.style.color = 'var(--secondary-color)';
            link.style.fontWeight = 'bold';
        }
    });
});
