// modify-student.js

$(document).ready(function() {
    // Function to handle form submission
    $('#studentForm').submit(function(event) {
        // Prevent default form submission
        event.preventDefault();
        
        // Perform form validation
        var valid = validateForm();
        
        if (valid) {
            // If form is valid, submit the form
            this.submit();
        }
    });

    // Function to validate form data
    function validateForm() {
        var valid = true;

        // Check if roll number is entered
        if (!$('#roll_number').val()) {
            // If roll number is not entered, show an error message
            $('#error_message').text('Roll number is required.');
            valid = false;
            return valid;
        } else {
            // Clear any previous error messages
            $('#error_message').text('');
        }

        // Check if at least one other field (besides roll number) is entered
        var otherFieldsEntered = false;
        $('#studentForm input[type="text"], #studentForm input[type="date"]').not('#roll_number').each(function() {
            if ($(this).val()) {
                otherFieldsEntered = true;
                return false; // Exit loop if at least one other field is entered
            }
        });

        if (!otherFieldsEntered) {
            // If no other fields (besides roll number) are entered, show an error message
            $('#error_message').text('At least one other field (besides roll number) is required.');
            valid = false;
        } else {
            // Clear any previous error messages
            $('#error_message').text('');
        }

        // Check if graduation date is later than enrollment date
        var enrollmentDate = new Date($('#enrollment_date').val());
        var graduationDate = new Date($('#graduation_date').val());

        if (graduationDate <= enrollmentDate) {
            // If graduation date is not later than enrollment date, show an error message
            $('#error_message').text('Graduation date must be later than enrollment date.');
            valid = false;
        }

        return valid;
    }
});
