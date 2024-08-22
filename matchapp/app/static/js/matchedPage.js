function likeUser(uid1, uid2) {
    window.location.href = `/like/${uid1}/${uid2}`;
}

function unlikeUser(uid1, uid2) {
    window.location.href = `/unlike/${uid1}/${uid2}`;
}

function back(uid1) {
    window.location.href = `/profile/${uid1}`;
}