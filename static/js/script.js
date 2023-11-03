
const myModal = new bootstrap.Modal(document.getElementById('request-service'));
const OfferModal = new bootstrap.Modal(document.getElementById('offerModal'));

window.addEventListener('DOMContentLoaded', () => {
    myModal.show();
    OfferModal.show();
    console.log('modal clicked');
});

function hideRequestButton() {
    // 
    document.querySelector('#make-request-btn').style.display = 'none';
}

setTimeout(function () {
    let messages = document.getElementById('approval-msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);