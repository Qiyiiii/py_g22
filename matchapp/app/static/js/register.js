function toggleInterest(button) {
    button.classList.toggle("selected");
    var interest = button.getAttribute("data-interest");
    var interestsInput = document.getElementById("interests");
    var interestsArray = interestsInput.value ? interestsInput.value.split(",") : [];
    
    if (button.classList.contains("selected")) {
        interestsArray.push(interest);
    } else {
        interestsArray = interestsArray.filter(i => i !== interest);
    }

    interestsInput.value = interestsArray.join(",");
    console.log("Selected Interests:", interestsInput.value);
}

function updateSelectedInterests(interestsArray) {
    var display = document.getElementById("selected-interests");
    display.innerHTML = interestsArray.map(interest => `<span class="interest-tag">${interest}</span>`).join(" ");
}

document.querySelector("form").addEventListener("submit", function() {
    var interestsInput = document.getElementById("interests");
    console.log("Submitting Interests:", interestsInput.value);
});