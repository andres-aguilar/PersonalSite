document.addEventListener('DOMContentLoaded', function() {
	var elems = document.querySelectorAll('.parallax')
	var instances = M.Parallax.init(elems, {})

	var side = document.querySelectorAll('.sidenav')
    var side_instances = M.Sidenav.init(side, {})
})
