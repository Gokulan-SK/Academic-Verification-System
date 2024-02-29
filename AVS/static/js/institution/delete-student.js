function confirmDelete() {
    var rollNumber = document.getElementById('roll_number').value;
    var confirmDelete = confirm("Are you sure you want to delete the student record with roll number " + rollNumber + "?");
    if (confirmDelete) {
        document.getElementById('deleteForm').submit();
    }
}
