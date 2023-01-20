const alert = (messages, type) => {
    const alertPlaceholder = document.getElementById('updateMessage')
    alertPlaceholder.innerHTML = ''
    for (let [key, message] of Object.entries(messages)){
    const wrapper = document.createElement('div')
    wrapper.innerHTML = [
        `<div class="alert alert-${type} alert-dismissible" role="alert">`,
        `   <div>${message}</div>`,
        '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
        '</div>'
    ].join('')

    alertPlaceholder.append(wrapper)}
}

function getUserOrders() {
    fetch('/send-user-orders').then((response) => {
        console.log(response.status)
        if (response.ok) {
            return response.json();
        } else {
            throw Error(response.status);
        }
    })
        .then((orders) => {
            let tableRow = ''
            // let state = document.getElementById('filter')
            // console.log(state.value)
            for (let order of orders) {
                // if (state.value === 'All Orders' || order.state=== state.value){
                tableRow += ' <tr><th scope="row">' + order.id + '</th>'
                tableRow += '<td>' + order.order_time + '</td>'
                tableRow += '<td>' + order.state + '</td>'
                tableRow += '<td>' + order.delivery_address + '</td>'
                tableRow += '<td>' + order.reserved_id + '</td>'
                tableRow += '<td>' + order.receipt_id + '</td>'
                tableRow += '<td>' + order.order_type + '</td>'
                tableRow += '<td>' + order.offer_id + '</td>'
                tableRow += '<td>' + order.comment + '</td>'
                tableRow += '</tr>'
            }
            document.getElementById('u-obody').innerHTML = tableRow
        })
        .catch((error) => console.log(error));
}

function updateProfile() {
    const form = document.getElementById('update-form');
    const data = new FormData(form);
    const req = new Request('/user-dashboard', {
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
            alert(messages, 'warning')
        })
        .catch((error) => console.log(error));
}

function clickUpdate(){
    document.getElementById("update").style.display = 'block';
    document.getElementById("myOrder").style.display = 'none'}

function clickMyOrder(){
    document.getElementById("update").style.display = 'none';
    document.getElementById("myOrder").style.display = 'block'
    getUserOrders()
}



document.getElementById("btn-update-profile").onclick = clickUpdate
document.getElementById("btn-my-orders").onclick = clickMyOrder