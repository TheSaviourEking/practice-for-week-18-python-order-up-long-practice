document.addEventListener('DOMContentLoaded', () => {
    const updateFormAction = () => {

        const tableSelect = document.getElementById('open-tables');
        const employeeSelect = document.getElementById('servers');

        const tableId = tableSelect.value;
        const employeeId = employeeSelect.value;

        // Ensure both IDs are selected before updating the action
        if (tableId && employeeId) {
            const form = document.getElementById('assignForm');
            form.action = `/assign_table/${tableId}/${employeeId}/`;
        } else {
            alert("Please select both a table and a server.");
        }
    }

    const assignForm = document.getElementById('assignForm');
    assignForm.addEventListener('submit', e => {
        e.preventDefault()

        updateFormAction();

        // Check if action was updated successfully before submitting
        const tableSelect = document.getElementById('open-tables');
        const employeeSelect = document.getElementById('servers');

        if (parseInt(tableSelect.value) && parseInt(employeeSelect.value)) {
            // Now allow the form to submit
            assignForm.submit();
        } else {
            e.preventDefault(); // Prevent submission if not ready
        }
    })
})
