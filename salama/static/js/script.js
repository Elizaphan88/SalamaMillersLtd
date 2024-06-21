window.addEventListener('scroll', function() {
    var navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) { // Adjust the value as needed
        navbar.classList.add('sticky');
        navbar.classList.remove('transparent');
    } else {
        navbar.classList.add('transparent');
        navbar.classList.remove('sticky');
    }
});
