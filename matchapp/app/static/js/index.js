function createUser() {
    window.location.href = "/register";
}

function loginUser() {
    let userId = prompt("Please enter your User ID:");
    if (userId && Number.isInteger(Number(userId))) {
        window.location.href = `/profile/${userId}`;}
    else if(!userId){

    }

    else {
        alert("Please enter a valid user id");
    }
 
}