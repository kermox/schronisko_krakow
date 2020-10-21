// Init AOS module.
AOS.init({
    once: true
});


// Init AnimateNumber module.
$('.count').each(function () {
    $(this).animateNumber(
        {
            number: $(this).text(),
            numberStep: $.animateNumber.numberStepFactories.separator(' ')
        },
        2500
    )
});


// Init stickyTabs module.
$(document).ready(function () {
    options = {
        scrollToTab: $(".nav-pills"),
    }
    $('.nav-pills').stickyTabs(options);
})


// When redirecting to tabs from home page on small and medium screen size devices, close the navigation menu
// and remove classes connected to it.
$('.external-tab-link').on('click', function () {
    $('#navbarSupportedContent').collapse('hide')
    $('body').removeClass('overflow-hidden')
    $('nav').removeClass('bg-dark')
})


// SearchForm radio inputs handling (to make them look as select inputs)
let selected = document.querySelectorAll(".selected");

selected.forEach(function (x) {
    x.addEventListener("click", () => {
        let i = document.getElementById(x.id)
        let j = document.getElementById(i.closest('.select-box').id)
        j.querySelector('.option-container').classList.toggle("active");
        j.querySelector('.selected').classList.toggle("active");
        let optionList = j.querySelectorAll('.option')
        optionList.forEach(o => {
            o.addEventListener("click", () => {
                if (x.id === 'searchAge') {
                    x.innerHTML = "wiek" + " : " + '<span class="form-select-input">' + o.querySelector("label").innerHTML + '</span>';
                } else if (x.id === 'searchSpecies') {
                    x.innerHTML = "gatunek" + " : " + '<span class="form-select-input">' + o.querySelector("label").innerHTML + '</span>';
                } else if (x.id === 'searchSize') {
                    x.innerHTML = "rozmiar" + " : " + '<span class="form-select-input">' + o.querySelector("label").innerHTML + '</span>';
                } else if (x.id === 'searchGender') {
                    x.innerHTML = "płeć" + " : " + '<span class="form-select-input">' + o.querySelector("label").innerHTML + '</span>';
                }
                j.querySelector('.option-container').classList.remove("active");
                j.querySelector('.selected').classList.remove("active");
                j.querySelector('.reset').classList.add('show')
            });
        });
    })
});


// Reset button in SearchForm handling
let reset = document.querySelectorAll('.reset')
reset.forEach(function (x) {
    x.addEventListener('click', () => {
        let selectBox = document.getElementById(x.closest('.select-box').id)
        let selected = selectBox.querySelector(".selected")
        if (selected.id === 'searchAge') {
            selected.innerHTML = "wiek"
        } else if (selected.id === 'searchSpecies') {
            selected.innerHTML = "gatunek"
        } else if (selected.id === 'searchSize') {
            selected.innerHTML = "rozmiar"
        } else if (selected.id === 'searchGender') {
            selected.innerHTML = "płeć"
        }
        x.classList.remove('show')
    })
})


// Handling navigation active state
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

// Facebook embed responsive handling
// Add events to listen to screen width change
if (matchMedia) {
    const mq = window.matchMedia("(min-width: 600px)");
    const mq2 = window.matchMedia("(min-width: 501px")
    mq.addEventListener("change", WidthChange);
    mq2.addEventListener("change", WidthChange);
    WidthChange(mq, mq2);
}

// Set attributes depending on media query change (needs page reload)
function WidthChange(mq, mq2) {
    if (mq.matches) {
        $('.fb-post').attr('data-width', "550")
    } else if (mq2.matches) {
        $('.fb-post').attr('data-width', "450")
    } else {
        $('.fb-post').attr({'data-width': "340", 'style': 'overflow-x: scroll;'})
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
