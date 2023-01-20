function getContact() {
    fetch('/send-contact').then((response) => {
        console.log(response.status)
        if (response.ok) {
            return response.json();
        } else {
            throw Error(response.status);
        }
    })
        .then((contacts) => {
            let tableRow = ''
            for (let contact of contacts) {
                tableRow += ' <tr><th scope="row">' + contact.id + '</th>'
                tableRow += '<td>' + contact.first_name + '</td>'
                tableRow += '<td>' + contact.last_name + '</td>'
                tableRow += '<td>' + contact.email + '</td>'
                tableRow += '<td>' + contact.phone + '</td>'
                tableRow += '<td>' + contact.message + '</td>'
                tableRow += '<td><span style="cursor: pointer" id="del-' + contact.id + '" onclick="delContact(this)">delete</span></td></tr>'
            }
            document.getElementById('contact-body').innerHTML = tableRow
        })
        .catch((error) => console.log(error));
}



function delContact(el) {

    const el_id = el.getAttribute('id').slice(4)
    let text = 'You want to delete the Contact with ID: ' + el_id + '. are you sure?';
    if (confirm(text) === true) {
        let data = JSON.stringify({id: el_id})
        const req = new Request('/del-contact', {
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
                alert(messages, 'warning', 'contact-msg')
                getContact()
            })
            .catch((error) => console.log(error));
    } else {
    }
}

