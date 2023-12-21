document.addEventListener('DOMContentLoaded', function() {
  fetch('prediction.txt')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.text();
    })
    .then(text => {
      document.getElementById('prediction').textContent = text;
    })
    .catch(error => {
      console.error('Error fetching the prediction:', error);
      document.getElementById('prediction').textContent = 'Prediction currently unavailable.';
    });
});
