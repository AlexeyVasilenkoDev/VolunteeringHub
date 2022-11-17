/*!
* Start Bootstrap - Grayscale v7.0.5 (https://startbootstrap.com/theme/grayscale)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE)
*/
//
// Scripts
//

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    }
    ;

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });
});

// const type = document.getElementById("type");
// const username = document.getElementById("username");
// const phone = document.getElementById("phone");
// const email = document.getElementById("email");
// const password1 = document.getElementById("password1");
// const password2 = document.getElementById("password2");
//
// if (type.value === "") {
//     username.parentElement.parentElement.style.display = 'none';
//     phone.parentElement.parentElement.style.display = 'none';
//     email.parentElement.parentElement.style.display = 'none';
//     password1.parentElement.parentElement.style.display = 'none';
//     password2.parentElement.parentElement.style.display = 'none';
// } else if (type.value === "Single Volunteer" ||
//     type.value === "Volunteers Organisation"
//     ||
//     type.value === "Civil Person"
// ) {
//     username.parentElement.parentElement.style.display = 'none';
//     phone.parentElement.parentElement.style.display = 'initial';
//     email.parentElement.parentElement.style.display = 'initial';
//     password1.parentElement.parentElement.style.display = 'initial';
//     password2.parentElement.parentElement.style.display = 'initial';
// } else {
//     username.parentElement.parentElement.style.display = 'initial';
//     phone.parentElement.parentElement.style.display = 'none';
//     email.parentElement.parentElement.style.display = 'none';
//     password1.parentElement.parentElement.style.display = 'initial';
//     password2.parentElement.parentElement.style.display = 'initial';
// }
// type.addEventListener("change", function () {
//     if (type.value === "") {
//         username.parentElement.parentElement.style.display = 'none';
//         phone.parentElement.parentElement.style.display = 'none';
//         email.parentElement.parentElement.style.display = 'none';
//         password1.parentElement.parentElement.style.display = 'none';
//         password2.parentElement.parentElement.style.display = 'none';
//     } else if (type.value === "Single Volunteer" ||
//         type.value === "Volunteers Organisation"
//         ||
//         type.value === "Civil Person"
//     ) {
//         username.parentElement.parentElement.style.display = 'none';
//         phone.parentElement.parentElement.style.display = 'initial';
//         email.parentElement.parentElement.style.display = 'initial';
//         password1.parentElement.parentElement.style.display = 'initial';
//         password2.parentElement.parentElement.style.display = 'initial';
//     } else {
//         username.parentElement.parentElement.style.display = 'initial';
//         phone.parentElement.parentElement.style.display = 'none';
//         email.parentElement.parentElement.style.display = 'none';
//         password1.parentElement.parentElement.style.display = 'initial';
//         password2.parentElement.parentElement.style.display = 'initial';
//     }
// });
