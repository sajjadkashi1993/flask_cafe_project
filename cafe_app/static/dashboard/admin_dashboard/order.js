function getOrders() {
    fetch('/send-orders').then((response) => {
        console.log(response.status)
        if (response.ok) {
            return response.json();
        } else {
            throw Error(response.status);
        }
    })
        .then((orders) => {
            let tableRow = ''
            let state = document.getElementById('filter')
            console.log(state.value)
            for (let order of orders) {
                if (state.value === 'All Orders' || order.state=== state.value){
                tableRow += ' <tr><th scope="row">' + order.id + '</th>'
                tableRow += '<td>' + order.order_time + '</td>'
                tableRow += '<td>' + order.state + '</td>'
                tableRow += '<td>' + order.delivery_address + '</td>'
                tableRow += '<td>' + order.reserved_id + '</td>'
                tableRow += '<td>' + order.receipt_id + '</td>'
                tableRow += '<td>' + order.order_type + '</td>'
                tableRow += '<td>' + order.offer_id + '</td>'
                tableRow += '<td>' + order.comment + '</td>'
                tableRow += '<td><span style="cursor: pointer" id="edt-' + order.id + '" onclick="edtOrder(this)" data-bs-toggle="modal" data-bs-target="#modalEditOrder">edit</span></td></tr>'
            }}
            document.getElementById('obody').innerHTML = tableRow
        })
        .catch((error) => console.log(error));
}

function edtOrder(el){
    const el_id = el.getAttribute('id').slice(4)
    let data = JSON.stringify({id: el_id})
    const req = new Request('/send-order', {
        method: 'POST',
        body: data
    });
    fetch(req).then((response) => {
        console.log(response.status)
        if (response.ok) {
            return response.json();
        } else {
            throw Error(response.status);
        }
    })
        .then((order) => {
            document.getElementById('o-id').value = order.id
            document.getElementById('o-e-state').value = order.state

        })
        .catch((error) => console.log(error));
}


function updateOrder(){
    const form = document.getElementById('editOrder');
    const data = new FormData(form);
    const req = new Request('/update-order', {
        method: 'POST',
        body: data
    });
    fetch(req).then((response) => {
        console.log(response.status)
        if (response.ok) {
            return response.json();
        } else {
            throw Error(response.status);
        }
    })
        .then((messages) => {
            alert(messages, 'warning', 'editOMessage')
            getOrders()
        })
        .catch((error) => console.log(error));
}

