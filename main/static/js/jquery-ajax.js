// Когда html документ готов (прорисован)
$(document).ready(function () {
    // берем в переменную элемент разметки с id jq-notification для оповещений от ajax
    var successMessage = $("#jq-notification");

    // Ловим собыитие клика по кнопке добавить в корзину
    $(document).on("click", ".add-to-cart", function (e) {
        // Блокируем его базовое действие
        e.preventDefault();

        // // Берем элемент счетчика в значке корзины и берем оттуда значение
        // var goodsInCartCount = $("#goods-in-cart-count");
        // var cartCount = parseInt(goodsInCartCount.text() || 0);

        // Получаем id товара из атрибута data-product-id
        var product_id = $(this).data("product-id");

        // Из атрибута href берем ссылку на контроллер django
        var add_to_cart_url = $(this).attr("href");

        // делаем post запрос через ajax не перезагружая страницу
        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Сообщение
                successMessage.html(`<span class="close-button" onclick="closeNotification(this)">×</span><br>${data.message}`);
                successMessage.fadeIn(400);
            
                // Через 7сек убираем сообщение
                setTimeout(function () {
                    successMessage.css("display", "none"); // Удаляем сообщение через 7 секунд
                }, 7000); 

                // Увеличиваем количество товаров в корзине (отрисовка в шаблоне)
                // cartCount++;
                // goodsInCartCount.text(cartCount);

                // // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
                // var cartItemsContainer = $("#cart-items-container");
                // cartItemsContainer.html(data.cart_items_html);

            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    });





    // Ловим собыитие клика по кнопке удалить товар из корзины
    $(document).on("click", ".remove-from-cart", function (e) {
        // Блокируем его базовое действие
        e.preventDefault();

        // Получаем id корзины из атрибута data-cart-id
        var basket_id = $(this).data("basket-id");
        // Из атрибута href берем ссылку на контроллер django
        var remove_from_cart = $(this).attr("href");

        // делаем post запрос через ajax не перезагружая страницу
        $.ajax({
            type: "POST",
            url: remove_from_cart,
            data: {
                basket_id: basket_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {

                // Сообщение
                successMessage.html(`<span class="close-button" onclick="closeNotification(this)">×</span><br>${data.message}`);
                successMessage.css("display", "block"); // Устанавливаем display на block
                successMessage.fadeIn(400); // Показываем сообщение
                
                // Через 7сек убираем сообщение  
                setTimeout(function () {
                    successMessage.css("display", "none"); // Устанавливаем display на none
                }, 3000); 

                // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);
            },
            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    });


    $(document).on("click", ".add-item-basket", function (e) {
        // Определяем, на какую кнопку нажали
        var button = e.target;

        // Проверяем, является ли нажатая кнопка кнопкой increment
        if (button.classList.contains("increment")) {
            // Получаем url, cartID и значение input
            var url = $(button).data("cart-change-url");
            var cartID = $(button).data("cart-id");
            var $input = $(button).closest('.total-price').find('.number');
            var currentValue = parseInt($input.val());

            // Изменяем значение input
            currentValue += 1;
            $input.val(currentValue);

            // Вызываем функцию updateCart
            updateCart(cartID, currentValue, url);
        }
        if (button.classList.contains("decrement")) {
            // Получаем url, cartID и значение input
            var url = $(this).data("cart-change-url");
            // Берем id корзины из атрибута data-cart-id
            var cartID = $(this).data("cart-id");
            // Ищем ближайшеий input с количеством 
            var $input = $(this).closest('.total-price').find('.number');
            // Берем значение количества товара
            var currentValue = parseInt($input.val());
            // Если количества больше одного, то только тогда делаем -1
            if (currentValue > 1) {
                $input.val(currentValue - 1);
                // Запускаем функцию определенную ниже
                // с аргументами (id карты, новое количество, количество уменьшилось или прибавилось, url)
                updateCart(cartID, currentValue - 1, url);
            }
        }
    });

    function updateCart(cartID, quantity, url) {
        console.log(url);
        console.log(cartID);
        console.log(quantity);
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },

            success: function (data) {
                // Сообщение
                successMessage.html(`<span class="close-button" onclick="closeNotification(this)">×</span><br>${data.message}`);
                successMessage.fadeIn(400);
                // Через 7сек убираем сообщение
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);

                // Меняем содержимое корзины
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },
            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    }
});