const myModal = new bootstrap.Modal(document.getElementById('request-service'));
const OfferModal = new bootstrap.Modal(document.getElementById('offerModal'));

/** Modal event listener function **/
window.addEventListener('DOMContentLoaded', () => {
   myModal.show();
   OfferModal.show();
   console.log('modal clicked');
});

/** Button hide on details page
 *  event listener function **/
function hideRequestButton() {
   // 
   document.querySelector('#make-request-btn').style.display = 'none';
}
