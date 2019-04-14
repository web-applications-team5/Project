$(document).ready(function () {

    $('#menuCount').empty();
    $('#menuCount').append(sessionStorage.menuCount);

    $(document).on('click', '.menuItemAddToCart', function (e) {

        var menuItemId = $(this).data('menuitemid');
        var newMenuItem = new Object();

        if (typeof (Storage) !== "undefined") {
            if (sessionStorage.menuCount) {

                var menuOrder = JSON.parse(sessionStorage.menuOrder);
                var alreadyHasItem = false;

                menuOrder.menuItems.forEach(function (menuItem) {
                    if (menuItemId === menuItem.id) {
                        menuItem.quantity = menuItem.quantity + 1;
                        alreadyHasItem = true;
                    }
                });

                if(!alreadyHasItem) {
                    newMenuItem.id = menuItemId;
                    newMenuItem.quantity = 1;
                    menuOrder.menuItems.push(newMenuItem);
                }

                sessionStorage.menuOrder = JSON.stringify(menuOrder);
                sessionStorage.menuCount = Number(sessionStorage.menuCount) + 1;

            } else {
                newMenuItem.id = menuItemId;
                newMenuItem.quantity = 1;
                sessionStorage.menuOrder = JSON.stringify({'menuItems': [newMenuItem]});
                sessionStorage.menuCount = 1;
            }
            $('#menuCount').empty();
            $('#menuCount').append(sessionStorage.menuCount);
        } else {
            console.error("Sorry, your browser does not support web storage...");
        }
    });

    $.get("/api/v1/restaurants/1/menu").done(function (data) {

        $('#menuItemsList').empty();
        data.menu.forEach(function (menuItem) {

            console.log("appending " + menuItem.id);
            $('#menuItemsList').append(
                '<div class="col-md-3 col-sm-6">\n' +
                '    \t\t<span class="thumbnail">\n' +
                '      \t\t\t<img src="/static/images/' + menuItem.photo + '" alt="...">\n' +
                '      \t\t\t<h4 style="text-align:center; padding:10px 0;">' + menuItem.name + '</h4>\n' +
                '      \t\t\t\n' +
                '      \t\t\t<!--<p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. </p>-->\n' +
                '                <div class="row">\n' +
                '      \t\t\t\t<div class="col-md-12 col-sm-12">\n' +
                '      \t\t\t\t\t<p class="price" style="color:#F00; text-align:center;font-size:18px;">' + menuItem.price + '$</p>\n' +
                '      \t\t\t\t</div>\n' +
                '      \t\t\t\t      \t\t\t\t\n' +
                '      \t\t\t</div>\n' +
                '      \t\t\t<hr class="line">\n' +
                '      \t\t\t<div class="row">\n' +
                '      \t\t\t\t<div class="col-md-6 col-sm-6 col-xs-12">\n' +
                '      \t\t\t\t\t<button class="btn btn-danger center-block menuItemAddToCart" style="margin-top:10px;" data-menuItemId="' + menuItem.id + '"> Add To Cart</button>\n' +
                '      \t\t\t\t</div>\n' +
                '      \t\t\t\t\n' +
                '      \t\t\t\t\n' +
                '      \t\t\t</div>\n' +
                '    \t\t</span>\n' +
                '  \t\t</div>'
            )
        });
    });
});