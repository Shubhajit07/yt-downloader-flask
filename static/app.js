var sB = document.querySelector("#sB");
var urlfeed = document.querySelector("#urlInvalid");

const isYTlink = link =>{
    const regex=/^(?:https?:\/\/)?(?:www\.)?(?:m\.)?(?:youtube\.com\/(?:watch\?v=|shorts\/)?|youtu\.be\/)([\w\-]{11})(?:\S+)?$/
    return regex.test(link)
}

function url_(u) {
    if (isYTlink(u) === false) {
        if (url.classList.contains("is-valid")) {
            url.classList.remove("is-valid");
        }
        url.classList.add("is-invalid");
        sB.disabled = true;
    } else {
        if (url.classList.contains("is-invalid")) {
            url.classList.remove("is-invalid");
        }
        url.classList.add("is-valid");
        sB.disabled = false;

    }
}