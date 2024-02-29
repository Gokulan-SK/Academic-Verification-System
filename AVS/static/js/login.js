// login.js

$(document).ready(function() {
    // Submit login form
    $('#login-form').submit(function(e) {
        e.preventDefault(); // Prevent form submission
        var username = $('#username').val();
        var password = $('#password').val();
        
        // Send AJAX request to Django view for user authentication
        $.ajax({
            type: 'POST',
            url: '{% url "login" %}',
            data: {
                'username': username,
                'password': password,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response) {
                // Handle success response
                console.log(response);
                // Redirect to dashboard or display success message
            },
            error: function(xhr, errmsg, err) {
                // Handle error response
                console.log(xhr.status + ": " + xhr.responseText); // Log error to console
                // Display error message to user
            }
        });
    });
});
