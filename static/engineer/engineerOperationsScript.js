
const dashboardSection = document.getElementById('dashboard');
const queueSection = document.getElementById('full-queue');

queueSection.hidden = true;

document.getElementById("queue-button").addEventListener("click", function () {
    if (queueSection.hidden) {
        queueSection.hidden = false;
        dashboardSection.hidden = true;
    };
});

document.getElementById("dashboard-button").addEventListener("click", function () {
    if (dashboardSection.hidden) {
        queueSection.hidden = true;
        dashboardSection.hidden = false;
    };
})


const loadMyOrders = () => {
    fetch('/my_orders')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('my-orders-data');
            tableBody.innerHTML = "";
            data.forEach(order => {
                const newRow = document.createElement("tr");
                newRow.innerHTML = `
            <td><button class='remove-btn' data-id="${order.order_id}" onclick="removeFromMyQueue(event)">-</button></td>
            <td>${order.order_id}</td>
            <td>${order.company}</td>
            <td>${order.customer_name}</td>
            <td>${order.wafer_id}</td>
            <td>${order.chip_id}</td>
            <td>${order.lamella_id}</td>
            <td>${order.cut_direction}</td>
            <td>${order.substrate}</td>
            <td>${order.feature_name}</td>
            <td>${order.due_date}</td>
            <td>${order.employee_name}</td>
            <td><button class='instruction-btn' data-id="${order.id}">Instructions</button></td>
            <td><button class='images-btn' data-id="${order.id}">Images</button></td>
            <td><button class='complete-btn' data-id="${order.id}">Complete</button></td>
            `;
                tableBody.appendChild(newRow);
            });
        });
}
loadMyOrders();


const loadUnassignedOrders = () => {
    fetch('/orders')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('orders-data');
            tableBody.innerHTML = "";
            data.forEach(order => {
                const newRow = document.createElement("tr");
                newRow.innerHTML = `
            <td><button class='assign-btn' data-id="${order.order_id}" onclick="addToMyQueue(event)">+</button></td>
            <td>${order.order_id}</td>
            <td>${order.company}</td>
            <td>${order.customer_name}</td>
            <td>${order.wafer_id}</td>
            <td>${order.chip_id}</td>
            <td>${order.lamella_id}</td>
            <td>${order.cut_direction}</td>
            <td>${order.substrate}</td>
            <td>${order.feature_name}</td>
            <td>${order.service_id}</td>
            <td>${order.employee_name}</td>
            <td><button class='instruction-btn' data-id="${order.id}">Instructions</button></td>
            <td><button class='images-btn' data-id="${order.id}">Images</button></td>
            <td><button class='complete-btn' data-id="${order.order_id}">Complete</button></td>
            `;
                tableBody.appendChild(newRow);

            });
        });
};

loadUnassignedOrders();

function addToMyQueue(event) {
    Id = event.target.getAttribute('data-id');
    fetch("/assign_order", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ orderId: Id })
    }).then(response => response.json()).then(data => {

        loadUnassignedOrders();
        loadMyOrders();
    }).catch(error =>
        console.error('error:', error))

}


function removeFromMyQueue(event) {
    Id = event.target.getAttribute('data-id');
    fetch("/unassign_order", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ orderId: Id })
    }).then(response => response.json())
        .then(data => {
            loadMyOrders();
            loadUnassignedOrders();
        })
        .catch(error => console.error("error:", error))
}

