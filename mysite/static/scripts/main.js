$(document).ready(function(){AOS.init({})}),$("a.smooth-scroll").click(function(t){if(location.pathname.replace(/^\//,"")==this.pathname.replace(/^\//,"")&&location.hostname==this.hostname){var a=$(this.hash);a=a.length?a:$("[name="+this.hash.slice(1)+"]"),a.length&&(t.preventDefault(),$("html, body").animate({scrollTop:a.offset().top},1e3,function(){var t=$(a);return t.focus(),!t.is(":focus")&&(t.attr("tabindex","-1"),void t.focus())}))}});