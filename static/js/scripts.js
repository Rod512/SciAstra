function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    const closeBtn = document.querySelector('.close-btn');
    const hamburger = document.querySelector('.hamburger');

    navLinks.classList.toggle('nav-active');
    closeBtn.classList.toggle('show-close');
    hamburger.classList.toggle('hide-hamburger');
}
