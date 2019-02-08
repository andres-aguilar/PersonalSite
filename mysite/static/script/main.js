(function openMenu(){
    document.querySelector(".navbar-burger.burger.has-text-white").addEventListener('click', () => {
        document.querySelector('.navbar-menu').classList.toggle('is-active')
    })
})()