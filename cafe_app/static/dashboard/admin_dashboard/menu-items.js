function getMenu() {
    fetch('/send-menus').then((response) => {
        console.log(response.status)
        if (response.ok) {
            return response.json();
        } else {
            throw Error(response.status);
        }
    })
        .then((menus) => {
            let tableRow = ''
            for (let menu of menus) {
                tableRow += ' <tr><th scope="row">' + menu.id + '</th>'
                tableRow += '<td>' + menu.name + '</td>'
                tableRow += '<td>' + menu.price + '</td>'
                tableRow += '<td>' + menu.status + '</td>'
                tableRow += '<td>' + menu.picture_path + '</td>'
                tableRow += '<td>' + menu.description + '</td>'
                tableRow += '<td>' + menu.category_id + '</td>'
                tableRow += '<td><span style="cursor: pointer" id="edt-' + menu.id + '" onclick="edtMenu(this)" data-bs-toggle="modal" data-bs-target="#modalEditMenu">edit</span></td>'
                tableRow += '<td><span style="cursor: pointer" id="del-' + menu.id + '" onclick="delMenu(this)">delete</span></td></tr>'
            }
            document.getElementById('mbody').innerHTML = tableRow
        })
        .catch((error) => console.log(error));
}


function newMenu() {
    const form = document.getElementById('newMenu');
    const data = new FormData(form);
    const req = new Request('/new-menu', {
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
            alert(messages, 'warning', 'messageMenu')
            getMenu()
        })
        .catch((error) => console.log(error));


}


function delMenu(el) {

    const el_id = el.getAttribute('id').slice(4)
    let text = 'You want to delete the Category with ID: ' + el_id + '. are you sure?';
    if (confirm(text) === true) {
        let data = JSON.stringify({id: el_id})
        const req = new Request('/del-menu', {
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
                alert(messages, 'warning', 'm-msg')
                getMenu()
            })
            .catch((error) => console.log(error));
    } else {
    }

}


function edtMenu(el){
    const el_id = el.getAttribute('id').slice(4)
    let data = JSON.stringify({id: el_id})
    const req = new Request('/send-menu', {
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
        .then((menu) => {
            document.getElementById('m-id').value = menu.id
            document.getElementById('m-e-name').value = menu.name
            document.getElementById('m-e-price').value = menu.price
            document.getElementById('m-e-picture_path').value = menu.picture_path
            document.getElementById('m-e-status').value = menu.status
            document.getElementById('m-e-category_id').value = menu.category_id
            document.getElementById('m-e-description').value = menu.description
        })
        .catch((error) => console.log(error));
}


function updateMenu(){
    const form = document.getElementById('editMenu');
    const data = new FormData(form);
    const req = new Request('/update-menu', {
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
            console.log(messages)
            alert(messages, 'warning', 'editMMessage')
            getMenu()
        })
        .catch((error) => console.log(error));


}

