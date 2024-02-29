// base.js

// Example JavaScript code to make navbar dropdowns work
document.addEventListener("DOMContentLoaded", function() {
    // Get all navbar items with dropdown
    var dropdowns = document.querySelectorAll(".navbar-item.dropdown");

    // Add click event listener to each dropdown
    dropdowns.forEach(function(dropdown) {
        dropdown.addEventListener("click", function() {
            // Toggle dropdown menu
            var menu = dropdown.querySelector(".dropdown-menu");
            menu.classList.toggle("show");
        });
    });

    // Close dropdown menu when clicking outside of it
    document.addEventListener("click", function(event) {
        dropdowns.forEach(function(dropdown) {
            var menu = dropdown.querySelector(".dropdown-menu");
            if (!dropdown.contains(event.target) && !menu.contains(event.target)) {
                menu.classList.remove("show");
            }
        });
    });
});
