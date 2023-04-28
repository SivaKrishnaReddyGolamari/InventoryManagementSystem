function redirectToIndex() {
  window.location.href = "/index";
}

function redirectTosignup() {
  window.location.href = "/signup";
}





      
var popup = document.querySelector('.popup');

var closeButton = document.querySelector('.close');
        // Open the popup when the page loads
window.onload = function() {
      popup.style.display = 'block';
  };

// Close the popup when the user clicks the close button
closeButton.onclick = function() {
  popup.style.display = 'none';
};


