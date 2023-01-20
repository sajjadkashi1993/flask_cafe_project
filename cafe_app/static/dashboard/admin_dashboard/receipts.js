function getReceipts() {
    fetch('/send-receipts').then((response) => {
        console.log(response.status)
        if (response.ok) {
            return response.json();
        } else {
            throw Error(response.status);
        }
    })
        .then((receipts) => {
            let tableRow = ''
            let state = document.getElementById('r-filter')
            console.log(state.value)
            for (let receipt of receipts) {
                if (state.value === 'All Receipt' || receipt.state=== state.value){
                tableRow += ' <tr><th scope="row">' + receipt.id + '</th>'
                tableRow += '<td>' + receipt.total_price + '</td>'
                tableRow += '<td>' + receipt.discount + '</td>'
                tableRow += '<td>' + receipt.final_price + '</td>'
                tableRow += '<td>' + receipt.receipt_time + '</td>'
                tableRow += '<td>' + receipt.state + '</td>'
                tableRow += '</tr>'
            }}
            document.getElementById('rbody').innerHTML = tableRow
        })
        .catch((error) => console.log(error));
}
