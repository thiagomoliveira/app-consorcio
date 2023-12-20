function setDescriptionContent(description, state) {
    description.innerHTML = state;
}

function configureDescription(descriptionSelector) {
    const description = document.querySelector(descriptionSelector);

    document.querySelectorAll('path').forEach((el) =>
        el.addEventListener('mouseover', (event) => {
            event.target.className = "enabled";
            description.classList.add("active");
            setDescriptionContent(description, event.target.id);
        })
    );

    document.querySelectorAll('path').forEach((el) =>
        el.addEventListener("mouseout", () => {
            description.classList.remove("active");
        })
    );

    document.onmousemove = function (e) {
        description.style.left = e.pageX + "px";
        description.style.top = (e.pageY - 70) + "px";
    };
}


configureDescription(".tooltip")
