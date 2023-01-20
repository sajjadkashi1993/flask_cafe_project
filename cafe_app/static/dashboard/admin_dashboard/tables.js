function getTable() {
    fetch('/send-tables').then((response) => {
        console.log(response.status)
        if (response.ok) {
            return response.json();
        } else {
            throw Error(response.status);
        }
    })
        .then((tables) => {
            let tableRow = ''
            for (let table of tables) {
                tableRow += ' <tr><th scope="row">' + table.id + '</th>'
                tableRow += '<td>' + table.position + '</td>'
                tableRow += '<td>' + table.table_number + '</td>'
                tableRow += '<td>' + table.table_spacing + '</td>'
                tableRow += '<td><span style="cursor: pointer" id="edt-' + table.id + '" onclick="edtTable(this)" data-bs-toggle="modal" data-bs-target="#modalEdit">edit</span></td>'
                tableRow += '<td><span style="cursor: pointer" id="del-' + table.id + '" onclick="delTable(this)">delete</span></td></tr>'
            }
            document.getElementById('tbody').innerHTML = tableRow
        })
        .catch((error) => console.log(error));
}

const alert = (messages, type, id) => {
    const alertPlaceholder = document.getElementById(id)
    alertPlaceholder.innerHTML = ''
    for (let [key, message] of Object.entries(messages)) {
        const wrapper = document.createElement('div')
        wrapper.innerHTML = [
            `<div class="alert alert-${type} alert-dismissible" role="alert">`,
            `   <div>${message}</div>`,
            '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
            '</div>'
        ].join('')

        alertPlaceholder.append(wrapper)
    }
    getTable()
}


function newTable() {
    const form = document.getElementById('newTable');
    const data = new FormData(form);
    const req = new Request('/new-table', {
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
            alert(messages, 'warning', 'message')
        })
        .catch((error) => console.log(error));


}


function delTable(el) {

    const el_id = el.getAttribute('id').slice(4)
    let text = 'You want to delete the table with ID: ' + el_id + '. are you sure?';
    if (confirm(text) === true) {
        let data = JSON.stringify({id: el_id})
        console.log(data)
        const req = new Request('/del-table', {
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
                alert(messages, 'warning', 'tb-msg')
            })
            .catch((error) => console.log(error));
    } else {
    }

}


function edtTable(el){
    
    const el_id = el.getAttribute('id').slice(4)
    let data = JSON.stringify({id: el_id})
    console.log(data)
    const req = new Request('/send-table', {
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
        .then((table) => {
            document.getElementById('t-id').value = table.id
            document.getElementById('t-e-num').value = table.table_number
            document.getElementById('e-position').value = table.position
            document.getElementById('t-e-spacing').value = table.table_spacing
        })
        .catch((error) => console.log(error));
}


function updateTable(){
    const form = document.getElementById('editTable');
    const data = new FormData(form);
    const req = new Request('/update-table', {
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
            alert(messages, 'warning', 'editMessage')
        })
        .catch((error) => console.log(error));


}

