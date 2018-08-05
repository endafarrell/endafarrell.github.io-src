!function ($) {
    $(function () {

        // Activate Bootstrap's tooltips
        $('[data-toggle="tooltip"]').tooltip();

        // Subnav fixing code from
        // https://github.com/thomaspark/bootswatch/blob/gh-pages/2/js/bootswatch.js
        var $win = $(window);
        var $nav = $(".navbar");
        var navTop = $nav.length && $nav.offset().top;
        var isFixed = 0;
        processScroll();
        $win.on('scroll', processScroll);

        function processScroll() {
            var i, scrollTop = $win.scrollTop();
            if (scrollTop >= navTop && !isFixed) {
                isFixed = 1;
                $nav.addClass('navbar-fixed-top')
            } else if (scrollTop <= navTop && isFixed) {
                isFixed = 0;
                $nav.removeClass('navbar-fixed-top')
            }
        }

        // TODO: this should be done server side with a Jinja or Markdown
        // extension.
        // Add bootstrap table style to table elements.
        $("#content table").addClass('table').addClass('table-hover');

        // Make images responsive in article content, which was the default in
        // Bootstrap 2.x. See: https://getbootstrap.com/css/#images-responsive
        $("#content img").addClass('img-responsive');

    });
}(window.jQuery);
