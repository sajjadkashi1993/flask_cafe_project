function updateShopItems() {
    $.ajax({
        type: "GET",
        url: "/update-cart-data",
        success: function (result) {
            let addRow = '';
            let sumPrice = 0;
            document.getElementById('cart-table').innerHTML = addRow;
            const full_info = JSON.parse(result);
            for (const item in full_info) {
                rowNumber = parseInt(item) + 1;
                addRow += '<tr> <th scope="row">' + rowNumber + '</th>';
                addRow += '<td>' + full_info[item]['name'] + '</td>';
                addRow += '<td>' + full_info[item]['quantity'] + '</td>';
                addRow += '<td>' + full_info[item]['price'] + '</td>';
                addRow += '<td> <button type="button" class="btn-close" onclick="deleteCartData(' + full_info[item]['id'] + ')"></button> </td> </tr>';
                sumPrice += (parseInt(full_info[item]['price']) * parseInt(full_info[item]['quantity']))
            }
            document.getElementById('cart-table').innerHTML = addRow;
            document.getElementById('subtotal').textContent = sumPrice + ' $';
            document.getElementById('total-price').textContent = sumPrice + ' $';
        }
    });
    $.ajax({
        type: "GET",
        url: "/update-table-data",
        success: function (result) {
            let addRow = '<option selected>Select Your Table from the List</option>';
            // let sumPrice = 0;
            document.getElementById('table-box').innerHTML = addRow;
            const full_info = JSON.parse(result);
            for (const table in full_info) {
                addRow += '<option value=' + full_info[table]['id'] + '>Table '
                    + full_info[table]['table-number'] + ' | ' + full_info[table]['seater'] + '-Seater</option>';
            }
            document.getElementById('table-box').innerHTML = addRow;
        }
    });
};

function checkOffCode() {
    const disCode = document.getElementById('discount-code').value
    const req = new Request('/check-offer-code', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({'code': disCode}),
    });
    fetch(req)
        .then((response) => {
            if (response.ok) {
                document.getElementById('checking-discount-code').innerText = 'Code is OK!';
                document.getElementById('checking-discount-code').style.color = 'green';
                return response.json();
            } else {
                document.getElementById('checking-discount-code').innerText = 'Code is not OK!';
                document.getElementById('checking-discount-code').style.color = 'red';
                const subTotal = document.getElementById('subtotal').textContent;
                document.getElementById('total-price').textContent = subTotal;
                throw Error(response.status);
            }
        })
        .then((date) => {
            offerData = JSON.parse(date);
            console.log(offerData['percent']);
            const subTotal = parseInt(document.getElementById('subtotal').textContent);
            const totalPrice = subTotal * (1 - (offerData['percent']) / 100);
            document.getElementById('total-price').textContent = totalPrice + ' $';
        })
};

// The function for remove item from cart
function deleteCartData(id) {
    const listData = [
        {"id": id}
    ];
    $.ajax({
        type: "DELETE",
        url: "/delete-cart-data",
        data: JSON.stringify(listData),
        contentType: "application/json",
        dataType: 'json',
        success: function (result) {
            updateShopItems()
            console.log("POST Result:");
            console.log(result);
        }
    });
}


function purchase() {
        const purchaseData = [{
            "total-price": document.getElementById('subtotal').textContent,
            "final-price": document.getElementById('total-price').textContent,
            "state": document.getElementById('order-in-cafe').checked ?'order_in_cafe': document.getElementById('order-ahead').checked ? 'order_ahead': "take_away" ,
            "table": document.getElementById('order-in-cafe').checked ? $("#table-box option:selected").text(): null,
            "address": document.getElementById('order-ahead').checked ?document.getElementById("address").value: null,
            "offer_code": document.getElementById('checking-discount-code').style.color === 'green' ? document.getElementById('discount-code').value :null
        }
        ];
        console.log(purchaseData)
        $.ajax({
            type: "POST",
            url: "/purchase",
            data: JSON.stringify(purchaseData),
            contentType: "application/json",
            dataType: 'json',
            success: function () {
                document.getElementById("transaction-result").innerText = 'Successful Transaction';
                document.getElementById("transaction-result").style.color = 'green';
                updateShopItems()
            },
            error: function () {
                document.getElementById("transaction-result").innerText = 'Unsuccessful Transaction';
                document.getElementById("transaction-result").style.color = 'red';
            }
        });
}
