document.getElementById('myDropdown').addEventListener('change', function() {
    const selectedOption = this.options[this.selectedIndex];
    if (selectedOption.value !== '') {// Ignore default option
       window.location.href = selectedOption.getAttribute('data-url');
    }
});