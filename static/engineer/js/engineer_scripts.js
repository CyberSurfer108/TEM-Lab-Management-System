async function loadContacts(element, selectId) {
    try {
        // Fetch data and log to confirm data came through
        const response = await fetch('/contact_accounts');
        const data = await response.json();
        console.log(data);

        // Add the select input and options to the add form 
        const inputDiv = document.getElementById(element);
        const inputElement = document.createElement('select');
        inputElement.id = 'contactId'
        inputElement.name = 'contactId'

        data.forEach(contact => {
            const option = document.createElement('option');
            option.value = contact.id;
            option.textContent = `${contact.first_name} ${contact.last_name}`
            inputElement.appendChild(option);

        })
        inputElement.value = selectId;
        inputDiv.appendChild(inputElement);
    }
    catch (err) {
        console.error("Failed to load companies:", err)
    }
}

// Load account data on Open
loadContacts('customer');

async function postData(url, data) {
    const res = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    if (!res.ok) {
        throw new Error(`HTTP error ${res.status}`);
    }
    const result = await res.json();
    console.log(result)
    return result;
}
