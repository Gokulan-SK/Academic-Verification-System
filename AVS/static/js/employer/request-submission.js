document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("documentForm");
    var successMessage = document.querySelector(".success-message");
    var errorMessage = document.querySelector(".error-message");

    // Add event listener to the form submission
    form.addEventListener("submit", function(event) {
        // Prevent the default form submission
        event.preventDefault();
        
        // Get the form data
        var formData = new FormData(this);

        // Add the CSRF token to the form data
        var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        formData.append('csrfmiddlewaretoken', csrfToken);

        // Send the form data using AJAX
        var xhr = new XMLHttpRequest();
        xhr.open('POST', this.action, true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest'); // Optional
        xhr.onload = function () {
            if (xhr.status >= 200 && xhr.status < 300) {
                // Request was successful, handle the response
                var responseData = JSON.parse(xhr.responseText);
                // Handle the response data accordingly

                // Check if success message exists and display it
                if (successMessage) {
                    successMessage.style.display = 'block';
                    setTimeout(function() {
                        successMessage.style.display = 'none';
                    }, 5000);
                }
            } else {
                // Request failed, handle the error
                console.error('Request failed with status', xhr.status);
            }
        };
        xhr.onerror = function () {
            // Request errored, handle the error
            console.error('Request errored');
        };
        xhr.send(formData);
    });

    // Close the error message after 5 seconds if it exists
    if (errorMessage) {
        setTimeout(function() {
            errorMessage.style.display = 'none';
        }, 5000);
    }
});
