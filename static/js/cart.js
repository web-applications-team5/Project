$(document).ready(function () {

    $('#menuCount').empty();
    $('#menuCount').append(sessionStorage.menuCount);

    function populateCartWithChoosedMenuItems() {

        if (typeof (Storage) !== "undefined") {
            if (sessionStorage.menuOrder) {

                var menuOrder = JSON.parse(sessionStorage.menuOrder);

                $("#cart-table-body").empty();

                menuOrder.menuItems.forEach(function (menuItem) {

                    $.get("/api/v1/item/" + menuItem.id).done(function (data) {

                        $('#cart-table-body').append(
                            '<tr class="cart-menu-item" data-menuItemId="' + menuItem.id + '">\n' +
                            '  <td colspan="2" class="prod-column">\n' +
                            '      <div class="column-box">\n' +
                            '          <figure class="prod-thumb">' +
                            '              <a href="#"><img src="/static/images/' + data.photo + '" alt=""></a>' +
                            '          </figure>\n' +
                            '          <h4 class="prod-title">' + data.name + '</h4>\n' +
                            '      </div>\n' +
                            '  </td>\n' +
                            '  <td class="price">$ ' + data.price + '</td>\n' +
                            '  <td class="qty">\n' +
                            '      <div class="quantity-spinner">\n' +
                            '          <button type="button" class="minus minus-menu-item-qty"><span class="fa fa-minus"></span></button>\n' +
                            '          <input type="text" name="product" value="' + menuItem.quantity + '" class="prod_qty"/>\n' +
                            '          <button type="button" class="plus plus-menu-item-qty"><span class="fa fa-plus"></span></button>\n' +
                            '      </div>\n' +
                            '  </td>\n' +
                            '  <td class="sub-total">$ ' + (data.price * menuItem.quantity) + '</td>\n' +
                            '  <td class="remove remove-cart-item"><a href="#" class="remove-btn"><span class="fa fa-remove"></span></a>\n' +
                            '  </td>\n' +
                            '</tr>'
                        )
                    });
                });
            }
        } else {
            console.error("Sorry, your browser does not support web storage...");
        }
    }

    populateCartWithChoosedMenuItems();


    function updateItemQuantity(newQty, menuItemId) {

        if (typeof (Storage) !== "undefined") {
            if (sessionStorage.menuCount) {

                var menuOrder = JSON.parse(sessionStorage.menuOrder);
                var newMenuCount = 0;
                var indexToRemove = -1;

                for (let i = 0; i < menuOrder.menuItems.length; i++) {
                    if (menuItemId === menuOrder.menuItems[i].id) {
                        if (newQty < 1) {
                            indexToRemove = i;
                        } else {
                            menuOrder.menuItems[i].quantity = newQty;
                            newMenuCount += menuOrder.menuItems[i].quantity;
                        }
                    } else {
                        newMenuCount += menuOrder.menuItems[i].quantity;
                    }
                }

                if(indexToRemove > -1) {
                    menuOrder.menuItems.splice(indexToRemove, 1);
                }

                sessionStorage.menuOrder = JSON.stringify(menuOrder);
                sessionStorage.menuCount = newMenuCount;

            }
            $('#menuCount').empty();
            $('#menuCount').append(sessionStorage.menuCount);
        } else {
            console.error("Sorry, your browser does not support web storage...");
        }
    }

    $(document).on('click', '.remove-cart-item', function (e) {
        e.preventDefault();
        var menuItemId = $(this).closest('tr').data('menuitemid');
        $(this).closest('tr').remove();
        updateItemQuantity(0, menuItemId);
    });

    $(document).on('click', '.plus-menu-item-qty', function (e) {

        var menuItemId = $(this).closest('.cart-menu-item').data('menuitemid');
        var val = $(this).closest('.cart-menu-item').find("input[name='product']").val();
        var price = $(this).closest('.cart-menu-item').find(".price").text().substring(2);

        val = Number(val);
        price = Number(price);

        $(this).closest('.cart-menu-item').find("input[name='product']").val(val + 1);
        $(this).closest('.cart-menu-item').find('.sub-total').empty();
        $(this).closest('.cart-menu-item').find('.sub-total').html('$ ' + (val + 1) * price);
        updateItemQuantity(val + 1, menuItemId);
    });

    $(document).on('click', '.minus-menu-item-qty', function (e) {

        var menuItemId = $(this).closest('tr').data('menuitemid');
        var val = $(this).closest('tr .qty').find("input[name='product']").val();
        var price = $(this).closest('.cart-menu-item').find(".price").text().substring(2);

        val = Number(val);
        price = Number(price);

        if (val >= 2) {
            $(this).closest('.cart-menu-item').find("input[name='product']").val(val - 1);
            $(this).closest('.cart-menu-item').find('.sub-total').empty();
            $(this).closest('.cart-menu-item').find('.sub-total').html('$ ' + (val - 1) * price);
        } else if (val === 1) {
            $(this).closest('tr').remove();
            updateItemQuantity(val - 1, menuItemId);
        }

        updateItemQuantity(val - 1, menuItemId);
    });


});