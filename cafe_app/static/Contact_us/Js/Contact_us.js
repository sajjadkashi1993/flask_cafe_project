const alert = (messages, type) => {
    const alertPlaceholder = document.getElementById('sendMessage')
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
}


function get_comments() {
    const form = document.getElementById('contact-form');
    const data = new FormData(form);
    const req = new Request('/contact', {
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