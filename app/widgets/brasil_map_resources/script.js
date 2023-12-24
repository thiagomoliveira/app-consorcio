let mapData = {};

function receiveData(data) {
    mapData = data;
}

function setDescriptionContent(description, stateId) {
    // Check if the state is in the data; if not, set total to 0
    const totalNotifications = mapData[stateId] ? mapData[stateId].todas : 0;
    description.innerHTML = `Total: ${totalNotifications}`;
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

configureDescription(".tooltip");
