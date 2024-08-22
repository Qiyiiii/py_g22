function createUser() {
    window.location.href = "/register";
}

function loginUser() {
    let userId = prompt("Please enter your User ID:");
    if (userId) {
        window.location.href = `/profile/${userId}`;
    }
}