document.addEventListener("DOMContentLoaded", () => {
    const deleteButtons = document.querySelectorAll(".delete-btn");
    deleteButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const itemId = button.getAttribute("data-id");
            const confirmed = confirm("Are you sure you want to delete this item?");
            if(confirmed) {
                window.location.href = `/delete/${itemId}`;
        
            }
        });
    });
});