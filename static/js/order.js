$(document).ready(function () {

    $('#order-confirmation').hide();

    $(document).on('click', '#order-submit', function (e) {

        e.preventDefault();
        var menuOrder = JSON.parse(sessionStorage.menuOrder);

        var menuItems = []
        menuOrder.menuItems.forEach(function (menuItem) {
            menuItems.push({"id": menuItem.id, "quantity": menuItem.quantity});
        });


        var orderRequest = new Object();

        orderRequest.name = $(this).closest('#order-submit-form').find('input[name="name"]').val();
        orderRequest.phone = $(this).closest('#order-submit-form').find('input[name="mobile"]').val();
        orderRequest.email = $(this).closest('#order-submit-form').find('input[name="email"]').val();
        orderRequest.restaurantId = 1;
        orderRequest.menuItems = menuItems;

        $.ajax({
            url: "/api/v1/restaurants/1/order",
            type: "POST",
            data: JSON.stringify(orderRequest),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (data) {
                console.info("Confirmation Number : " + data.confirmation_number)
                console.info("Order Time : " + data.order_time)
                console.info("Finish Time: " + data.finish_time)
                console.info("Restaurant Info : " + data.restaurant_info)

                sessionStorage.removeItem('menuCount');
                sessionStorage.removeItem('menuOrder');

                $('#order-food').hide();
                $('#title-image').hide();
                $('#order-confirmation').show();

                $("#order-summary").empty();
                $("#order-summary").html(
                    '<div class="form-group row">\n' +
                    '   <label for="name" class="col-sm-2 col-form-label">Confirmation Number : </label>\n' +
                    '   <div class="col-sm-4">'+data.confirmation_number+'</div>\n' +
                    '</div>'+
                    '<div class="form-group row">\n' +
                    '   <label for="name" class="col-sm-2 col-form-label">Order Time : </label>\n' +
                    '   <div class="col-sm-4">'+data.order_time+'</div>\n' +
                    '</div>'+
                    '<div class="form-group row">\n' +
                    '   <label for="name" class="col-sm-2 col-form-label">Finish Time : </label>\n' +
                    '   <div class="col-sm-4">'+data.finish_time+'</div>\n' +
                    '</div>'
                );


                $('#menuCount').empty();
                $('#menuCount').append(sessionStorage.menuCount);
            }
        });
    });
});