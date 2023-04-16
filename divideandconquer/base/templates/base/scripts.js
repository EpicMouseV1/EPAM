function showTab(tabId) {
  var tabContents = document.querySelectorAll('.tab-content');
  tabContents.forEach(function (tabContent) {
    tabContent.style.display = 'none';
  });

  var tabButtons = document.querySelectorAll('.tab-btn');
  tabButtons.forEach(function (tabButton) {
    tabButton.classList.remove('active');
  });

  document.getElementById(tabId).style.display = 'block';
  document.querySelector('.tab-btn[onclick="showTab(\'' + tabId + '\')"]').classList.add('active');
}

// Default active tab
showTab('active-applications');

// Form submission
document.getElementById('create-application-form').addEventListener('submit', function (e) {
  e.preventDefault();
  // Handle form submission here, for example, send data to the server
  alert('Application submitted!');
});

// Mark as completed button click
document.querySelectorAll('.mark-completed').forEach(function (button) {
  button.addEventListener('click', function (e) {
    // Handle marking an application as completed, for example, update the server data
    alert('Marked as completed!');
  });
});