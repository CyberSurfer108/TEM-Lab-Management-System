



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
