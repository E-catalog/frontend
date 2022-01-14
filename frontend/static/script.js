document.forms['get-individual'].addEventListener('submit', (event) => {
    event.preventDefault();
    fetch(event.target.action, {
        method: 'POST',
        body: new URLSearchParams(new FormData(event.target))
    }).then((resp) => {
        return resp.text();
    }).then((data) => {
        const update_modal_body = document.querySelector('#update-modal');
        update_modal_body.innerHTML = data;

        const get_modal_close = document.querySelector('#get-ind-modal-close-btn');
        get_modal_close.click();

        const update_modal = new bootstrap.Modal(document.getElementById("UpdateIndividualModal"));
        update_modal.show();
    });
});
