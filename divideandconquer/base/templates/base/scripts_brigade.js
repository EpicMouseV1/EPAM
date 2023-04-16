// Add this function to handle tab switching for the brigade page
function openTab(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tab-content");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tab-btn");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}

// Add event listeners for the Proceed and Mark as Done buttons for the brigade
document.querySelectorAll('.proceed').forEach(function (button) {
  button.addEventListener('click', function (e) {
    // Change the status to In Progress and update the button to Mark as Done
    var row = e.target.closest('tr');
    row.querySelector('.status').innerText = 'In Progress';
    e.target.innerText = 'Mark as Done';
    e.target.classList.remove('proceed');
    e.target.classList.add('mark-as-done');

    // Add event listener to the Mark as Done button
    row.querySelector('.mark-as-done').addEventListener('click', function (e) {
      // Move the application to the closed-applications table
      var row = e.target.closest('tr');
      row.querySelector('.mark-as-done').remove();
      document.getElementById('closed-applications').querySelector('tbody').appendChild(row);
    });
  });
});
