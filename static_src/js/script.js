let navigation = document.getElementById("navigation");
window.addEventListener("scroll", function () {
    if (window.pageYOffset >= 100) {
        navigation.classList.add("active")
    } else if (window.pageYOffset < 90) {
        navigation.classList.remove("active")
    }
})

let openNavigation = $('.navbar-toggler')
openNavigation.click(function () {
    $('body').toggleClass("overflow-hidden")
    $('nav').toggleClass('nav-bg-dark')
    $('.collapse-trick-close').toggleClass('collapse-trick-open')
})

$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
})

$(document).ready(function () {
    $(".dropdown-toggle").dropdown();
});

$(function () {
    let pathName = document.location.pathname;
    window.onbeforeunload = function () {
        let scrollPosition = $(document).scrollTop();
        sessionStorage.setItem("scrollPosition_" + pathName, scrollPosition.toString());
    }
    if (sessionStorage["scrollPosition_" + pathName]) {
        $(document).scrollTop(sessionStorage.getItem("scrollPosition_" + pathName));
    }
});
// let position= $(window).scrollTop();
//
// //some things here
//
// $(window).scrollTop(position);

AOS.init({
    once: true
});
