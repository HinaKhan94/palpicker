
const myModal = new bootstrap.Modal(document.getElementById('request-service'));
const OfferModal = new bootstrap.Modal(document.getElementById('offerModal'));

window.addEventListener('DOMContentLoaded', () => {
    myModal.show();
    OfferModal.show();
    console.log('modal clicked')
});
