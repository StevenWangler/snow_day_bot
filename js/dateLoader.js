document.addEventListener('DOMContentLoaded', function() {
    const dateHeading = document.getElementById('date-heading');
    if (dateHeading) {
      const currentDate = new Date().toLocaleDateString();
      dateHeading.textContent += currentDate;
    } else {
      console.error('Date heading element not found');
    }
  });
  