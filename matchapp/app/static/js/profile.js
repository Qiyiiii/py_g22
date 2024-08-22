function add_interest(uid) {
    let new_interest = prompt("Please enter your interest:");
    if (new_interest) {
        $.ajax({
            url: '/add_interest/' + uid,
            type: 'POST',
            data: {interest: new_interest},
            success: function(response) {
                location.reload();
            }
        });
    }
}

function match(uid) {
    window.location.href = `/match/${uid}`;
}

function setting(uid) {
    window.location.href = `/setting/${uid}`;
}

function view_liked(uid) {
    window.location.href = `/liked-users/${uid}`;
}

function view_unliked(uid) {
    window.location.href = `/unliked-users/${uid}`;
}

function view_mutual_liked(uid) {
    window.location.href = `/mutually-liked-users/${uid}`;
}

function view_top_5(uid) {
    window.location.href = `/top_user/${uid}`;
}

function deleteUser(uid) {
    if (confirm("Are you sure you want to delete your account?")) {
        $.ajax({
            url: `/delete_user/${uid}`,
            type: 'POST',
            success: function() {
                window.location.href = `/`;
            },
            error: function() {
                alert("Failed to delete the account.");
            }
        });
    }
}

function edit_name(uid){
    let content = prompt("Please enter your new name");
    if (content) {
        $.ajax({
            url: '/editname/' + uid,
            type: 'POST',
            data: {content: content},
            success: function(response) {
                location.reload();
            }
        });
    }
}

function edit_gender(uid){
    let content = prompt("Please claim your new gender");
    if (content) {
        $.ajax({
            url: '/editgender/' + uid,
            type: 'POST',
            data: {content: content},
            success: function(response) {
                location.reload();
            }
        });
    }
}

function edit_location(uid){
    let content = prompt("Please change to your new location");
    if (content) {
        $.ajax({
            url: '/editlocation/' + uid,
            type: 'POST',
            data: {content: content},
            success: function(response) {
                location.reload();
            }
        });
    }
}

function edit_age(uid){
    let content = prompt("Please change to your new age");
    if (content) {
        $.ajax({
            url: '/editage/' + uid,
            type: 'POST',
            data: {content: content},
            success: function(response) {
                location.reload();
            }
        });
    }
}

function back(uid) {
    window.location.href = '/';
}

window.onload = function() {
    var messages = JSON.parse('{{ get_flashed_messages(with_categories=true)|tojson }}');
    messages.forEach(function(message) {
        alert(message[1]);
    });
};