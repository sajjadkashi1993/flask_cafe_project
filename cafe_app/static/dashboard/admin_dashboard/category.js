function getCategory() {
    fetch('/send-categories').then((response) => {
        console.log(response.status)
        if (response.ok) {
            return response.json();
        } else {
            throw Error(response.status);
        }
    })
        .then((categories) => {
            let tableRow = ''
            for (let category of categories) {
                tableRow += ' <tr><th scope="row">' + category.id + '</th>'
                tableRow += '<td>' + category.name + '</td>'
                tableRow += '<td>' + category.description + '</td>'
                tableRow += '<td><span style="cursor: pointer" id="edt-' + category.id + '" onclick="edtCategory(this)" data-bs-toggle="modal" data-bs-target="#modalEditCategory">edit</span></td>'
                tableRow += '<td><span style="cursor: pointer" id="del-' + category.id + '" onclick="delCategory(this)">delete</span></td></tr>'
            }
            document.getElementById('cbody').innerHTML = tableRow
        })
        .catch((error) => console.log(error));
}


function newCategory() {
    const form = document.getElementById('newCategory');
    const data = new FormData(form);
    const req = new Request('/new-category', {
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
            alert(messages, 'warning', 'messageCategory')
            getCategory()
        })
        .catch((error) => console.log(error));


}


function delCategory(el) {

    const el_id = el.getAttribute('id').slice(4)
    let text = 'You want to delete the Category with ID: ' + el_id + '. are you sure?';
    if (confirm(text) === true) {
        let data = JSON.stringify({id: el_id})
        const req = new Request('/del-category', {
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
                alert(messages, 'warning', 'c-msg')
                getCategory()
            })
            .catch((error) => console.log(error));
    } else {
    }

}


function edtCategory(el){
    const el_id = el.getAttribute('id').slice(4)
    let data = JSON.stringify({id: el_id})
    const req = new Request('/send-category', {
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
        .then((category) => {
            document.getElementById('c-id').value = category.id
            document.getElementById('c-e-name').value = category.name
            document.getElementById('c-e-description').value = category.description
        })
        .catch((error) => console.log(error));
}


function updateCategory(){
    const form = document.getElementById('editCategory');
    const data = new FormData(form);
    const req = new Request('/update-category', {
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
            alert(messages, 'warning', 'editCMessage')
            getCategory()
        })
        .catch((error) => console.log(error));


}

