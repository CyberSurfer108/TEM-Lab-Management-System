
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
});


fetch('/my_orders')
    .then(response => response.json())
    .then(data => {
        const tableBody = document.getElementById('my-orders-data');
        data.forEach(order => {
            const newRow = document.createElement("tr");
            newRow.innerHTML = `
            <td><button class='remove-btn' data-id="${order.id}">-</button></td>
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

fetch('/orders')
    .then(response => response.json())
    .then(data => {
        const tableBody = document.getElementById('orders-data');
        data.forEach(order => {
            const newRow = document.createElement("tr");
            newRow.innerHTML = `
            <td><button class='assign-btn' data-id="${order.id}">+</button></td>
            <td>${order.id}</td>
            <td>${order.company}</td>
            <td>${order.customer_name}</td>
            <td>${order.wafer_id}</td>
            <td>${order.chip_id}</td>
            <td>${order.lamella_id}</td>
            <td>${order.cut_direction}</td>
            <td>${order.substrate}</td>
            <td>${order.name}</td>
            <td>${order.service_id}</td>
            <td>${order.assigned_employee_id}</td>
            <td><button class='instruction-btn' data-id="${order.id}">Instructions</button></td>
            <td><button class='images-btn' data-id="${order.id}">Images</button></td>
            <td><button class='complete-btn' data-id="${order.id}">Complete</button></td>
            `;
            tableBody.appendChild(newRow);
        });


    });





