if (document.location.pathname == '/individuals/')
    document.forms['get-individual'].addEventListener('submit', (event) => {
        event.preventDefault();
        fetch(event.target.action, {
            method: 'POST',
            body: new URLSearchParams(new FormData(event.target))
        }).then((resp) => {
            return resp.text();
        }).then((data) => {
            const update_modal_body = document.querySelector('#update-individual-modal');
            update_modal_body.innerHTML = data;

            const get_modal_close = document.querySelector('#get-ind-modal-close-btn');
            get_modal_close.click();

            const update_modal = new bootstrap.Modal(document.getElementById("UpdateIndividualModal"));
            update_modal.show();
        });
    });


if (document.location.pathname == '/places/')
    document.forms['get-place'].addEventListener('submit', (event) => {
        event.preventDefault();
        fetch(event.target.action, {
            method: 'POST',
            body: new URLSearchParams(new FormData(event.target))
        }).then((resp) => {
            return resp.text();
        }).then((data) => {
            const update_modal_body = document.querySelector('#update-place-modal');
            update_modal_body.innerHTML = data;

            const get_modal_close = document.querySelector('#get-place-modal-close-btn');
            get_modal_close.click();

            const update_modal = new bootstrap.Modal(document.getElementById("UpdatePlaceModal"));
            update_modal.show();
        });
    });
