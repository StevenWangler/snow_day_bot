document.addEventListener('DOMContentLoaded', function() {
  const dateHeading = document.getElementById('date-heading');
  if (dateHeading) {
    const currentDate = new Date();
    currentDate.setDate(currentDate.getDate() + 1); // Add 1 day to the current date
    const nextDate = currentDate.toLocaleDateString();
    dateHeading.textContent += nextDate;
  } else {
    console.error('Date heading element not found');
  }
});
