let navigation = document.getElementById("navigation");
window.addEventListener("scroll", function () {
    if (window.pageYOffset >= 100) {
        navigation.classList.add("active")
    } else if (window.pageYOffset < 90) {
        navigation.classList.remove("active")
    }
})

// let hamburger = document.querySelector(".hamburger");
// hamburger.addEventListener("click", function () {
//     hamburger.classList.toggle("open");
//     document.body.classList.toggle("menu-open");
// })

let openNavigation = $('.navbar-toggler')
openNavigation.click(function () {
    $('body').toggleClass("overflow-hidden")
    $('nav').toggleClass('nav-bg-dark')
})



AOS.init();
